from app import App
import datetime
#from PIL import Image
import pyIslSdk

class SonarApp(App):
    def __init__(self):
        super().__init__()
        self.pingCount = 0
        self.sonar_data = pyIslSdk.SonarDataStore()
        self.palette = pyIslSdk.Palette()
        self.sonar_image = pyIslSdk.SonarImage()
        self.sonar_texture = pyIslSdk.SonarImage()

    def subscribe(self):
        super().subscribe()
        self.device.ahrs.on_data.connect(self.on_ahrs_data)
        self.device.gyro.on_data.connect(self.on_gyro_data)
        self.device.accel.on_data.connect(self.on_accel_data)
        self.device.mag.on_data.connect(self.on_mag_data)
        self.device.on_settings_updated.connect(self.on_settings_updated)
        self.device.on_head_homed.connect(self.on_head_homed)
        self.device.on_ping_data.connect(self.on_ping_data)
        self.device.on_echo_data.connect(self.on_echo_data)
        self.device.on_pwr_and_temp.connect(self.on_pwr_and_temp)
#
    def unsubscribe(self):
        super().unsubscribe()
        self.device.ahrs.on_data.disconnect(self.on_ahrs_data)
        self.device.gyro.on_data.disconnect(self.on_gyro_data)
        self.device.accel.on_data.disconnect(self.on_accel_data)
        self.device.mag.on_data.disconnect(self.on_mag_data)
        self.device.on_settings_updated.disconnect(self.on_settings_updated)
        self.device.on_head_homed.disconnect(self.on_head_homed)
        self.device.on_ping_data.disconnect(self.on_ping_data)
        self.device.on_echo_data.disconnect(self.on_echo_data)
        self.device.on_pwr_and_temp.disconnect(self.on_pwr_and_temp)

    def do_task(self, key):
        if key == 'd':
            self.device.set_system_settings(pyIslSdk.Sonar.System(), True)
            self.device.set_acoustic_settings(pyIslSdk.Sonar.Acoustic(), True)
            self.device.set_setup_settings(pyIslSdk.Sonar.Setup(), True)
        elif key == 's':
            self.device.save_config(self.device.info.pn_sn_str() + ' settings.xml')
        elif key == 'r':
            self.device.test_pattern(True)
            self.device.start_scanning()
        elif key == 'R':
            self.device.stop_scanning()
        elif key == 'p':
            self.palette.save_bmp('palette.bmp', 1000, 100, True)
        elif key == 'i':
            self.sonar_image.save_bmp('sonar.bmp')
        elif key == 't':
            self.sonar_texture.save_bmp('texture.bmp')

    def set_logger(self, logger):
        self.logger = logger
        if self.device is not None:
            self.device.set_logger(logger, pyIslSdk.SeaViewAppType.sonar)

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

    def on_settings_updated(self, device, ok, setting_type):
        if ok:
            print(device, setting_type, "settings updated")
            if setting_type == pyIslSdk.Sonar.Settings.Type.Setup:
                self.sonar_image.set_sector_area(0, self.device.settings.setup.max_range_mm, self.device.settings.setup.sector_start, self.device.settings.setup.sector_size)
                self.sonar_texture.set_buffer(self.device.settings.setup.image_data_point, int(pyIslSdk.Sonar.max_angle / abs(self.device.settings.setup.step_size)), True)
                self.sonar_texture.set_sector_area(0, self.device.settings.setup.max_range_mm, self.device.settings.setup.sector_start, self.device.settings.setup.sector_size)
        else:
            print(device, setting_type, "settings update failed")

    def on_head_homed(self, device, state):
        print(device, "head homed", state)

    def on_ping_data(self, device, ping_data):
        self.sonar_data.add(ping_data)
        self.pingCount += 1

        if self.pingCount >= (pyIslSdk.Sonar.max_angle / device.settings.setup.step_size) / 8:
            print("Sonar has completed an 1/8th of a revolution. Saving image...")
            self.pingCount = 0
            self.sonar_image.render(self.sonar_data, self.palette, True)
            self.sonar_image.save_bmp('sonar.bmp')
            self.sonar_texture.render_texture(self.sonar_data, self.palette, True)
            self.sonar_texture.save_bmp('texture.bmp')
            
            #img = Image.fromarray(self.sonar_image, 'RGBA')
            #img.save('snr.png')

    def on_echo_data(self, device, echo_data):
        print(device, "echo data", echo_data)

    def on_pwr_and_temp(self, device, pwr_and_temp):
        print(device, "pwr and temp", pwr_and_temp)

    def connectionEvent(self):
        rate = self.device.sensor_rates
        rate.ahrs = 100
        rate.gyro = 0
        rate.accel = 0
        rate.mag = 0
        rate.voltage_and_temp = 1000
        self.device.set_sensor_rates(rate)

        self.sonar_image.set_buffer(1000, 1000, True)
        self.sonar_image.set_sector_area(0, self.device.settings.setup.max_range_mm, self.device.settings.setup.sector_start, self.device.settings.setup.sector_size)
        self.sonar_image.use_biliner_interpolation = True

        #Optimal texture size to pass to the GPU - each pixel represents a data point. The GPU can then map this texture to circle (triangle fan)
        self.sonar_texture.set_buffer(self.device.settings.setup.image_data_point, int(pyIslSdk.Sonar.max_angle / abs(self.device.settings.setup.step_size)), True)
        self.sonar_texture.set_sector_area(0, self.device.settings.setup.max_range_mm, self.device.settings.setup.sector_start, self.device.settings.setup.sector_size)
        self.sonar_texture.use_biliner_interpolation = False

        self.device.test_pattern(True)
        self.device.start_scanning()
        #self.palette.set([(0xff00ff00, 0), (0xffff0000, 32768), (0xff0000ff, 65535)], 0)
        self.palette.save_bmp('palette.bmp', 1000, 100, True)
        #img_array = self.palette.render(1000,100, True)

        if self.device.start_logging():
            print("Logging started")
        else:
            print("Logging failed to start")