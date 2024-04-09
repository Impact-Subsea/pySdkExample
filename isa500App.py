from app import App
from pyIslSdk import SeaViewAppType, Isa500
import datetime

class Isa500App(App):
    def __init__(self):
        super().__init__()

    def subscribe(self):
        super().subscribe()
        self.device.ahrs.on_data.connect(self.on_ahrs_data)
        self.device.gyro.on_data.connect(self.on_gyro_data)
        self.device.accel.on_data.connect(self.on_accel_data)
        self.device.mag.on_data.connect(self.on_mag_data)
        self.device.on_echo.connect(self.on_echo)
        self.device.on_echogram_data.connect(self.on_echogram_data)
        self.device.on_temperature.connect(self.on_temperature)
        self.device.on_voltage.connect(self.on_voltage)
        self.device.on_trigger.connect(self.on_trigger)
        self.device.on_script_data_received.connect(self.on_script_data_received)
        self.device.on_settings_updated.connect(self.on_settings_updated)

    def unsubscribe(self):
        super().unsubscribe()
        self.device.ahrs.on_data.disconnect(self.on_ahrs_data)
        self.device.gyro.on_data.disconnect(self.on_gyro_data)
        self.device.accel.on_data.disconnect(self.on_accel_data)
        self.device.mag.on_data.disconnect(self.on_mag_data)
        self.device.on_echo.disconnect(self.on_echo)
        self.device.on_echogram_data.disconnect(self.on_echogram_data)
        self.device.on_temperature.disconnect(self.on_temperature)
        self.device.on_voltage.disconnect(self.on_voltage)
        self.device.on_trigger.disconnect(self.on_trigger)
        self.device.on_script_data_received.disconnect(self.on_script_data_received)
        self.device.on_settings_updated.disconnect(self.on_settings_updated)

    def do_task(self, key):
        if key == 'd':
            self.device.set_settings(Isa500.Settings(), True)
        elif key == 's':
            self.device.save_config(self.device.info.pn_sn_str() + ' settings.xml')
        elif key == 'p':
            self.device.ping_now()

    def set_logger(self, logger):
        self.logger = logger
        if self.device is not None:
            self.device.set_logger(logger, SeaViewAppType.isa500)

    def on_ahrs_data(self, ahrs, time_us, quaternion, mag_heading_rad, turns_count):
        time = datetime.datetime.fromtimestamp(time_us/1000000.0)
        eular_angles = quaternion.to_euler_angles().rad_to_deg()
        print(eular_angles)

    def on_gyro_data(self, gyro, data):
        print("gyro data", data)

    def on_accel_data(self, accel, data):
        print("accel data", data)

    def on_mag_data(self, mag, data):
        print("mag data", data)

    def on_echo(self, device, time_us, selected_idx, total_echo_count, echos):
        time = datetime.datetime.fromtimestamp(time_us/1000000.0)
        print(device, "echo count:", total_echo_count, "time stamp", time, selected_idx, echos)

    def on_echogram_data(self, device, data):
        print(device, "echogram data", data)

    def on_temperature(self, device, temperature):
        print(device, "temperature", temperature)

    def on_voltage(self, device, voltage):
        print(device, "voltage", voltage)

    def on_trigger(self, device, edge):
        print(device, "trigger", edge)

    def on_script_data_received(self, device):
        print(device, "script data received")

    def on_settings_updated(self, device, ok):
        print(device, "settings updated", ok)

    #

    def connectionEvent(self):
        rate = self.device.sensor_rates
        rate.ping = 1000
        rate.ahrs = 1000
        rate.gyro = 0
        rate.accel = 0
        rate.mag = 0
        rate.temperature = 0
        rate.voltage = 0
        self.device.set_sensor_rates(rate)

        if self.device.start_logging():
            print("Logging started")
        else:
            print("Logging failed to start")
