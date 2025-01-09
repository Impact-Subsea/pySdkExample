from devices.deviceManager import DeviceManager
import pyIslSdk as sdk
from devices.imuManager import AhrsManager, GyroManager, AccelManager, MagManager
import datetime

class SonarManager(DeviceManager):
    def __init__(self, device: sdk.Sonar) -> None:
        self.pingCount = 0
        self.sonar_data = sdk.SonarDataStore()
        self.palette = sdk.Palette()
        self.sonar_image = sdk.SonarImage()
        self.sonar_texture = sdk.SonarImage()
        self.ahrs_manager = AhrsManager(device.ahrs)
        self.gyro_manager = GyroManager(device.gyro)
        self.accel_manager = AccelManager(device.accel)
        super().__init__(device)

    def _subscribe(self) -> None:
        super()._subscribe()
        self.ahrs_manager.subscribe()
        self.gyro_manager.subscribe()
        self.accel_manager.subscribe()
        self.device.on_settings_updated.connect(self.__on_settings_updated)
        self.device.on_head_indexes_acquired.connect(self.__on_head_indexes_acquired)
        self.device.on_ping_data.connect(self.__on_ping_data)
        self.device.on_echo_data.connect(self.__on_echo_data)
        self.device.on_pwr_and_temp.connect(self.__on_pwr_and_temp)
        self.device.on_motor_slip.connect(self.__on_motor_slip)
        self.device.on_motor_move_complete.connect(self.__on_motor_move_complete)

    def _unsubscribe(self) -> None:
        super()._unsubscribe()
        self.ahrs_manager.unsubscribe()
        self.gyro_manager.unsubscribe()
        self.accel_manager.unsubscribe()
        self.device.on_settings_updated.disconnect(self.__on_settings_updated)
        self.device.on_head_indexes_acquired.disconnect(self.__on_head_indexes_acquired)
        self.device.on_ping_data.disconnect(self.__on_ping_data)
        self.device.on_echo_data.disconnect(self.__on_echo_data)
        self.device.on_pwr_and_temp.disconnect(self.__on_pwr_and_temp)
        self.device.on_motor_slip.disconnect(self.__on_motor_slip)
        self.device.on_motor_move_complete.disconnect(self.__on_motor_move_complete)

    def __on_settings_updated(self, device: sdk.Sonar, ok: bool, setting_type: sdk.Sonar.Settings.Type) -> None:
        if ok:
            print(device, setting_type, 'settings updated')
            if setting_type == sdk.Sonar.Settings.Type.Setup:
                self.sonar_image.set_sector_area(0, self.device.settings.setup.max_range_mm, self.device.settings.setup.sector_start, self.device.settings.setup.sector_size)
                self.sonar_texture.set_buffer(self.device.settings.setup.image_data_point, int(sdk.Sonar.max_angle / abs(self.device.settings.setup.step_size)), True)
                self.sonar_texture.set_sector_area(0, self.device.settings.setup.max_range_mm, self.device.settings.setup.sector_start, self.device.settings.setup.sector_size)
        else:
            print(device, setting_type, 'settings update failed')

    def __on_head_indexes_acquired(self, device: sdk.Sonar, result: sdk.Sonar.HeadIndexes) -> None:
        print(device, 'indexes acquired', result.state)
        print(f'slippage:{result.slippage}, std dev:{result.std_deviation}, hysteresis:{result.hysteresis_correction}, width:{result.width_correction}')
        for index in result.indexes:
            print('index', index.idx, index.level, index.dir)

    def __on_ping_data(self, device: sdk.Sonar, ping_data: sdk.Sonar.Ping) -> None:
        self.sonar_data.add(ping_data)
        self.pingCount += 1

        if self.pingCount >= abs(sdk.Sonar.max_angle / device.settings.setup.step_size) / 8:
            print('Sonar has completed an 1/8th of a revolution. Saving image...')
            self.pingCount = 0
            self.sonar_image.render(self.sonar_data, self.palette, True)
            self.sonar_image.save_bmp('sonar.bmp')
            self.sonar_texture.render_texture(self.sonar_data, self.palette, True)
            self.sonar_texture.save_bmp('texture.bmp')

    def __on_echo_data(self, device: sdk.Sonar, echo_data: sdk.Sonar.Echos) -> None:
        print(device, 'echo data', echo_data)
        
    def __on_pwr_and_temp(self, device: sdk.Sonar, pwr_and_temp: sdk.Sonar.CpuPowerTemp) -> None:
        print(device, 'pwr and temp\n', pwr_and_temp)

    def __on_motor_slip(self, device: sdk.Sonar) -> None:
        print(device, 'Warning motor has slipped')
  
    def __on_motor_move_complete(self, device: sdk.Sonar, complete: bool) -> None:
        print(device, 'motor move complete', complete)

    def _connection_event(self) -> None:
        super()._connection_event()
        rate = self.device.sensor_rates
        rate.ahrs = 1000
        rate.gyro = 0
        rate.accel = 0
        rate.mag = 0
        rate.voltage_and_temp = 0
        self.device.set_sensor_rates(rate)
       
        self.sonar_image.set_buffer(1000, 1000, True)
        self.sonar_image.set_sector_area(0, self.device.settings.setup.max_range_mm, self.device.settings.setup.sector_start, self.device.settings.setup.sector_size)
        self.sonar_image.use_biliner_interpolation = True

        #Optimal texture size to pass to the GPU - each pixel represents a data point. The GPU can then map this texture to circle (triangle fan)
        self.sonar_texture.set_buffer(self.device.settings.setup.image_data_point, int(sdk.Sonar.max_angle / abs(self.device.settings.setup.step_size)), True)
        self.sonar_texture.set_sector_area(0, self.device.settings.setup.max_range_mm, self.device.settings.setup.sector_start, self.device.settings.setup.sector_size)
        self.sonar_texture.use_biliner_interpolation = False

        #print(self.device.settings.to_dict())
        #self.palette.set([(0xff00ff00, 0), (0xffff0000, 32768), (0xff0000ff, 65535)], 0)
        #self.palette.save_bmp('palette.bmp', 1000, 100, True)

    def set_logger(self, logger):
        self.logger = logger
        self.device.set_logger(logger, sdk.SeaViewAppType.sonar)

    def process_command(self, cmd: str) -> None:
        if cmd == 'd':
            self.device.set_system_settings(sdk.Sonar.System(), True)
            self.device.set_acoustic_settings(sdk.Sonar.Acoustic(), True)
            self.device.set_setup_settings(sdk.Sonar.Setup(), True)
        elif cmd == 's':
            self.device.save_config(self.device.info.pn_sn + ' settings.xml')
        elif cmd == 'r':
            self.device.start_scanning()
        elif cmd == 'R':
            self.device.stop_scanning()
        elif cmd == 'p':
            self.palette.save_bmp('palette.bmp', 1000, 100, True)
        elif cmd == 'i':
            self.sonar_image.save_bmp('sonar.bmp')
        elif cmd == 't':
            self.sonar_texture.save_bmp('texture.bmp')
        elif cmd == 'h':
            print("Checking head slippage")
            self.device.check_head_idx(False)