from devices.deviceManager import DeviceManager
import pyIslSdk as sdk
from devices.imuManager import AhrsManager, GyroManager, AccelManager, MagManager
import datetime
import math
import copy

class Isa500Manager(DeviceManager):
    def __init__(self, device: sdk.Isa500) -> None:
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
        self.device.on_echo.connect(self.__on_echo)
        self.device.on_echogram_data.connect(self.__on_echogram_data)
        self.device.on_temperature.connect(self.__on_temperature)
        self.device.on_voltage.connect(self.__on_voltage)
        self.device.on_trigger.connect(self.__on_trigger)
        self.device.on_script_data_received.connect(self.__on_script_data_received)
        self.device.on_settings_updated.connect(self.__on_settings_updated)
        self.device.on_ping_test.connect(self.__on_ping_test)
        
    def _unsubscribe(self) -> None:
        super()._unsubscribe()
        self.ahrs_manager.unsubscribe()
        self.gyro_manager.unsubscribe()
        self.accel_manager.unsubscribe()
        self.mag_manager.unsubscribe()
        self.device.on_echo.disconnect(self.__on_echo)
        self.device.on_echogram_data.disconnect(self.__on_echogram_data)
        self.device.on_temperature.disconnect(self.__on_temperature)
        self.device.on_voltage.disconnect(self.__on_voltage)
        self.device.on_trigger.disconnect(self.__on_trigger)
        self.device.on_script_data_received.disconnect(self.__on_script_data_received)
        self.device.on_settings_updated.disconnect(self.__on_settings_updated)
        self.device.on_ping_test.disconnect(self.__on_ping_test)

    def __on_echo(self, device: sdk.Isa500, time_us: int, selected_idx: int, total_echo_count: int, echos: list[sdk.Isa500.Echo]) -> None:
        time = datetime.datetime.fromtimestamp(time_us/1000000.0)
        print(device, 'echo count:', total_echo_count, 'time stamp', time, selected_idx, echos)

    def __on_echogram_data(self, device: sdk.Isa500, data: list[int]) -> None:
        print(device, 'echogram data', data)

    def __on_temperature(self, device: sdk.Isa500, temperature: float) -> None:
        print(device, 'temperature', temperature)

    def __on_voltage(self, device: sdk.Isa500, voltage: float) -> None:
        print(device, 'voltage', voltage)

    def __on_trigger(self, device: sdk.Isa500, edge: bool) -> None:
        print(device, 'trigger', edge)

    def __on_script_data_received(self, device: sdk.Isa500) -> None:
        print(device, 'script data received')

    def __on_settings_updated(self, device: sdk.Isa500, ok: bool) -> None:
        print(device, 'settings updated', ok)

    def __on_ping_test(self, device: sdk.Isa500, total_echo_count: int, total_tof: float, correlation: float, signal_energy: float, wave: list[int]) -> None:
        print(device, 'ping test', total_echo_count, total_tof, correlation, signal_energy, wave)

    def _connection_event(self) -> None:
        super()._connection_event()
        rate = self.device.sensor_rates
        rate.ping = 1000
        rate.ahrs = 500
        rate.gyro = 0
        rate.accel = 0
        rate.mag = 0
        rate.voltage = 0
        rate.temperature = 0
        self.device.set_sensor_rates(rate)

    def set_logger(self, logger):
        self.logger = logger
        self.device.set_logger(logger, sdk.SeaViewAppType.isa500)

    def process_command(self, cmd: str) -> None:
        if cmd == 'd':
            self.device.set_settings(sdk.Isa500.Settings(), True)
        elif cmd == 's':
            self.device.save_config(self.device.info.pn_sn + ' settings.xml')
        elif cmd == 'p':
            self.device.ping_now()