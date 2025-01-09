from devices.deviceManager import DeviceManager
import pyIslSdk as sdk
from devices.imuManager import AhrsManager, GyroManager, AccelManager, MagManager
import datetime

class Isd4000Manager(DeviceManager):
    def __init__(self, device: sdk.Isd4000) -> None:
        self.ahrs_manager = AhrsManager(device.ahrs)
        self.gyro_manager = GyroManager(device.gyro)
        self.accel_manager = AccelManager(device.accel)
        self.mag_manager = MagManager(device.mag)
        super().__init__(device)

    def _subscribe(self) -> None:
        super()._subscribe()
        self.ahrs_manager.subscribe()
        self.gyro_manager.subscribe()
        self.accel_manager.subscribe()
        self.mag_manager.subscribe()
        self.device.on_pressure.connect(self.__on_pressure)
        self.device.on_temperature.connect(self.__on_temperature)
        self.device.on_script_data_received.connect(self.__on_script_data_received)
        self.device.on_settings_updated.connect(self.__on_settings_updated)
        self.device.on_pressure_cal_cert.connect(self.__on_pressure_cal_cert)
        self.device.on_temperature_cal_cert.connect(self.__on_temperature_cal_cert)

    def _unsubscribe(self) -> None:
        super()._unsubscribe()
        self.ahrs_manager.unsubscribe()
        self.gyro_manager.unsubscribe()
        self.accel_manager.unsubscribe()
        self.mag_manager.unsubscribe()
        self.device.on_pressure.disconnect(self.__on_pressure)
        self.device.on_temperature.disconnect(self.__on_temperature)
        self.device.on_script_data_received.disconnect(self.__on_script_data_received)
        self.device.on_settings_updated.disconnect(self.__on_settings_updated)
        self.device.on_pressure_cal_cert.disconnect(self.__on_pressure_cal_cert)
        self.device.on_temperature_cal_cert.disconnect(self.__on_temperature_cal_cert)

    def __on_pressure(self, device: sdk.Isd4000, time_us: int, pressure: float, depth: float, pressureRaw: float) -> None:
        time = datetime.datetime.fromtimestamp(time_us/1000000.0)
        print(device, 'pressure', time, pressure, depth)

    def __on_temperature(self, device: sdk.Isd4000, temperature: float, temperatureRaw: float) -> None:
        print(device, 'temperature', temperature)

    def __on_script_data_received(self, device: sdk.Isd4000) -> None:
        print(device, 'script data received')

    def __on_settings_updated(self, device: sdk.Isd4000, ok: bool) -> None:
        print(device, 'settings updated', ok)

    def __on_pressure_cal_cert(self, device: sdk.Isd4000, pressure_cal: sdk.Isd4000.PressureCal) -> None:
        print(device, 'pressure cal', pressure_cal)

    def __on_temperature_cal_cert(self, device: sdk.Isd4000, temperature_cal: sdk.Isd4000.TemperatureCal) -> None:
        print(device, 'temperature cal', temperature_cal)

    def _connection_event(self) -> None:
        super()._connection_event()
        rate = self.device.sensor_rates
        rate.pressure = 500
        rate.temperature = 0
        rate.ahrs = 500
        rate.gyro = 0
        rate.accel = 0
        rate.mag = 0
        self.device.set_sensor_rates(rate)

    def set_logger(self, logger):
        self.logger = logger
        self.device.set_logger(logger, sdk.SeaViewAppType.isd4000)

    def process_command(self, cmd: str) -> None:
        if cmd == 'd':
            self.device.set_settings(Isd4000.Settings(), True)
        elif cmd == 's':
            self.device.save_config(self.device.info.pn_sn + ' settings.xml')