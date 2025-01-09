from devices.deviceManager import DeviceManager
import pyIslSdk as sdk
from devices.imuManager import AhrsManager, GyroManager, AccelManager, MagManager

class Ism3dManager(DeviceManager):
    def __init__(self, device: sdk.Ism3d) -> None:     
        self.ahrs_manager = AhrsManager(device.ahrs)
        self.gyro_manager = GyroManager(device.gyro)
        self.accel_manager = AccelManager(device.accel)
        self.mag_manager = MagManager(device.mag)
        self.gyro_backup_manager = GyroManager(device.gyro_sec)
        self.accel_backup_manager = AccelManager(device.accel_sec)
        super().__init__(device)

    def _subscribe(self) -> None:
        super()._subscribe()
        self.ahrs_manager.subscribe()
        self.gyro_manager.subscribe()
        self.accel_manager.subscribe()
        self.mag_manager.subscribe()
        self.gyro_backup_manager.subscribe()
        self.accel_backup_manager.subscribe()
        self.device.on_script_data_received.connect(self.__on_script_data_received)
        self.device.on_settings_updated.connect(self.__on_settings_updated)
        self.device.on_422_serial_test.connect(self.__on_422_serial_test)

    def _unsubscribe(self) -> None:
        super()._unsubscribe()
        self.ahrs_manager.unsubscribe()
        self.gyro_manager.unsubscribe()
        self.accel_manager.unsubscribe()
        self.mag_manager.unsubscribe()
        self.gyro_backup_manager.unsubscribe()
        self.accel_backup_manager.unsubscribe()
        self.device.on_script_data_received.disconnect(self.__on_script_data_received)
        self.device.on_settings_updated.disconnect(self.__on_settings_updated)
        self.device.on_422_serial_test.disconnect(self.__on_422_serial_test)

    def __on_script_data_received(self, device: sdk.Ism3d) -> None:
        print(device, 'script data received')

    def __on_settings_updated(self, device: sdk.Ism3d, ok : bool) -> None:
        print(device, 'settings updated', ok)

    def __on_422_serial_test(self, device: sdk.Ism3d, str : str) -> None:
        print(device, 'TEST', str)
 
    def _connection_event(self) -> None:
        super()._connection_event()
        rate = self.device.sensor_rates
        rate.ahrs = 0
        rate.gyro = 0
        rate.accel = 0
        rate.mag = 100
        self.device.set_sensor_rates(rate)

    def set_logger(self, logger):
        self.logger = logger
        self.device.set_logger(logger, sdk.SeaViewAppType.ism3d)

    def process_command(self, cmd: str) -> None:
        if cmd == 'd':
            self.device.set_settings(sdk.Ism3d.Settings(), True)
        elif cmd == 's':
            self.device.save_config(self.device.info.pn_sn + ' settings.xml')