import pyIslSdk as sdk
import datetime

class AhrsManager():
    def __init__(self, ahrs: sdk.Ahrs) -> None:
        self.ahrs = ahrs

    def subscribe(self) -> None:
        self.ahrs.on_data.connect(self.__on_ahrs_data)

    def unsubscribe(self) -> None:
        self.ahrs.on_data.disconnect(self.__on_ahrs_data)
    
    def __on_ahrs_data(self, ahrs: sdk.Ahrs, time_us: int, quaternion: sdk.Quaternion, mag_heading_rad: float, turns_count: float) -> None:
        time = datetime.datetime.fromtimestamp(time_us/1000000.0)
        eular_angles = quaternion.to_euler_angles().rad_to_deg()
        print(eular_angles)

class GyroManager:
    def __init__(self, gyro: sdk.GyroSensor) -> None:
        self.gyro = gyro

    def subscribe(self) -> None:
        self.gyro.on_data.connect(self.__on_gyro_data)
        self.gyro.on_cal_change.connect(self.__on_cal_change)
       
    def unsubscribe(self) -> None:
        self.gyro.on_data.disconnect(self.__on_gyro_data)
        self.gyro.on_cal_change.disconnect(self.__on_cal_change)
    
    def __on_gyro_data(self, gyro: sdk.GyroSensor, data: sdk.Vector3) -> None:
        print('gyro data', data)

    def __on_cal_change(self, mag: sdk.GyroSensor, bias: sdk.Vector3) -> None:
        print('cal change', bias)

class AccelManager():
    def __init__(self, accel: sdk.AccelSensor) -> None:
        self.accel = accel

    def subscribe(self) -> None:
        self.accel.on_data.connect(self.__on_accel_data)
        self.accel.on_cal_progress.connect(self.__on_cal_progress)
        self.accel.on_cal_change.connect(self.__on_cal_change)
       
    def unsubscribe(self) -> None:
        self.accel.on_data.disconnect(self.__on_accel_data)
        self.accel.on_cal_progress.disconnect(self.__on_cal_progress)
        self.accel.on_cal_change.disconnect(self.__on_cal_change)
    
    def __on_accel_data(self, accel: sdk.AccelSensor, data: sdk.Vector3) -> None:
        print('accel data', data)

    def __on_cal_progress(self, accel: sdk.AccelSensor, vec: sdk.Vector3, idx: int) -> None:
        print('cal progress', vec, idx)

    def __on_cal_change(self, accel: sdk.AccelSensor, bias: sdk.Vector3, transform: sdk.Matrix3x3) -> None:
        print('cal change', bias, '\n', transform)

class MagManager():
    def __init__(self, mag: sdk.MagSensor) -> None:
        self.mag = mag

    def subscribe(self) -> None:
        self.mag.on_data.connect(self.__on_mag_data)
        self.mag.on_cal_progress.connect(self.__on_cal_progress)
        self.mag.on_cal_change.connect(self.__on_cal_change)
       
    def unsubscribe(self) -> None:
        self.mag.on_data.disconnect(self.__on_mag_data)
        self.mag.on_cal_progress.disconnect(self.__on_cal_progress)
        self.mag.on_cal_change.disconnect(self.__on_cal_change)
    
    def __on_mag_data(self, mag: sdk.MagSensor, data: sdk.Vector3) -> None:
        print('mag data', data)
       
    def __on_cal_progress(self, mag: sdk.MagSensor, vec: sdk.Vector3, size: int) -> None:
        print('cal progress', vec, size)

    def __on_cal_change(self, mag: sdk.MagSensor, bias: sdk.Vector3, transform: sdk.Matrix3x3) -> None:
        print('cal change', bias, '\n', transform)