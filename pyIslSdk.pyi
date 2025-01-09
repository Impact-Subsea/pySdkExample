from typing import Any, Dict, Callable, Optional, overload, Tuple, Union, List
from enum import Enum

class SeaViewAppType:
    ''' When creating log files with the SDK these app types can be used to identify which Seaview app
    should play back the the log file. '''
    isa500: bytes
    ''' The isa500 app type. '''
    isd4000: bytes
    ''' The isd4000 app type. '''
    ism3d: bytes
    ''' The ism3d app type. '''
    fmd: bytes
    ''' The fmd app type. '''
    sonar: bytes
    ''' The sonar app type. '''
    cam: bytes
    ''' The cam app type. '''
    profiler: bytes
    ''' The profiler app type. '''

class Signal:
    def connect(self, callback: Callable[[Any], None]) -> None:
        '''Connect to the signal.

        params
            callback: The callback function.
        '''
        ...

    def disconnect(self, callback: Callable[[Any], None]) -> None:
        '''Disconnect from the signal.

        params
            callback: The callback function.
        '''
        ...
#------------------------------------- Types Bindings ----------------------------------------------
class ConstArray:
    '''A class representing a constant array of bytes.
    This class supports the buffer protocol and __array_interface__.'''
    size: int
    '''The size of the array.'''
    def to_bytes(self) -> bytes:
        '''Return the array as a bytes object.'''
        ...

class ConnectionMeta:
    '''A class representing connection details.'''
    def __init__(self, baudrate: int) -> None: ...
    def __init__(self, ip_address: str, port: int) -> None: ...
    baudrate: int
    '''The baudrate.'''
    ip_address: str
    '''The ip address.'''
    port: int
    '''The TCP/UDP port.'''
    def is_different(self, other: ConnectionMeta) -> bool:
        '''Check if two ConnectionMeta objects are different.
        
        params
            other: The other ConnectionMeta object.

        returns
            True if the objects are different.
        '''
        ...
    
class AutoDiscovery:
    class Type(Enum):
        '''The auto discovery types.'''
        Isl : int
        '''The Impact Subsea Ltd auto discovery type.'''
        Nmea : int
        '''The NMEA auto discovery type.'''

class Connection:
    '''A class representing a connection.'''
    port: SysPort
    '''The Sysport.'''
    meta: ConnectionMeta
    '''The connection meta.'''

class DeviceScript:
    '''A class representing a device script.'''
    def __init__(self) -> None: ...
    def __init__(self, name: str, code: str) -> None: ...
    state: DataState
    '''The script state.'''
    name: str
    '''The script name.'''
    code: str
    '''The script code.'''
    
class DataState(Enum):
    '''The data states.'''
    Invalid : int
    '''The data is invalid.'''
    Pending : int
    '''The data is pending.'''
    Valid : int
    '''The data is valid.'''

class ScriptVars:
    '''A class representing script variables.'''
    class VarType(Enum):
        '''The variable types.'''
        Byte : int
        '''The byte type.'''
        Int : int
        '''The int type.'''
        Real : int
        '''The real type.'''
        ByteArray : int
        '''The byte array type.'''
        IntArray : int
        '''The int array type.'''
        RealArray : int
        '''The real array type.'''

    class Var:
        '''A class representing a script variable.'''
        type: VarType
        '''The variable type.'''
        name: str
        '''The variable name.'''
        description: str
        '''The variable description.'''
    state: DataState
    '''The script state.'''
    vars: List[Var]
    '''The script variables.'''

class Point:
    '''A class representing a point.'''
    x: float
    '''The x value.'''
    y: float
    '''The y value.'''

class Vector3:
    '''A class representing a 3D vector.'''
    x: float
    '''The x value.'''
    y: float
    '''The y value.'''
    z: float
    '''The z value'''

    def __init__(self) -> None: ...
    def __init__(self, x: float, y: float, z: float) -> None: ...
    def zero(self) -> None:
        '''Set the vector to zero.'''
        ...
    def magnitude(self) -> float:
        '''Return the magnitude of the vector.'''
        ...
    def magnitude_sq(self) -> float:
        '''Return the magnitude squared of the vector.'''
        ...
    def normalise(self) -> None:
        '''Return the normalised vector.'''
        ...

    def dot(self, v: Vector3) -> float:
        '''Return the dot product of two vectors.
        
        params
            v: The other vector.
        
        returns
            The dot product.
        '''
        ...

    def cross(self, v: Vector3) -> Vector3:
        '''Return the cross product of two vectors.
        
        params
            v: The other vector.
        
        returns
            The cross product.
        '''
        ...

    def find_closest_cardinal_axis(self) -> Axis:
        '''Return the closest cardinal axis to the vector.
        
        returns
            The closest cardinal axis.
        '''
        ...

    def get_vector_from_axis(axis: Axis) -> Vector3:
        '''Return a vector from an axis.
        
        params
            axis: The axis.
        
        returns
            The vector.
        '''
        ...

    class Axis(Enum):
        '''The vector axis.'''
        xPlus : int
        '''The x plus axis.'''
        xMinus : int
        '''The x minus axis.'''
        yPlus : int
        '''The y plus axis.'''
        yMinus : int
        '''The y minus axis.'''
        zPlus : int
        '''The z plus axis.'''
        zMinus : int
        '''The z minus axis.'''

class Matrix3x3:
    '''A class representing a 3x3 matrix.'''
    def __init__(self) -> None: ...
    '''Initialise the matrix to the identity.'''
    def __init__(self, heading: float, pitch: float, roll: float) -> None: ...
    '''Initialise the matrix from Eular angles.'''
    def __init__(self, down: Vector3, forward: Vector3) -> None: ...
    '''Initialise the matrix from a down anf forward vectors.'''
    m: List[List[float]]
    '''The matrix values.'''
    def identity(self) -> None:
        '''Set the matrix to the identity.'''
        ...
    def transpose(self) -> None:
        '''Transpose the matrix.'''
        ...

class EulerAngles:
    '''A class representing Euler angles.'''
    heading: float
    '''The heading in radians.'''
    pitch: float
    '''The pitch in radians.'''
    roll: float
    '''The roll in radians.'''
    def rad_to_deg(self) -> EulerAngles:
        '''Convert radians to degrees.

        returns
            self with angle in degrees.
        '''
        ...

class Quaternion:
    '''A class representing a quaternion.'''
    def __init__(self) -> None: ...
    def __init__(self, w: float, x: float, y: float, z: float) -> None: ...
    def __init__(self, axis: Vector3, angle: float) -> None: ...
    def __init__(self, axis: Vector3) -> None: ...
    def __init__(self, matrix: Matrix3x3) -> None: ...
    w: float
    '''The w value.'''
    x: float
    '''The x value.'''
    y: float
    '''The y value'''
    z: float
    '''The z value'''

    def conjugate(self) -> Quaternion:
        '''Return the conjugate of the quaternion.
        
        returns
            The conjugate.
        '''
        ...

    def normalise(self) -> Quaternion:
        '''Normalise the quaternion.

        returns
            The normalised quaternion.
        '''
        ...
    
    def magnitude(self) -> float:
        '''Return the magnitude of the quaternion.
        
        returns
            The magnitude.
        '''
        ...
    
    def to_matrix(self) -> Matrix3x3:
        '''Return the quaternion as a matrix.
        
        returns
            The matrix.
        '''
        ...
    
   
    def to_euler_angles(self, heading_offset_rad: float=0) -> EulerAngles:
        '''Return the quaternion as Euler angles.
        
        params
            heading_offset_rad: The heading offset in radians.
        
        returns
            The Euler angles.
        '''
        ...

#------------------------------------- SDK Bindings ------------------------------------------------
class Sdk:
    '''This is the main SDK class. It contains all functionality of the SDK.'''
    def run(self) -> None:
        '''Run the SDK.
        This function should be called periodically to run all SDK tasks and trigger signals.
        A recommended period is between 20ms and 50ms.'''
        ...
    version : str
    '''The SDK version.'''
    ports : SysPortMgr
    '''The port manager object.'''
    devices : DeviceMgr
    '''The device manager object.'''

class DeviceMgr:
    '''A management class for devices.'''
            
    def set_comms_timeouts(self, host_timeout_ms: int, device_timeout_ms: int, tx_retries: int) -> None:
        '''Set the comms timeouts for all devices.
        
        params
            host_timeout_ms: The host timeout in milliseconds.
            device_timeout_ms: The device timeout in milliseconds.
            tx_retries: The number of transmit retries before giving up and disconnecting.
        '''
        ...

    def find_by_id(self, id: int) -> [Device, None]:
        '''Find a device by id.
        
        params
            id: The id of the device.

        returns
            The device object or None.
        '''
        ...

    def find_by_pn_sn(self, pn: int, sn: int) -> [Device, None]:
        '''Find a device by part number and serial number.
        
        params
            pn: The part number of the device.
            sn: The serial number of the device.

        returns
            The device object or None.
        '''
        ...

    def remove(self, device: Device) -> None:
        '''Remove a device from the SDk.

        This will disconnect the device and remove it from the SDK.
        
        params
            device: The device to remove.
        '''
        ...

    @property 
    def on_new(self) -> Signal:
        '''The on_new signal.

        This signal is emitted when a new device is discovered.
        The callback function should have the signature: 
        callback(device: Device, port: SysPort, meta: ConnectionMeta) -> None
            device: A class representing the discovered device.
            port: The port the device was discovered on.
            meta: The connection details.
        '''
        ...

    @property 
    def list(self) -> list:
        '''The list of devices currently discovered or connected to the SDK.'''
        ...

class SysPortMgr:
    ''' A managment class for system ports. '''

    def create_sol(self, name: str, use_tcp: bool, use_RFC2217: bool, ip_address: str, port: int) -> None:
        '''Create a new Sol port.

        Create a new Serial Over Lan (SOL) port in the SDK to connect to standard SOL hardware.
        If the SOL hardware supports RFC2217 then setting use_RFC2217 to True will allow the SDK
        to automatically adjust the connection settings in the SOL hardware.

        params
            name: The name to assign to the port.
            use_tcp: True if the network connection is TCP, False if UDP.
            use_RFC2217: True to use RFC2217, False to use raw.
            ip_address: The IP address of the SOL hardware.
            port: The port number for UDP/TCP SOL hardware.
        '''
        ...

    def delete_sol(self, port: SolPort) -> None:
        '''Delete a Sol port.

        params
            port: The port to delete.
        '''
        ...

    def find_by_id(self, id: int) -> [SysPort, None]:
        '''Find a port by id.
        
        params
            id: The id of the port.

        returns
            The port object or None.
        '''
        ...

    @property
    def on_new(self) -> Signal:
        '''The on_new signal.
        
        This signal is emitted when a new port is discovered or added to the SDK.
        The callback function should have the signature:
        callback(port: SysPort) -> None
            port: A class representing the discovered port.
        '''
        ...

    @property
    def list(self) -> list:
        '''The list of ports known to the SDK.'''
        ...


#------------------------------------- Port Bindings ---------------------------------------------
class SysPort:
    ''' A class representing a system port. '''

    class ClassType(Enum):
        '''The class types.'''
        Serial : int
        Sol : int
        Net : int
        Pcp : int

    class Type(Enum):
        '''The port types.'''
        Serial : int
        Net : int

    id: int
    '''The id number of the port.'''
    discovery_timeout_ms: int
    '''The discovery timeout in milliseconds.'''
    name: str
    '''The name of the port.'''
    type: Type
    '''The type of the port.'''
    is_open: bool
    '''True if the port is open.'''
    
    @property
    def on_error(self) -> Signal:
        '''The on error signal.

        This signal is emitted when an error occurs.
        The callback function should have the signature:
        callback(port: SysPort, msg: str) -> None
            port: The port object.
            msg: The error message.
        '''
        ...

    @property
    def on_delete(self) -> Signal:
        '''The on delete signal.

        This signal is emitted when the port is deleted from the SDK.
        The callback function should have the signature:
        callback(port: SysPort) -> None
            port: The port object.
        '''
        ...

    @property
    def on_open(self) -> Signal:
        '''The on open signal.

        This signal is emitted when the port is opened.
        The callback function should have the signature:
        callback(port: SysPort, success: bool) -> None
            port: The port object.
            success: True if the port was opened successfully.
        '''
        ...

    @property
    def on_close(self) -> Signal:
        '''The on close signal.

        This signal is emitted when the port is closed.
        The callback function should have the signature:
        callback(port: SysPort) -> None
            port: The port object.
        '''
        ...

    @property
    def on_port_stats(self) -> Signal:
        '''The on port stats signal.

        This signal is emitted when port stats are available.
        The callback function should have the signature:
        callback(port: SysPort, tx_bytes: int, rx_bytes: int, bad_packets: int) -> None
            port: The port object.
            tx_bytes: The number of transmitted bytes.
            rx_bytes: The number of received bytes.
            bad_packets: The number of bad packets.
        '''
        ...

    @property
    def on_discovery_started(self) -> Signal:
        '''The on discovery started signal.

        This signal is emitted when discovery starts.
        The callback function should have the signature:
        callback(port: SysPort, type: AutoDiscovery.Type) -> None
            port: The port object.
            type: The discovery type.
        '''
        ...

    @property
    def on_discovery_event(self) -> Signal:
        '''The on discovery event signal.

        This signal is emitted when a discovery event occurs.
        The callback function should have the signature:
        callback(port: SysPort, meta: ConnectionMeta, type: AutoDiscovery.Type, discovery_count: int) -> None
            port: The port object.
            meta: The connection details.
            type: The discovery type.
            discovery_count: The number of devices discovered.
        '''
        ...

    @property
    def on_discovery_finished(self) -> Signal:
        '''The on discovery finished signal.

        This signal is emitted when discovery finishes.
        The callback function should have the signature:
        callback(port: SysPort, type: AutoDiscovery.Type, discovery_count: int, cancelled: bool) -> None
            port: The port object.
            type: The discovery type.
            discovery_count: The number of devices discovered.
            cancelled: True if the discovery was cancelled.
        '''
        ...

    @property
    def on_rx_data(self) -> Signal:
        '''The on rx data signal.

        This signal is emitted when data is received.
        The callback function should have the signature:
        callback(port: SysPort, data: bytes) -> None
            port: The port object.
            data: The received data.
        '''
        ...

    @property
    def on_tx_data(self) -> Signal:
        '''The on tx data signal.
        
        This signal is emitted when data is transmitted.
        The callback function should have the signature:
        callback(port: SysPort, data: bytes) -> None
            port: The port object.
            data: The transmitted data.
        '''
        ...

    def stop_discovery(self) -> None:
        '''Stop discovery.'''
        ...

    def is_discovering(self) -> bool:
        '''True if the port is discovering.

        returns
            True if the port is discovering.
        '''

    def open(self) -> None:
        '''Open the port.'''
        ...

    def close(self) -> None:
        '''Close the port.'''
        ...

    def write(self, data: bytes, meta: ConnectionMeta) -> bool:
        '''Write data to the port specifying baudrate or ip address and port.

        params
            data: The data to write.
            meta: The connection details.

        returns
            True if the write was successful.
        '''
        ...

    def discover_isl_devices(self, pid: int=0xffff, pn: int=0xffff, sn: int=0xffff) -> None:
        '''Discover Impact Subsea devices.

        params
            pid: The product ID of the device.
            pn: The part number of the device.
            sn: The serial number of the device.
        '''
        ...

    @overload
    def discover_isl_devices(self, pid: int, pn: int, sn: int, meta: ConnectionMeta, timeout_ms: int, count: int) -> None:
        '''Discover Impact Subsea devices.

        params
            pid: The product ID of the device.
            pn: The part number of the device.
            sn: The serial number of the device.
            meta: The connection details.
            timeout_ms: The timeout in milliseconds.
            count: The number of devices to discover.
        '''
        ...

    def discover_nmea_devices(self) -> None:
        '''Discover NMEA devices.'''
        ...

#------------------------------------- Device Bindings ---------------------------------------------
class Device:
    '''The base class of all devices.'''
    id: int
    '''The device ID.'''
    info: Info
    '''The device info.'''
    connection: Connection
    '''The device connection info.'''

    def is_connected(self) -> bool:
        '''True if the device is connected.

        returns
            True if the device is connected.
        '''
        ...

    def connect(self) -> None:
        '''Connect to the device.'''
        ...

    def set_rediscovery_timeouts(self, search_timeout_ms: int, search_count: int) -> None:
        '''Set the rediscovery timeouts.
        
        params
            search_timeout_ms: The timeout in milliseconds to wait for a response.
            search_count: The number of times to search.
        '''
        ...

    def set_comms_retries(self, retries: int) -> None:
        '''Set the comms retries.
        
        params
            retries: The number of transmit retries before giving up and disconnecting.
        '''
        ...

    def reset(self) -> None:
        '''Reset the device.'''
        ...

    def save_config(self, file_name: str) -> None:
        '''Save the device config.
        
        params
            file_name: The file name to save the config to.
        '''
        ...

    def get_config(self) -> str:
        '''Get the xml device config as a string.

        returns
            The xml device config as a string.
        '''
        ...

    def get_hardware_faults(self) -> List[str]:
        '''Get the hardware faults.
        
        returns
            The list of hardware faults.
        '''
        ...

    def bootloader_mode(self) -> bool:
        '''True if the device is in bootloader mode.

        returns
            True if the device is in bootloader mode.
        '''
        ...

    @property
    def on_error(self) -> Signal:
        '''The on error signal.

        This signal is emitted when an error occurs.
        The callback function should have the signature:
        callback(device: Device, msg: str) -> None
            device: The device object.
            msg: The error message.
        '''
        ...

    @property
    def on_delete(self) -> Signal:
        '''The on delete signal.

        This signal is emitted when the device is deleted from the SDK.
        The callback function should have the signature:
        callback(device: Device) -> None
            device: The device object.
        '''
        ...

    @property
    def on_connect(self) -> Signal:
        '''The on connect signal.

        This signal is emitted when the device connects.
        The callback function should have the signature:
        callback(device: Device) -> None
            device: The device object.
        '''
        ...

    @property
    def on_disconnect(self) -> Signal:
        '''The on disconnect signal.

        This signal is emitted when the device disconnects.
        The callback function should have the signature:
        callback(device: Device) -> None
            device: The device object.
        '''
        ...

    @property
    def on_port_added(self) -> Signal:
        '''The on port added signal.

        This signal is emitted when a port is added to the device.
        The callback function should have the signature:
        callback(device: Device, port: SysPort, meta: ConnectionMeta) -> None
            device: The device object.
            port: The port object.
            meta: The connection details.
        '''
        ...

    @property
    def on_port_changed(self) -> Signal:
        '''The on port changed signal.

        This signal is emitted when port connection details change for a device. (baudrate, ip address, etc)
        The callback function should have the signature:
        callback(device: Device, port: SysPort, meta: ConnectionMeta) -> None
            device: The device object.
            port: The port object.
            meta: The changed connection details.
        '''
        ...

    @property
    def on_port_removed(self) -> Signal:
        '''The on port removed signal.

        This signal is emitted when a port is removed from the device.
        The callback function should have the signature:
        callback(device: Device, port: SysPort) -> None
            device: The device object.
            port: The port object.
        '''
        ...

    @property
    def on_info_changed(self) -> Signal:
        '''The on info changed signal.

        This signal is emitted when the device info changes.
        The callback function should have the signature:
        callback(device: Device, info: Device.Info) -> None
            device: The device object.
            info: The new device info.
        '''
        ...

    @property
    def on_packet_count(self) -> Signal:
        '''The on packet count signal.

        This signal is emitted when the device packet count changes.
        The callback function should have the signature:
        callback(device: Device, tx_bytes: int, rx_bytes: int, bad_packets: int, missed: int) -> None
            device: The device object.
            tx_bytes: The number of transmitted bytes.
            rx_bytes: The number of received bytes.
            bad_packets: The number of bad packets.
            missed: The number of missed packets.
        '''

    @property
    def on_comms_timeout(self) -> Signal:
        '''The on comms timeout signal.

        This signal is emitted when a comms timeout occurs.
        The callback function should have the signature:
        callback(device: Device, timeout: bool) -> None
            device: The device object.
            timeout: True if the device will be disconnected.
        '''
        ...

    class Info:
        '''A class representing device information.'''
        pid: int 
        '''The device pid.'''
        pn : int
        '''The device part number.'''
        sn : int
        '''The device serial number.'''
        config : int
        '''The device config value.'''
        mode : int
        '''The device mode.'''
        status : int
        '''The device status.'''
        firmware_build_num : int
        '''The device firmware build number.'''
        firmware_version_bcd : int
        '''The device firmware version in BCD format.'''
        in_use : bool
        '''True if the device is connected to another instance of the SDK.'''
        pn_sn : str
        '''The device part number and serial number as a string.'''
        firmware_version : str
        '''The device firmware version as a string.'''
        name : str
        '''The device name as a string.'''
 

    class CustomStr:
        def __init__(self) -> None: ...
        @overload
        def __init__(self, enable:bool, str:str) -> None: ...
        enable: bool
        '''True if the custom string is enabled.'''
        str: str
        '''The custom string.'''

    class Pid(Enum):
        '''The device PIDs.'''
        Unknown : int
        Isa500v1 : int
        Isd4000v1 : int
        Ism3dv1 : int
        Iss360v1 : int
        Isa500 : int
        Isd4000 : int
        Ism3d : int
        Sonar : int
        MultiPcp : int
        Any : int

    class UartMode(Enum):
        '''The device UART modes.'''
        Rs232 : int
        Rs485 : int
        Rs485Terminated : int
        Unknown : int

    class Parity(Enum):
        '''The device parity settings.'''
        Off : int
        Odd : int
        Even : int
        Mark : int
        Space : int
        Unknown : int

    class StopBits(Enum):
        '''The device stop bits.'''
        One : int
        OneAndHalf : int
        Two : int
        Unknown : int

    class PhyMdixMode(Enum):
        '''The device MDIX modes.'''
        Normal : int
        Swapped : int
        Auto : int
        Unknown : int

    class PhyPortMode(Enum):
        '''The device port modes.'''
        Auto : int
        Base10TxHalf : int
        Base10TxFull : int
        Base100TxHalf : int
        Base100TxFull : int
        Unknown : int

#------------------------------------- AHRS Bindings -----------------------------------------------
class Ahrs:
    '''A class representing an AHRS device.'''

    id: int
    '''The device ID of the AHRS. This is the same as the device ID that owns the AHRS.'''

    def set_heading(self, heading_rad: float) -> None:
        '''Set the heading of the AHRS.
        
        params
            heading_rad: The heading in radians.
        '''
        ...

    def set_heading_to_mag(self) -> None:
        '''Set the heading of the AHRS to the magnetic heading.'''
        ...

    def clear_turns_count(self) -> None:
        '''Clear the turn count of the AHRS.'''
        ...

    @property
    def on_new(self) -> Signal:
        '''The on_data signal.

        This signal is emitted when new data is available.
        The callback function should have the signature:
        callback(ahrs: Ahrs, time_stamp_us: int, quaternion: Quaternion, magnetic_heading: float, turn_count: float) -> None
            ahrs: The AHRS object.
            time_stamp_us: The timestamp in microseconds.
            quaternion: The orientation quaternion.
            magnetic_heading: The raw magnetic heading in radians.
            turn_count: The number of turns.
        '''

class GyroSensor:
    ''' A class representing a gyro sensor device. '''

    id: int
    '''The device ID of the gyro sensor. This is the same as the device ID that owns the gyro sensor.'''
    sensor_number: int
    '''The sensor number of the gyro sensor.'''
    bias: Vector3
    '''The bias values for the gyro sensor.'''

    def update_cal_values(self, bias: Vector3) -> None:
        '''Update the calibration values within this class.
        
        params
            bias: The bias value to assign.
        '''
        ...

    def auto_cal(self) -> None:
        '''Automatically determine and set the calibration values for the gyro sensor.
        The sensor can be in any orientation when this is called, but it must be completely still.'''

    def set_cal(self, bias: Vector3) -> None:
        '''Set the calibration values for the gyro sensor.
        
        params
            bias: The bias value.
        '''
        ...

    @property
    def on_data(self) -> Signal:
        '''The on_data signal.

        This signal is emitted when new data is available.
        The callback function should have the signature:
        callback(gyro: GyroSensor, vector: Vector3) -> None
            gyro: The gyro sensor object.
            vector: The gyro data.
        '''

    @property
    def on_cal_change(self) -> Signal:
        '''The on_cal_change signal.

        This signal is emitted when the calibration values change.
        The callback function should have the signature:
        callback(gyro: GyroSensor, bias: Vector3) -> None
            gyro: The gyro sensor object.
            bias: The new bias values.
        '''

class AccelSensor:
    ''' A class representing an accelerometer sensor device. '''
    
    id: int
    '''The device ID of the accelerometer sensor. This is the same as the device ID that owns the accelerometer sensor.'''
    sensor_number: int
    '''The sensor number of the accelerometer sensor.'''
    bias: Vector3
    '''The bias values for the accelerometer sensor.'''
    transform: Matrix3x3
    '''The transform matrix for the accelerometer sensor.'''

    def update_cal_values(self, bias: Vector3, transform: Matrix3x3) -> None:
        '''Update the calibration values within this class.
        
        params
            bias: The bias values to assign.
            transform: The transform matrix to assign.
        '''
        ...

    def set_cal(self, bias: Vector3, transform: Matrix3x3) -> None:
        '''Set the calibration values for the accelerometer sensor.
        
        params
            bias: The bias values.
            transform: The transform matrix.
        '''
        ...

    def start_cal(self, samples_per_average: int, max_variation_g: float, factory_cal: bool = False) -> None:
        '''Start the calibration process for the accelerometer sensor.
        
        params
            samples_per_average: The number of samples to average per reading.
            max_variation_g: The maximum allowable variation in g between readings that form the average.
            factory_cal: True to run a multipoint factory calibration, False to run 2 point zeroing calibration.
        '''
        ...

    def stop_cal(self, cancel: bool) -> bool:
        '''Stop the calibration process for the accelerometer sensor.
        
        params
            cancel: True to cancel the calibration, False to compute and save the calibration.

        returns
            A tuple (success: bool, bias: Vector3, transform: Matrix3x3) where success is True if the calibration was successful and bias and transform are the corrected values.
        '''
        ...

    @property
    def on_data(self) -> Signal:
        '''The on_data signal.

        This signal is emitted when new data is available.
        The callback function should have the signature:
        callback(accel: AccelSensor, vector: Vector3) -> None
            accel: The accelerometer sensor object.
            vector: The accelerometer data.
        '''

    @property
    def on_cal_change(self) -> Signal:
        '''The on_cal_change signal.

        This signal is emitted when the calibration values change.
        The callback function should have the signature:
        callback(accel: AccelSensor, bias: Vector3, transform: Matrix3x3) -> None
            accel: The accelerometer sensor object.
            bias: The new bias values.
            transform: The new transform matrix.
        '''

    @property
    def on_cal_progress(self) -> Signal:
        '''The on_cal_progress signal.

        This signal is emitted when the calibration progress changes.
        The callback function should have the signature:
        callback(accel: AccelSensor, vector: Vector3, index: int) -> None
            accel: The accelerometer sensor object.
            vector: The reading that has been taken and stored in an array.
            index: The array index where the vector was stored. -1 if the vector is not stored.
        '''

class MagSensor:
    ''' A class representing a magnetometer sensor device. '''
 
    id: int
    '''The device ID of the mag sensor. This is the same as the device ID that owns the mag sensor.'''
    sensor_number: int
    '''The sensor number of the mag sensor.'''
    bias: Vector3
    '''The bias values for the mag sensor.'''
    transform: Matrix3x3
    '''The transform matrix for the mag sensor.'''

    def update_cal_values(self, bias: Vector3, transform: Matrix3x3) -> None:
        '''Update the calibration values within this class.
        
        params
            bias: The bias values to assign.
            transform: The transform matrix to assign.
        '''
        ...

    def set_cal(self, bias: Vector3, transform: Matrix3x3) -> None:
        '''Set the calibration values for the mag sensor.
        
        params
            bias: The bias values.
            transform: The transform matrix.
        '''
        ...

    def start_cal(self, spread_ut: float=10, accel: AccelSensor=None) -> None:
        '''Start the calibration process for the mag sensor.
        
        params
            spread_ut: The spread in uT to use for the calibration.
            accel: The accelerometer sensor object to use for factory calibration. If none then a user cal is performed.
        '''
        ...

    def stop_cal(self, cancel: bool, bias_correction: Optional[Vector3] = None, transform_correction: Optional[Matrix3x3] = None) -> bool:
        '''Stop the calibration process for the mag sensor.
        
        params
            cancel: True to cancel the calibration, False to compute and save the calibration.
            bias_correction: The bias correction values.
            transform_correction: The transform correction matrix.

        returns
            A tuple (success: bool, bias: Vector3, transform: Matrix3x3) where success is True if the calibration was successful and bias and transform are the corrected values.
        '''
        ...

    @property
    def on_data(self) -> Signal:
        '''The on_data signal.

        This signal is emitted when new data is available.
        The callback function should have the signature:
        callback(mag: MagSensor, vector: Vector3) -> None
            mag: The mag sensor object.
            vector: The mag data.
        '''

    @property
    def on_cal_change(self) -> Signal:
        '''The on_cal_change signal.

        This signal is emitted when the calibration values change.
        The callback function should have the signature:
        callback(mag: MagSensor, bias: Vector3, transform: Matrix3x3) -> None
            mag: The mag sensor object.
            bias: The new bias values.
            transform: The new transform matrix.
        '''
        ...

    @property
    def on_cal_progress(self) -> Signal:
        '''The on_cal_progress signal.

        This signal is emitted when the calibration progress changes.
        The callback function should have the signature:
        callback(mag: MagSensor, vector: Vector3, count: uint) -> None
            mag: The mag sensor object.
            vector: The reading that has been taken and stored in an array.
            count: The number of readings taken so far.
        '''
        ...

#------------------------------------- Firmware Bindings -------------------------------------------

class Firmware:
    class CodeBlock:
        '''A class representing a code block.'''
        address: int
        '''The address.'''
        code: bytes
        '''The code.'''

    '''A class representing firmware.'''
    pid: int
    '''The product ID.'''
    version: int
    '''The firmware version in BCD format, eg. 0x1234 = V1.2.3.4.'''
    blocks: List[CodeBlock]
    '''The code blocks.'''
    def reset(self) -> None:
        '''Reset the firmware.'''
        ...
    @property
    def get_size(self) -> int:
        '''Return the size of the firmware.
        
        returns
            The size.
        '''
        ...
    def set_section_alignment(self, alignment_mask: int, pad_value: int) -> None:
        '''Set the section alignment.
        
        params
            alignment_mask: The alignment mask.
            pad_value: The pad value.
        '''
        ...

def fwi_file_open(filename: str) -> Firmware:
    '''Open a fwi file.
    
    params
        filename: The filename of the fwi file.
    
    returns
        The firmware object.
    '''
    ...

class CodeConverter:
    '''A class representing a code converter.'''
    def set_sonar_fw_options(self, includeFsbl: bool, includePl: bool, includeApp: bool) -> None:
        '''Set the Sonar FW options.
        
        params
            includeFsbl: True to include the FSBL.
            includePl: True to include the PL.
            includeApp: True to include the App.
        '''
        ...

    def hex_to_fwi(self, hex_filename: str, fwi_filename: str, pid: int, fw_version: int) -> None:
        '''Convert a hex file to a fwi file.
        
        params
            hex_filename: The hex filename to open.
            fwi_filename: The fwi filename to save.
            pid: The product ID.
            fw_version: The firmware version in BCD format eg 0x1234 = V.1.2.3.4
        '''
        ...

    def fwi_to_bin(self, fwi_filename: str, bin_filename: str, alignment_mask: int = 0x0fff, padding_value: int = 0xff) -> None:
        '''Convert a fwi file to a bin file.
        
        params
            fwi_filename: The fwi filename to open.
            bin_filename: The bin folder name to place the bin files.
            alignment_mask: The alignment mask.
            padding_value: The padding value.
        '''
        ...

#------------------------------------- ISA500 Bindings ---------------------------------------------

class Isa500(Device):
    '''A class representing an ISA500 device.'''
    ahrs: Ahrs
    '''The AHRS sensor.'''
    gyro: GyroSensor
    '''The gyro sensor.'''
    accel: AccelSensor
    '''The accelerometer sensor.'''
    mag: MagSensor
    '''The magnetometer sensor.'''
    def set_sensor_rates(self, rate: SensorRates) -> None:
        '''Set the sensor rates for data output.
        
        params
            rate: The rates.
        '''
        ...
    def set_settings(self, settings: Settings, save: bool) -> None:
        '''Set the settings.
        
        params
            settings: The settings.
            save: True to save the settings.
        '''
        ...

    def ping_now(self) -> None:
        '''Ping now.'''
        ...

    def set_echo_gram(self, data_point_count: int) -> None:
        '''Set the echo gram.
        
        params
            data_point_count: The number of data points per ping.
        '''
        ...

    def set_ping_script(self, name: str, code: str) -> None:
        '''Set the ping script.
        
        params
            name: The name of the script.
            code: The script code.
        '''
        ...

    def set_ahrs_script(self, name: str, code: str) -> None:
        '''Set the AHRS script.
        
        params
            name: The name of the script.
            code: The script code.
        '''
        ...

    def get_scripts(self) -> bool:
        '''Get the scripts.
        If the scripts haven't been retrieved, this function will request them from the device.

        returns
            True if the scripts were retrieved, False if waiting for a response.
        '''
        ...

    def load_config(self, filename: str) -> Tuple[Info, Settings, DeviceScript, DeviceScript, AhrsCal]:
        '''Load the config xml file.
        
        params
            filename: The filename.
        
        returns
            A tuple containing the info, settings, script0, script1, and cal.
        '''
        ...

    def has_ahrs(self) -> bool:
        '''True if the device has the AHRS licence.

        returns
            True if the device has the AHRS licence.
        '''
        ...

    def has_echo_gram(self) -> bool:
        '''True if the device has the echogram licence.

        returns
            True if the device has the echogram licence.
        '''
        ...

    def has_fmd(self) -> bool:
        '''True if the device has the FMD licence.

        returns
            True if the device has the FMD licence.
        '''
        ...

    def has_right_angle_transducer(self) -> bool:
        '''True if the device has a right angle transducer.

        returns
            True if the device has a right angle transducer.
        '''
        ...

    def has_current_loop(self) -> bool:
        '''True if the device has current loop analogue output.

        returns
            True if the device has current loop analogue output.
        '''
        ...

    settings: Settings
    '''The settings.'''
    sensor_rates: SensorRates
    '''The sensor rates.'''
    hard_coded_ping_output_strings: List[str]
    '''The hard coded ping output strings.'''
    hard_coded_ahrs_output_strings: List[str]
    '''The hard coded AHRS output strings.'''
    script_vars: List[str]
    '''The script variables.'''
    on_ping: DeviceScript
    '''The ping script that is run to output a string.'''
    on_ahrs: DeviceScript
    '''The AHRS script that is run to output a string.'''
    
    @property
    def on_echo(self) -> Signal:
        '''The on echo signal.

        This signal is emitted when new echo data is available.
        The callback function should have the signature:
        callback(isa500: Isa500, time_us: int, selected_echo_index: int, total_echo_count: int, echos: List[Echo]) -> None
            isa500: The ISA500 object.
            time_us: The time in microseconds.
            selected_echo_index: The selected echo index.
            total_echo_count: The total echo count.
            echos: The echos.
        '''
        ...

    @property
    def on_echogram_data(self) -> Signal:
        '''The on echogram data signal.

        This signal is emitted when new echogram data is available.
        The callback function should have the signature:
        callback(isa500: Isa500, echogram: List[int]) -> None
            isa500: The ISA500 object.
            echogram: The echogram data.
        '''
        ...

    @property
    def on_temperature(self) -> Signal:
        '''The on temperature signal.

        This signal is emitted when new temperature data is available.
        The callback function should have the signature:
        callback(isa500: Isa500, temperature: float) -> None
            isa500: The ISA500 object.
            temperature: The temperature in degrees celsius.
        '''
        ...

    @property
    def on_voltage(self) -> Signal:
        '''The on voltage signal.

        This signal is emitted when new voltage data is available.
        The callback function should have the signature:
        callback(isa500: Isa500, voltage: float) -> None
            isa500: The ISA500 object.
            voltage: The voltage.
        '''
        ...

    @property
    def on_trigger(self) -> Signal:
        '''The on trigger signal.

        This signal is emitted when a trigger event occurs.
        The callback function should have the signature:
        callback(isa500: Isa500, edge: bool) -> None
            isa500: The ISA500 object.
            edge: True if the trigger edge is rising.
        '''
        ...

    @property
    def on_script_data_received(self) -> Signal:
        '''The on script data received signal.

        This signal is emitted when new script data is available.
        The callback function should have the signature:
        callback(isa500: Isa500) -> None
            isa500: The ISA500 object.
        '''
        ...

    @property
    def on_settings_updated(self, ok: bool) -> Signal:
        '''The on settings updated signal.

        This signal is emitted when the settings have updated.
        The callback function should have the signature:
        callback(isa500: Isa500) -> None
            isa500: The ISA500 object.
            ok: True if the settings were updated successfully.
        '''
        ...

    class AhrsCal:
        '''A class representing AHRS calibration.'''
        gyro_bias: Vector3
        '''The gyro bias.'''
        accel_bias: Vector3
        '''The accel bias.'''
        mag_bias: Vector3
        '''The mag bias.'''
        accel_transform: Matrix3x3
        '''The accel transform.'''
        mag_transform: Matrix3x3
        '''The mag transform.'''

    class SensorRates:
        '''A class representing sensor rates.'''
        ping: int
        '''The ping rate in milliseconds.'''
        ahrs: int
        '''The AHRS rate in milliseconds.'''
        gyro: int
        '''The gyro rate in milliseconds.'''
        accel: int
        '''The accel rate in milliseconds.'''
        mag: int
        '''The mag rate in milliseconds.'''
        temperature: int
        '''The temperature rate in milliseconds.'''
        voltage: int
        '''The voltage rate in milliseconds.'''

    class Echo:
        '''A class representing an echo.'''
        total_tof: float
        '''The total time of flight in seconds to the target and back.'''
        correlation: float
        '''How well the received echo correlates 0 to 1.'''
        signal_energy: float
        '''Normalised energy level of the echo 0 to 1.'''

    class Settings:
        '''A class representing settings.'''
        uart_mode: Device.UartMode
        '''The serial port mode.'''
        baudrate: int
        '''The serial port baudrate.'''
        parity: Device.Parity
        '''The serial parity.'''
        data_bits: int
        '''The serial word length 5 to 8 bits.'''
        stop_bits: Device.StopBits
        '''The serial stop bits.'''
        ahrs_mode: int
        '''If bit zero is 1 use inertial mode. 0 is mag slave mode.'''
        orientation_offset: Quaternion
        '''Heading, pitch and roll offsets (or down and forward vectors) expressed as a quaternion.'''
        heading_offset_rad: float
        '''Offset in radians to add to the heading. Typically use for magnetic declination.'''
        turns_about: Vector3
        '''A vector representing the axis which turn are measured about.'''
        turns_about_earth_frame: bool
        '''If true the "turnsAbout" vector is referenced to the earth frame. False is sensor frame.'''
        clr_turn: str
        '''The turns clearing string.'''
        set_heading2_mag: str
        '''A string to set the heading to magnetometer heading.'''
        multi_echo_limit: int
        '''Sets the maximum multi echo limit, range is 0 to 100.'''
        frequency: int
        '''Frequency of operation in Hertz from 50000 to 700000.'''
        tx_pulse_width_us: int
        '''Length of the transmit pulse in microseconds ranging from 0 to 500.'''
        tx_pulse_amplitude: int
        '''Amplitude of the transmit pulse as a percentage ranging from 0 to 100.'''
        echo_analyse_mode: EchoAnalyseMode
        '''Selects which echo to report back as the chosen one.'''
        xc_threashold_low: float
        '''When the return cross correlated signal level drops below this value the end of an echo pulse is realised. Value ranges from 0 to 1 default is 0.4.'''
        xc_threashold_high: float
        '''When the return cross correlated signal level rises above this value the start of an echo pulse is realised. Value ranges from 0 to 1 default is 0.5.'''
        energy_threashold: float
        '''Minimum enery an echo must have to be reported. Range is 0 to 1.'''
        speed_of_sound: float
        '''Speed of sound in metres per second.'''
        min_range: float
        '''Minimum range in metres. Distance is one way, transducer to target.'''
        max_range: float
        '''Maximum range in metres. Upper limit is 300, distance is one way, transducer to target.'''
        distance_offset: float
        '''Offset + or - in metres to add to the final reading.'''
        use_tilt_correction: bool
        '''If true the echo range to target will be trigonometrically corrected for pitch and roll.'''
        use_max_value_on_no_return: bool
        '''If no echo is detected then use the maximum range value as the reading for outputted strings.'''
        ana_mode: AnalogueOutMode
        '''Mode of the analogue output.'''
        a_out_min_range: float
        '''Value in metres. "aOutMinRange" and "aOutMinVal" define a point. e.g 3 metres = 3 volt.'''
        a_out_max_range: float
        '''Value in meteres. "aOutMaxRange" and "aOutMaxVal" define a point.'''
        a_out_min_val: float
        '''Value in volts or mA depending on the mode. "aOutMinRange" and "aOutMinVal" define a point.'''
        a_out_max_val: float
        '''Value in volts or mA depending on the mode. "aOutMaxRange" and "aOutMaxVal" define a point.'''
        ping_str: StrOutputSetup
        '''Custom interrogation string.'''
        ahrs_str: StrOutputSetup
        '''Custom interrogation string.'''

        def defaults(self) -> None:
            '''Sets the default values.'''
            ...

    class StrOutputSetup:
        '''A class representing string output setup.'''
        str_id: int
        '''The string ID.'''
        interval_enabled: bool
        '''True if the interval is enabled.'''
        interval_ms: int
        '''The interval in milliseconds.'''
        trigger_enabled: bool
        '''True if the trigger is enabled.'''
        trigger_edge: bool
        '''True if the trigger edge is rising.'''
        interrogation: str
        '''The interrogation string.'''
 
    class EchoAnalyseMode(Enum):
        '''The echo analyse modes.'''
        First : int
        Strongest : int
        Tracking : int

    class AnalogueOutMode(Enum):
        '''The analogue out modes.'''
        Voltage : int
        Current : int

#------------------------------------- ISD4000 Bindings -------------------------------------------

class Isd4000(Device):
    '''A class representing an ISD4000 device.'''
    ahrs: Ahrs
    '''The AHRS sensor.'''
    gyro: GyroSensor
    '''The gyro sensor.'''
    accel: AccelSensor
    '''The accelerometer sensor.'''
    mag: MagSensor
    '''The magnetometer sensor.'''
    def set_sensor_rates(self, rate: SensorRates) -> None:
        '''Set the sensor rates for data output.
        
        params
            rate: The rates.
        '''
        ...
    def set_settings(self, settings: Settings, save: bool) -> None:
        '''Set the settings.
        
        params
            settings: The settings.
            save: True to save the settings.
        '''
        ...

    def set_depth_script(self, name: str, code: str) -> None:
        '''Set the depth script.
        
        params
            name: The name of the script.
            code: The script code.
        '''
        ...

    def set_ahrs_script(self, name: str, code: str) -> None:
        '''Set the AHRS script.
        
        params
            name: The name of the script.
            code: The script code.
        '''
        ...

    def get_scripts(self) -> bool:
        '''Get the scripts.
        If the scripts haven't been retrieved, this function will request them from the device.

        returns
            True if the scripts were retrieved, False if waiting for a response.
        '''
        ...

    def set_pressure_cal_cert(self, cert: CalCert) -> None:
        '''Set the pressure calibration certificate.
        
        params
            cert: The certificate.
        '''
        ...

    def set_temperature_cal_cert(self, cert: CalCert) -> None:
        '''Set the temperature calibration certificate.
        
        params
            cert: The certificate.
        '''
        ...

    def get_cal(self, pressure: bool = False, temperature: bool = False) -> bool:
        '''Get the calibration
        This function is used to test if retrieval of the pressure and temperature calibration certificates from the device is nessessary.
        It return's true if the calibrations are valid or false and requests the calibrations from the device.
        Passing true to the pressure and temperature will force the calibrations to be retrieved from the device.

        params
            pressure: True to force retrieval the pressure calibration.
            temperature: True to force retrieval the temperature calibration.

        returns
            True if the calibrations are valid, False if waiting for a response.
        '''
        ...

    def pressure_cal_valid(self) -> bool:
        '''True if the pressure calibration is valid.

        returns
            True if the pressure calibration is valid.
        '''
        ...

    def temperature_cal_valid(self) -> bool:
        '''True if the temperature calibration is valid.

        returns
            True if the temperature calibration is valid.
        '''
        ...

    def measure_now(self) -> None:
        '''Trigger a measurement.'''
        ...

    def load_config(self, filename: str) -> Tuple[Device.Info, Settings, DeviceScript, DeviceScript, AhrsCal, PressureCal, TemperatureCal]:
        '''Load the config xml file.
        
        params
            filename: The filename.
        
        returns
            A tuple containing the info, settings, script0, script1, cal, pCal, and tCal.
        '''
        ...

    def has_ahrs(self) -> bool:
        '''True if the device has the AHRS licence.

        returns
            True if the device has the AHRS licence.
        '''
        ...

    def max_pressure_rating_bar(self) -> float:
        '''The maximum pressure rating in Bar.

        returns
            The maximum pressure rating in Bar.
        '''
        ...

    settings: Settings
    '''The settings.'''
    sensor_rates: SensorRates
    '''The sensor rates.'''
    hard_coded_depth_output_strings: List[str]
    '''The hard coded depth output strings.'''
    hard_coded_ahrs_output_strings: List[str]
    '''The hard coded AHRS output strings.'''
    script_vars: List[str]
    '''The script variables.'''
    on_depth: DeviceScript
    '''The depth script that is run to output a string.'''
    on_ahrs: DeviceScript
    '''The AHRS script that is run to output a string.'''
    pressureCal: PressureCal
    '''The pressure calibration.'''
    temperatureCal: TemperatureCal
    '''The temperature calibration.'''

    @property
    def on_pressure(self) -> Signal:
        '''The on pressure signal.

        This signal is emitted when new pressure data is available.
        The callback function should have the signature:
        callback(isd4000: Isd4000, time_us: int, pressure: float, depth: float, pressure_raw: float) -> None
            isd4000: The ISD4000 object.
            time_us: The time in microseconds.
            pressure: The pressure in Bar.
            depth: The depth in metres.
            pressure_raw: The raw pressure value in Bar.
        '''
        ...

    @property
    def on_temperature(self) -> Signal:
        '''The on temperature signal.

        This signal is emitted when new temperature data is available.
        The callback function should have the signature:
        callback(isd4000: Isd4000, temperature: float, temperature_raw: float) -> None
            isd4000: The ISD4000 object.
            temperature: The temperature in degrees celsius.
            temperature_raw: The raw temperature value.
        '''
        ...

    @property
    def on_script_data_received(self) -> Signal:
        '''The on script data received signal.

        This signal is emitted when new script data is available.
        The callback function should have the signature:
        callback(isd4000: Isd4000) -> None
            isd4000: The ISD4000 object.
        '''
        ...

    @property
    def on_settings_updated(self, ok: bool) -> Signal:
        '''The on settings updated signal.

        This signal is emitted when the settings have updated.
        The callback function should have the signature:
        callback(isd4000: Isd4000, ok: bool) -> None
            isd4000: The ISD4000 object.
            ok: True if the settings were updated successfully.
        '''
        ...

    @property
    def on_pressure_cal_cert(self) -> Signal:
        '''The on pressure cal cert signal.

        This signal is emitted when the pressure calibration certificate is received.
        The callback function should have the signature:
        callback(isd4000: Isd4000, cal: PressureCal) -> None
            isd4000: The ISD4000 object.
            cal: The pressure calibration certificate.
        '''
        ...

    @property
    def on_temperature_cal_cert(self) -> Signal:
        '''The on temperature cal cert signal.

        This signal is emitted when the temperature calibration certificate is received.
        The callback function should have the signature:
        callback(isd4000: Isd4000, cal: TemperatureCal) -> None
            isd4000: The ISD4000 object.
            cal: The temperature calibration certificate.
        '''
        ...
    
    class Settings:
        '''A class representing settings.'''
        uart_mode: Device.UartMode
        '''The serial port mode.'''
        baudrate: int
        '''The serial port baudrate. Limits are standard bauds between 300 and 115200.'''
        parity: Device.Parity
        '''The serial parity.'''
        data_bits: int
        '''The serial word length 5 to 8 bits.'''
        stop_bits: Device.StopBits
        '''The serial stop bits.'''
        ahrs_mode: int
        '''If bit zero is 1 use inertial mode. 0 is mag slave mode.'''
        orientation_offset: Quaternion
        '''Heading, pitch and roll offsets (or down and forward vectors) expressed as a quaternion.'''
        heading_offset_rad: float
        '''Offset in radians to add to the heading. Typically use for magnetic declination.'''
        turns_about: Vector3
        '''A vector representing the axis which turn are measured about.'''
        turns_about_earth_frame: bool
        '''If true the "turnsAbout" vector is referenced to the earth frame. False is sensor frame.'''
        clr_turn: str
        '''The turns clearing string.'''
        set_heading2_mag: str
        '''A string to set the heading to magnetometer heading.'''
        filter_pressure: bool
        '''If true an exponential moving average filter is used to smooth data. This is the filter "output = (lastOutput * 0.9) + (pressure * 0.1)".'''
        depth_offset: float
        '''Offset in Meters to add to the depth.'''
        pressure_offset: float
        '''Offset in Bar to add to the calibrated pressure.'''
        latitude: float
        '''Latitude of the device. Used for gravity accuracy.'''
        tare_str: str
        '''Custom string to tare the pressure.'''
        unTare_str: str
        '''Custom string to remove the tare on the pressure.'''
        depth_str: StrOutputSetup
        '''depth string setup.'''
        ahrs_str: StrOutputSetup
        '''AHRS string setup.'''
        def defaults(self) -> None:
            '''Sets the default values.'''
            ...

    class StrOutputSetup:
        '''A class representing string output setup.'''
        str_id: int
        '''The string ID. 0 = script.'''
        interval_enabled: bool
        '''TIf true then autonomously acquire and output at the defined interval'''
        interval_ms: int
        '''Interval in milliseconds to autonomously output.'''
        interrogation: Device.CustomStr
        '''Custom interrogation string.'''

    class SensorRates:
        '''A class representing sensor rates.'''
        pressure: int
        '''The pressure rate in milliseconds.'''
        ahrs: int
        '''The AHRS rate in milliseconds.'''
        gyro: int
        '''The gyro rate in milliseconds.'''
        accel: int
        '''The accel rate in milliseconds.'''
        mag: int
        '''The mag rate in milliseconds.'''
        temperature: int
        '''The temperature rate in milliseconds.'''
   
    class CalCert:
        '''A class representing a calibration certificate.'''
        year: int
        '''The year.'''
        month: int
        '''The month.'''
        day: int
        '''The day.'''
        cal_points: List[float]
        '''The cal points.'''
        verify_points: List[float]
        '''The verify points.'''
        number: str
        '''The number.'''
        organisation: str
        '''The organisation.'''
        person: str
        '''The person.'''
        equipment: str
        '''The equipment.'''
        equipment_sn: str
        '''The equipment serial number.'''
        notes: str
        '''The notes.'''

    class PressureCal:
        '''A class representing pressure calibration.'''
        state: DataState
        '''The state.'''
        cal: CalCert
        '''The cal.'''

    class TemperatureCal:
        '''A class representing temperature calibration.'''
        state: DataState
        '''The state.'''
        cal: CalCert
        '''The cal.'''
        adc_offset: int
        '''The ADC offset.'''

    class AhrsCal:
        '''A class representing AHRS calibration.'''
        gyro_bias: Vector3
        '''The gyro bias.'''
        accel_bias: Vector3
        '''The accel bias.'''
        mag_bias: Vector3
        '''The mag bias.'''
        accel_transform: Matrix3x3
        '''The accel transform.'''
        mag_transform: Matrix3x3
        '''The mag transform.'''

#------------------------------------- ISM3D Bindings ---------------------------------------------
class Ism3d(Device):
    '''A class representing an ISM3D device.'''
    ahrs: Ahrs
    '''The AHRS sensor.'''
    gyro: GyroSensor
    '''The gyro sensor.'''
    gyro_sec: GyroSensor
    '''The backup gyro sensor.'''
    accel: AccelSensor
    '''The accelerometer sensor.'''
    accel_sec: AccelSensor
    '''The backup accelerometer sensor.'''
    mag: MagSensor
    '''The magnetometer sensor.'''
    sensor_rates: SensorRates
    '''The sensor rates.'''
    hard_coded_ahrs_output_strings: List[str]
    '''The hard coded AHRS output strings.'''
    script_vars: List[str]
    '''The script variables.'''
    on_ahrs: DeviceScript
    '''The AHRS data signal.'''

    def set_sensor_rates(self, rate: SensorRates) -> None:
        '''Set the sensor rates for data output.
        
        params
            rate: The rates.
        '''
        ...

    def set_settings(self, settings: Settings, save: bool) -> None:
        '''Set the settings.
        Device.onError event will be called if the settings are invalid.
        The EEPROM in this device has an endurance of 100000 write cycles. Writing to the EEPROM too often will
        reduce the life of the device. Consider setting save to false if updating the settings frequently.

        params
            settings: The settings.
            save: True to save the settings.
        '''
        ...

    def set_ahrs_script(self, name: str, code: str) -> None:
        '''Set the AHRS script.
        
        params
            name: The name of the script.
            code: The script code.
        '''
        ...

    def get_scripts(self) -> bool:
        '''Get the scripts.
        If the scripts haven't been retrieved, this function will request them from the device.

        returns
            True if the scripts were retrieved, False if waiting for a response.
        '''
        ...

    def save_config(self, filename: str) -> None:
        '''Save the configuration.

        params
            filename: The filename.
        '''
        ...

    def load_config(self, filename: str) -> Tuple[Device.Info, Settings, DeviceScript, AhrsCal]:
        '''Load the config xml file.

        params
            filename: The filename.

        returns
            A tuple containing the info, settings, script, and cal.
        '''
        ...

    @property
    def on_script_data_received(self) -> Signal:
        '''The on script data received signal.

        This signal is emitted when new script data is available.
        The callback function should have the signature:
        callback(ism3d: Ism3d) -> None
            ism3d: The ISM3D object.
        '''
        ...

    @property
    def on_settings_updated(self, ok: bool) -> Signal:
        '''The on settings updated signal.

        This signal is emitted when the settings have updated.
        The callback function should have the signature:
        callback(ism3d: Ism3d, ok: bool) -> None
            ism3d: The ISM3D object.
            ok: True if the settings were updated successfully.
        '''
        ...

    class Settings:
        '''A class representing settings.'''
        uart_mode: Device.UartMode
        '''The serial port mode.'''
        baudrate: int
        '''The serial port baudrate.'''
        parity: Device.Parity
        '''The serial parity.'''
        data_bits: int
        '''The serial word length 5 to 8 bits.'''
        stop_bits: Device.StopBits
        '''The serial stop bits.'''
        ahrs_mode: int
        '''If bit zero is 1 use inertial mode. 0 is mag slave mode.'''
        orientation_offset: Quaternion
        '''Heading, pitch and roll offsets (or down and forward vectors) expressed as a quaternion.'''
        heading_offset_rad: float
        '''Offset in radians to add to the heading. Typically use for magnetic declination.'''
        turns_about: Vector3
        '''A vector representing the axis which turn are measured about.'''
        turns_about_earth_frame: bool
        '''If true the "turnsAbout" vector is referenced to the earth frame. False is sensor frame.'''
        clr_turn: str
        '''The turns clearing string.'''
        set_heading2_mag: str
        '''A string to set the heading to magnetometer heading.'''
        ahrs_str: StrOutputSetup
        '''Custom interrogation string.'''
        def defaults(self) -> None:
            '''Sets the default values.'''
            ...

    class StrOutputSetup:
        '''A class representing string output setup.'''
        str_id: int
        '''The string ID.'''
        interval_enabled: bool
        '''True if the interval is enabled.'''
        interval_ms: int
        '''The interval in milliseconds.'''
        interrogation: str
        '''The interrogation string.'''

    class SensorRates:
        '''A class representing sensor rates.'''
        ahrs: int
        '''The AHRS rate in milliseconds.'''
        gyro: int
        '''The gyro rate in milliseconds.'''
        accel: int
        '''The accel rate in milliseconds.'''
        mag: int
        '''The mag rate in milliseconds.'''

    class AhrsCal:
        '''A class representing AHRS calibration.'''
        gyro_bias: Vector3
        '''The gyro bias.'''
        accel_bias: Vector3
        '''The accel bias.'''
        mag_bias: Vector3
        '''The mag bias.'''
        accel_transform: Matrix3x3
        '''The accel transform.'''
        mag_transform: Matrix3x3
        '''The mag transform.'''
        gyro_bias_sec: Vector3
        '''The backup gyro bias.'''
        accel_bias_sec: Vector3
        '''The backup accel bias.'''
        accel_transform_sec: Matrix3x3
        '''The backup accel transform.'''

#------------------------------------- Logging Bindings --------------------------------------------

class Logfile:
    class RecordHeader:
        class Type(Enum):
            '''The log types.'''
            Meta: int
            Data: int
            Index: int
            Track: int

        time_ms: int
        '''The time in milliseconds.'''
        track_id: int
        '''The track ID.'''
        can_skip: bool
        '''True if the data can be skipped on playback.'''
        record_type: Type
        '''The record type.'''
        data_size: int
        '''The data size in bytes.'''
        data_type: int
        '''A value that represents the type and structure of the data.'''

    class Track:
        id: int
        '''The track ID.'''
        file_offset: int
        '''The file offset.'''
        start_index: int
        '''The start index.'''
        record_count: int
        '''The record count in this track.'''
        start_time: int
        '''The start time.'''
        duration_ms: int
        '''The duration in milliseconds.'''
        data_type: int
        '''A value that represents the type and structure of the data.'''
        data: bytes
        '''The data.'''

class LoggingDevice:
    '''A class representing a logging device.'''
    def set_logger(self, logger: LogWriter, track_data: bytes) -> None:
        '''Set the logger.

        params
            logger: The logger used to log
            track_data: Optional track data.
        '''
        ...

    def log(self, data: bytes, data_type: int, can_skip: bool = True) -> None:
        '''Log data.

        params
            data: The data to log
            data_type: A value that represents the type and structure of the data being logged.
            can_skip: True if the data can be skipped on play back.
        '''
        ...

    def start_logging(self) -> None:
        '''Start logging.'''
        ...

    def stop_logging(self) -> None:
        '''Stop logging.'''
        ...

    def is_logging(self) -> bool:
        '''True if logging.'''
        ...
  
class LogWriter:
    '''A class representing a log writer.'''
    def start_new_file(self, file_name: str) -> None:
        '''Start a new file.

        params
            file_name: The file name.
        '''
        ...

    def add_track(self, data_type: int, data: bytes) -> int:
        '''Add a track to the log file.

        params
            data_type: The data type.
            data: The data.

        returns
            The track ID.
        '''
        ...

    def add_track_data(self, track_id: int, data: bytes, data_type: int, can_skip: bool = True) -> None:
        '''Add track data.

        params
            track_id: The track ID.
            data: Any data applicable to the track like device type, serial number, etc.
            data_type: A value that represents the type and structure of the data.
            can_skip: True if the data can be skipped on play back.
        '''
        ...

    def close(self) -> None:
        '''Close the file.'''
        ...

    def set_max_file_size(self, max_size: int) -> None:
        '''Set the max file size.
        When the file size reaches the max size the on_max_file_size signal will be emitted.

        params
            max_size: The max file size.
        '''
        ...

    record_count: int
    '''The record count.'''
    time_ms: int
    '''The time in milliseconds.'''
    duration_ms: int
    '''The duration in milliseconds.'''

    @property
    def on_max_file_size(self) -> Signal:
        '''The on max file size signal.

        This signal is emitted when the max file size is reached.
        The callback function should have the signature:
        callback(log_writer: LogWriter) -> None
            log_writer: The log writer.
        '''
        ...

class LogReader(LogWriter):
    '''A class representing a log reader.'''
    def open(self, file_name: str) -> None:
        '''Open the log file.

        params
            file_name: The file name.
        '''
        ...

    def play(self, play_speed: float) -> None:
        '''Play the log file.

        params
            play_speed: The play speed + is forward - is backwards. 1.0 is normal speed.
        '''
        ...

    def reset(self) -> None:
        '''Reset the playback of the log file.'''
        ...

    def seek(self, index: int) -> None:
        '''Seek to a record.

        params
            index: The index of the record.
        '''
        ...

    def process(self) -> None:
        '''Process the log file.
        This function needs to be called periodically to process the log file. It will emit the on_record signal when a record is ready.
        So must be called at a sufficient rate.
        '''
        ...

    @property
    def on_record(self) -> Signal:
        '''The on record signal.

        This signal is emitted when a record is ready.
        The callback function should have the signature:
        callback(log_reader: LogReader, record: LogReader.RecordData) -> None
            log_reader: The log reader.
            record: The record data.
        '''
        ...

    @property
    def on_error(self) -> Signal:
        '''The on error signal.

        This signal is emitted when an error occurs.
        The callback function should have the signature:
        callback(log_reader: LogReader, error: str) -> None
            log_reader: The log reader.
            error: The error message.
        '''
        ...

    class RecordData:
        '''A class representing record data.'''
        track_id: int
        '''The track ID.'''
        time_ms: int
        '''The time in milliseconds.'''
        record_index: int
        '''The record index.'''
        record_type: Logfile.RecordHeader.Type
        '''The record type.'''
        data_type: int
        '''The data type.'''
        data: bytes
        '''The data.'''

class LogPlayer(LogReader):
    '''A class representing a log player.'''
    def get_device_from_track(self, track: LogFile.Track) -> Device:
        '''Get a device from a track.

        params
            track: The track.

        returns
            The device.
        '''
        ...

    @property
    def on_new_track(self) -> Signal:
        '''The on new track signal.

        This signal is emitted when a new track is available.
        The callback function should have the signature:
        callback(log_player: LogPlayer, track: LogFile.Track) -> None
            log_player: The log player.
            track: The track.
        '''
        ...

class ProtocolDebugger:
    '''A class representing a protocol debugger.'''
    def __init__(self, name: str) -> None:
        '''Constructor.

        params
            name: The name.
        '''
        ...
        
    def monitor_port(self, port: SysPort) -> None:
        '''Monitor a port.

        params
            port: The port.
        '''
        ...

    show_payload: bool
    '''True to show the payload.'''

#------------------------------------- Sonar Bindings ----------------------------------------------

class Buf2D:
    '''A class representing a 2D buffer.
    This class supports the buffer protocol and __array_interface__.'''
    def __init__(self, width: int, height: int) -> None:
        '''Constructor.

        params
            width: The width.
            height: The height.
        '''
        ...
    def to_bytes(self) -> bytes:
        '''Return the buffer data as a bytes object.'''
        ...

class Palette:
    '''A class representing a palette.'''
    def set_to_default(self) -> None:
        '''Set the palette to the default.'''
        ...

    def set(self, gradient: List[Tuple[int, int]], null_colour: int) -> None:
        '''Set the palette.

        params
            gradient: A list of tuples containg a colour value and position ranging from 0 to 65535.
            null_colour: The null colour value.
        '''
        ...

    def render(self, width: int, height: int, horizontal: bool = True) -> Buf2D:
        '''Render the palette.

        params
            width: The width.
            height: The height.
            horizontal: True if horizontal.

        returns
            The buffer.
        '''
        ...

    def save_bmp(self, file_name: str, width: int, height: int, horizontal: bool = True) -> None:
        '''Save the image to a BMP file.

        params
            file_name: The file name.
            width: The width.
            height: The height.
            horizontal: True if horizontal, False if vertical.
        '''
        ...

class SonarImage:
    '''A class representing a sonar image.
    This class supports the buffer protocol and __array_interface__.'''
    def __init__(self, width: int, height: int, use_4_bpp: bool = True, use_biliner_interpolation: bool = True) -> None:
        '''Constructor.

        params
            width: The width.
            height: The height.
            use_4_bpp: True to use 4 bytes per pixel.
            use_biliner_interpolation: True to use bilinear interpolation.
        '''
        ...
    def to_bytes(self) -> bytes:
        '''Return the image as a bytes object.'''
        ...
    def set_buffer(self, width: int, height: int, use_4_bpp: bool) -> None:
        '''Set the buffer dimensions.

        params
            width: The width.
            height: The height.
            use_4_bpp: True to use 4 bytes per pixel.
        '''
        ...
    def set_sector_area(self, min_range_mm: int, max_range_mm: int, sector_start: int, sector_size: int) -> None:
        '''Set the sector area which the buffer represents.

        params
            min_range_mm: The minimum range in mm.
            max_range_mm: The maximum range in mm.
            sector_start: The sector start angle in units of 12800th of a circle.
            sector_size: The sector size in units of 12800th of a circle.
        '''
        ...
    def render(self, data: SonarDataStore, palette: Palette, redraw: bool = False) -> None:
        '''Render a circular image from data in the SonarDataStore using the passed palette.

        params
            data: A SonarDataStore object.
            palette: The palette.
            redraw: True to re-render all the data in the SonarDataStore object, False to only render new data.
        '''
        ...
    def render_16_bit(self, data: SonarDataStore, redraw: bool = False) -> None:
        '''Render a circular image from the SonarDataStore object as a 16 bit image.

        params
            data: A SonarDataStore object.
            redraw: True to re-render all the data in the SonarDataStore object, False to only render new data.
        '''
        ...
    def render_texture(self, data: SonarDataStore, palette: Palette, redraw: bool = False) -> None:
        '''Render a rectangular image from the SonarDataStore object using the passed palette.

        params
            data: A SonarDataStore object.
            palette: The palette.
            redraw: True to re-render all the data in the SonarDataStore object, False to only render new data.
        '''
        ...
    def render_texture_16_bit(self, data: SonarDataStore, redraw: bool = False) -> None:
        '''Render a rectangular image from the SonarDataStore object as a 16 bit image.

        params
            data: A SonarDataStore object.
            redraw: True to re-render all the data in the SonarDataStore object, False to only render new data.
        '''
        ...
    def save_bmp(self, file_name: str) -> None:
        '''Save the current rendered image to a bitmap file.

        params
            file_name: The file name.
        '''
        ...

        width: int
        '''The width.'''
        height: int
        '''The height.'''
        bpp: int
        '''The bytes per pixel.'''
        use_biliner_interpolation: bool
        '''True to use bilinear interpolation.'''

class SonarDataStore:
    '''A class to store sonar data.'''
    def add(self, ping: Ping, blank_range_mm: int = 0) -> None:
        '''Add ping data.

        params
            ping: The ping data.
            blank_range_mm: The blank range in mm. Data closer than this range will be zeroed.
        '''
        ...
    def clear(self, start_angle: int = 0, angle_size: int = Sonar.max_angle) -> None:
        '''Clear ping data from a sector.

        params
            start_angle: The start angle in units of 12800th of a circle.
            angle_size: The angle size in units of 12800th of a circle.
        '''
        ...

class Sonar:
    '''A class representing a sonar.'''
    max_angle: int
    '''The maximum angle.'''
    settings: Settings
    '''The settings.'''
    sensor_rates: SensorRates
    '''The sensor rates.'''
    tvg_points: List[Points]
    '''The TVG points.'''
    mac_address: str
    '''The MAC address.'''
    ahrs: Ahrs
    '''The AHRS sensor.'''
    gyro: GyroSensor
    '''The gyro sensor.'''
    accel: AccelSensor
    '''The accelerometer sensor.'''
    mag: MagSensor
    '''The magnetometer sensor.'''

    @property
    def on_settings_updated(self) -> Signal:
        '''The on settings updated signal.

        This signal is emitted when the settings have updated.
        The callback function should have the signature:
        callback(sonar: Sonar, settingType: Settings.Type) -> None
            sonar: The Sonar object.
            settingType: The type of settings.
        '''
        ...
    @property
    def on_head_indexes_acquired(self) -> Signal:
        '''The on head indexes acquired signal.

        This signal is emitted when the head indexes have been acquired.
        The callback function should have the signature:
        callback(sonar: Sonar, headIndexes: HeadIndexes) -> None
            sonar: The Sonar object.
            headIndexes: The head indexes.
        '''
        ...
    @property
    def on_ping_data(self) -> Signal:
        '''The on ping data signal.

        This signal is emitted when new ping data is available.
        The callback function should have the signature:
        callback(sonar: Sonar, ping: Ping) -> None
            sonar: The Sonar object.
            ping: The ping data.
        '''
        ...
    @property
    def on_echo_data(self) -> Signal:
        '''The on echo data signal.

        This signal is emitted when new echo data is available.
        The callback function should have the signature:
        callback(sonar: Sonar, echo: Echo) -> None
            sonar: The Sonar object.
            echo: The echo data.
        '''
        ...
    @property
    def on_pwr_and_temp(self) -> Signal:
        '''The on power and temperature signal.

        This signal is emitted when new power and temperature data is available.
        The callback function should have the signature:
        callback(sonar: Sonar, status: CpuPowerTemp) -> None
            sonar: The Sonar object.
            status: The data.
        '''
        ...
    @property
    def on_motor_slip(self) -> Signal:
        '''The on motor slip signal.

        This signal is emitted when the motor slips.
        The callback function should have the signature:
        callback(sonar: Sonar, slip: int) -> None
            sonar: The Sonar object.
            slip: The slip value.
        '''
        ...
    @property
    def on_motor_move_complete(self) -> Signal:
        '''The on motor move complete signal.

        This signal is emitted when the motor move is complete.
        The callback function should have the signature:
        callback(sonar: Sonar, complete: bool) -> None
            sonar: The Sonar object.
            complete: True if the move is complete.
        '''
        ...

    def set_sensor_rates(self, sensors: SensorRates) -> None:
        '''Set the sensor rates.

        params
            sensors: The sensor rates.
        '''
        ...
    def set_system_settings(self, settings: SystemSettings, save: bool = False) -> None:
        '''Set the system settings.
        Device.onError event will be called if the settings are invalid.
        Writing to the flash too often will reduce the life of the device. Consider setting save to false if updating the settings frequently.

        params
            settings: The settings.
            save: True to save the settings.
        '''
        ...
    def set_acoustic_settings(self, settings: AcousticSettings, save: bool = False) -> None:
        '''Set the acoustic settings.
        Device.onError event will be called if the settings are invalid.
        Writing to the flash too often will reduce the life of the device. Consider setting save to false if updating the settings frequently.

        params
            settings: The settings.
            save: True to save the settings.
        '''
        ...
    def set_setup_settings(self, settings: SetupSettings, save: bool = False) -> None:
        '''Set the setup settings.
        Device.onError event will be called if the settings are invalid.
        Writing to the flash too often will reduce the life of the device. Consider setting save to false if updating the settings frequently.

        params
            settings: The settings.
            save: True to save the settings.
        '''
        ...
    def check_head_idx(self) -> None:
        '''Reacquires the transducer position and reports any errors.'''
        ...
    def start_scanning(self) -> None:
        '''Start scanning.'''
        ...
    def stop_scanning(self) -> None:
        '''Stop scanning.'''
        ...
    def move_head(self, angle: int, relative: bool = False) -> None:
        '''Move the head.

        params
            angle: The angle in units of 12800th of a circle.
            relative: True if the angle is relative.
        '''
        ...
    def test_pattern(self, enable: bool) -> None:
        '''Test pattern.

        params
            enable: True to enable the test pattern.
        '''
        ...
    def set_tvg(self, points: List[Points]) -> None:
        '''Set the time variable gain curve.

        params
            points: The points.
        '''
        ...
    def get_default_tvg(self) -> List[Points]:
        '''Get the default time variable gain curve.

        returns
            The points.
        '''
        ...
 
    def load_config(self, file_name: str) -> Tuple[Device.Info, Settings, AhrsCal, List[Points]]:
        '''Load the configuration.

        params
            file_name: The file name.

        returns
            A tuple containing the info, settings, cal, and tvg points.
        '''
        ...
    def has_ahrs(self) -> bool:
        '''True if the sonar has AHRS.'''
        ...
    def is_hd(self) -> bool:
        '''True if the sonar is HD.'''
        ...
    def is_profiler(self) -> bool:
        '''True if the sonar is a profiler.'''
        ...

    class Sector:
        '''A class representing a sector.'''
        start: int
        '''The start angle of the sector in units of 12800th of a circle.'''
        size: int
        '''The size of the sector in units of 12800th of a circle.'''

    class Settings:
        '''A class representing settings.'''
        system: System
        '''The system settings.'''
        acoustic: Acoustic
        '''The acoustic settings.'''
        setup: Setup
        '''The setup settings.'''
        def defaults(self) -> None:
            '''Set the default values.'''
            ...
        class Type(Enum):
            '''The settings types.'''
            System: int
            Acoustic: int
            Setup: int

    class System:
        '''A class representing system settings.'''
        uart_mode: Device.UartMode
        '''The serial port mode.'''
        baudrate: int
        '''The serial port baudrate.'''
        ip_address: str
        '''The IP address.'''
        netmask: str
        '''The netmask.'''
        gateway: str
        '''The gateway.'''
        port: int
        '''The port.'''
        phy_port_mode: Device.PhyPortMode
        '''The ethernet connection speed and duplex mode.'''
        phy_mdix_mode: Device.PhyMdixMode
        '''The ethernet TX/RX swapping mode.'''
        use_dhcp: bool
        '''True if the device will request an IP address from the DHCP server.'''
        invert_head_direction: bool
        '''True if the head direction is swapped.'''
        ahrs_mode: int
        '''If bit zero is 1 use inertial mode. 0 is mag slave mode.'''
        orientation_offset: Quaternion
        '''Heading, pitch and roll offsets (or down and forward vectors) expressed as a quaternion.'''
        heading_offset_rad: float
        '''Offset in radians to add to the heading. Typically use for magnetic declination.'''
        turns_about: Vector3
        '''A vector representing the axis which turn are measured about.'''
        turns_about_earth_frame: bool
        '''If true the "turnsAbout" vector is referenced to the earth frame. False is sensor frame.'''
        use_xc_norm: bool
        '''Output normalised cross correlation data instead of unnormalised. Normalised data represents the quality of the echo rather than the strength of the echo.'''
        echo_mode: EchoMode
        '''Applies to profiling mode only. Selects which echo to report back as the chosen one when profiling.'''
        xc_threashold_low: float
        '''Applies to profiling mode only. Sets a lower limit on the quality of the return pulse. This ensures resilience to false echos. Value ranges from 0 to 1.'''
        xc_threashold_high: float
        '''Applies to profiling mode only. When the return signal level drops bellow this value the end of an echo pulse is realised. Value ranges from 0 to 1.'''
        energy_threashold: float
        '''Applies to profiling mode only. Minimum enery an echo must have to be reported. Range is 0 to 1.'''
        use_tilt_correction: bool
        '''Applies to profiling mode only. Not implemented yet.'''
        profiler_depth_gating: bool
        '''Applies to profiling mode only. Not implemented yet.'''
        profiler_min_range_mm: int
        '''Applies to profiling mode only. Start listening for echos after this range in millimeters.'''
        profiler_max_range_mm: int
        '''Applies to profiling mode only. Listen for echos up until this range in millimeters.'''
        def defaults(self) -> None:
            '''Set the default values.'''
            ...
        
        class EchoMode(Enum):
            '''The echo modes.'''
            First: int
            Strongest: int
            All: int

    class Acoustic:
        '''A class representing acoustic settings.'''
        tx_start_frequency: int
        '''Transmit pulse start frequency in hertz.'''
        tx_end_frequency: int
        '''Transmit pulse end frequency in hertz.'''
        tx_pulse_width_us: int
        '''Transmit pulse length in micro seconds.'''
        tx_pulse_amplitude: int
        '''Transmit pulse amplitude as a percent 0% to 100%.'''
        high_sample_rate: bool
        '''If true the ADC sample rate is 5 MHz else it's 2.5 MHz.'''
        psk_mode: PskMode
        '''PSK modulation mode.'''
        def defaults(self) -> None:
            '''Set the default values.'''
            ...

        class PskMode(Enum):
            '''The PSK modes.'''
            Off: int
            Code1: int
            Code2: int
            Code3: int
            Code4: int

    class Setup:
        '''A class representing setup settings.'''
        digital_gain: float
        '''Digital gain for the image data as a simple multiplier factor. limits 1 to 1000'''
        speed_of_sound: float
        '''Speed of sound in meters per second. limits 1000 to 2500'''
        max_range_mm: int
        '''Listen for echos up until this range in millimeters'''
        min_range_mm: int
        '''Start listening for echos after this range in millimeters'''
        step_size: int
        '''Angle the tranducer head should move between pings in units of 12800th. Positive values turn clockwise, negative anticlockwise. limits -6399 to 6399'''
        sector_start: int
        '''Start angle of the sector. limmts 0 to 12799'''
        sector_size: int
        '''Size of the sector. limits 0 to 12800'''
        flyback_mode: bool
        '''If true the transducer head returns back to either the sectorStart position when stepSize is positive, or sectorStart + sectorSize when stepSize is negative'''
        image_data_point: int
        '''Number of data points per ping between the range set by minRangeMm and maxRangeMm. limits 20 to 4096'''
        data_8_bit: bool
        '''true = 8-bit data, false = 16-bit data'''
        def defaults(self) -> None:
            '''Set the default values.'''
            ...

    class SensorRates:
        '''A class representing sensor rates.'''
        ahrs: int
        '''The AHRS rate in milliseconds.'''
        gyro: int
        '''The gyro rate in milliseconds.'''
        accel: int
        '''The accel rate in milliseconds.'''
        mag: int
        '''The mag rate in milliseconds.'''
        voltage_and_temp: int
        '''The voltage and temperature rate in milliseconds.'''

    class AhrsCal:
        '''A class representing AHRS calibration.'''
        gyro_bias: Vector3
        '''The gyro bias.'''
        accel_bias: Vector3
        '''The accel bias.'''
        mag_bias: Vector3
        '''The mag bias.'''
        accel_transform: Matrix3x3
        '''The accel transform.'''
        mag_transform: Matrix3x3
        '''The mag transform.'''

    class HeadIndexes:
        '''A class representing head indexes.'''
        state: State
        '''The state of the homing process.'''
        slippage: int
        '''The amount of slippage since the last acquisition or bootup in units of 12800th. 360 degrees = a value of 12800.'''
        hysteresis_correction: int
        '''The amount of hysteresis correction applied to the indexes in units of 12800th'''
        width_correction: int
        '''The amount of width correction applied to the indexes in units of 12800th'''
        edge1_idx: int
        '''Index of the first edge.'''
        edge1_level: int
        '''Level of the first edge.'''
        edge2_idx: int
        '''Index of the second edge.'''
        edge2_level: int
        '''Level of the second edge.'''

        class State(Enum):
            '''The states.'''
            Ok: int
            Error_E1_E2: int
            Error_E2: int
            Error_E1: int
            Error: int

    class Ping:
        '''A class representing a ping.'''
        angle: int
        '''Angle the data was aquired at in units of 12800th. 360 degrees = a value of 12800'''
        step_size: int
        '''The step size setting at the time this data was aquired'''
        min_range_mm: int
        '''Start distance of the data in millimeters, the frist data value is aquired at this range'''
        max_range_mm: int
        '''Final distance of the data in millimeters, the last data value is aquired at this range'''

    class Echo:
        '''A class representing an echo.'''
        total_tof: float
        '''Total time of flight in seconds to the target and back'''
        correlation: float
        '''How well the received echo correlates 0 to 1'''
        signal_energy: float
        '''Normalised energy level of the echo 0 to 1'''

    class Echos:
        '''A class representing echos.'''
        time_us: int
        '''Time in microseconds of the start of the ping'''
        angle: int
        '''Angle the data was aquired at in units of 12800th. 360 degrees = a value of 12800'''
        min_range_mm: int
        '''Start distance of the data in millimeters, data[0] is aquired at this range'''
        max_range_mm: int
        '''Final distance of the data in millimeters, data[dataCount-1] is aquired at this range'''
        data: List[Echo]
        '''Array of echos. Each echo represents a single target'''

    class CpuPowerTemp:
        '''A class representing CPU power and temperature.'''
        core1_v0: float
        '''CPU Core voltage, should be 1V'''
        aux1_v8: float
        '''Auxillary voltage, should be 1.8V'''
        ddr1_v35: float
        '''DDR voltage, should be 1.35V'''
        cpu_temperature: float
        '''CPU temperature in degrees C'''
        aux_temperature: float
        '''Auxillary temperature in degrees C'''

  

#------------------------------------- MultiPcp Bindings -------------------------------------------

class MultiPcp:
    '''A class representing a MultiPCP.'''
    def set_settings(self, settings: Settings, save: bool = False) -> None:
        '''Set the settings.

        params
            settings: The settings.
            save: True to save the settings.
        '''
        ...

    @property
    def on_settings_updated(self) -> Signal:
        '''The on settings updated signal.

        This signal is emitted when the settings are updated.
        The callback function should have the signature:
        callback(multiPcp: MultiPcp, success: bool) -> None
            multiPcp: The MultiPcp object.
            success: True if successful.
        '''
        ...

    setting: Settings
    '''The settings.'''
    pcp_devices: List[PcpDevice]
    '''The PCP devices.'''

    class Settings:
        '''A class representing settings.'''
        ip_address: str
        '''The IP address.'''
        netmask: str
        '''The netmask.'''
        gateway: str
        '''The gateway.'''
        port: int
        '''The port.'''
        use_dhcp: bool
        '''True if DHCP is used.'''
        phy_port_mode: Device.PhyPortMode
        '''The ethernet connection speed and duplex mode.'''
        phy_mdix_mode: Device.PhyMdixMode
        '''The ethernet TX/RX swapping mode.'''
        def defaults(self) -> None:
            '''Set the default values.'''
            ...

#------------------------------------- pcpDevice Bindings -------------------------------------------

class PcpServices:
    '''A class representing PCP services.'''
    def open(self) -> bool:
        '''Open the port.

        returns
            True if successful.
        '''
        ...

    def close(self) -> None:
        '''Close the port.'''
        ...

    def write(self, data: bytes, size: int) -> None:
        '''Write data to the port.

        params
            data: The data.
            size: The size.
        '''
        ...

    def set_serial(self, baudrate: int) -> None:
        '''Set the serial port baudrate.

        params
            baudrate: The baudrate.
        '''
        ...

    def set_serial(self, baudrate: int, data_bits: int, parity: Device.Parity, stop_bits: Device.StopBits) -> None:
        '''Set the serial port settings.

        params
            baudrate: The baudrate.
            data_bits: The data bits.
            parity: The parity.
            stop_bits: The stop bits.
        '''
        ...

    def set_power(self, on: bool) -> None:
        '''Set the power.

        params
            on: True to power on.
        '''
        ...

    def set_mode(self, mode: PortProtocol) -> None:
        '''Set the port protocol mode.

        params
            mode: The mode.
        '''
        ...

    class PortProtocol(Enum):
        '''The port protocols.'''
        Rs232: int
        Rs485: int
        Rs485Terminated: int
        Unknown: int

class PcpDevice(PcpServices):
    '''A class representing an PCP device.'''
    def set_settings(self, settings: Settings, save: bool = False) -> None:
        '''Set the settings.

        params
            settings: The settings.
            save: True to save the settings.
        '''
        ...

    @property
    def on_power_stats(self) -> Signal:
        '''The on power stats signal.

        This signal is emitted when the power stats are updated.
        The callback function should have the signature:
        callback(pcpDevice: PcpDevice, volatge: real_t, current: real_t) -> None
            pcpDevice: The pcpDevice object.
            volatge: The volatge.
            current: The current.
        '''
        ...

    @property
    def on_settings_updated(self) -> Signal:
        '''The on settings updated signal.

        This signal is emitted when the settings are updated.
        The callback function should have the signature:
        callback(pcpDevice: PcpDevice, success: bool) -> None
            pcpDevice: The pcpDevice object.
            success: True if successful.
        '''
        ...

    pcp: PoweredComPort
    '''The port.'''
    settings: Settings
    '''The settings.'''
    id: int
    '''The id.'''

    class Settings:
        '''A class representing settings.'''
        power_on: bool
        '''True to power on.'''
        enabled: bool
        '''True to enable.'''
        port_protocol: PcpServices.PortProtocol
        '''The port protocol.'''
        baudrate: int
        '''The baudrate.'''
        data_bits: int
        '''The data bits.'''
        parity: Device.Parity
        '''The parity.'''
        stop_bits: Device.StopBits
        '''The stop bits.'''
        def defaults(self) -> None:
            '''Set the default values.'''
            ...

class Isa500TestJig:
    '''A class representing an ISA500 test jig.'''
    def read_analogue(self, mode: AnalogueMode) -> None:
        '''Start the analogue readings.

        params
            mode: current or voltage.
        '''
        ...

    def set_trigger_level(self, level: bool_t) -> None:
        '''Set the trigger level.

        params
            level: The level.
        '''
        ...

    @property
    def on_analogue(self) -> Signal:
        '''The on analogue signal.

        This signal is emitted when the analogue value is read.
        The callback function should have the signature:
        callback(isa500TestJig: Isa500TestJig, value: real_t, mode: AnalogueMode) -> None
            isa500TestJig: The Isa500TestJig object.
            value: The value.
            mode: The mode.
        '''
        ...

    class AnalogueMode(Enum):
        '''The analogue modes.'''
        Off: int
        Voltage: int
        Current: int

class SonarTestJig(PcpDevice):
    '''A class representing a sonar test jig.'''
    def connect_to_flash(self) -> None:
        '''Connect to the flash.'''
        ...

    def disconnect_from_flash(self) -> None:
        '''Disconnect from the flash.'''
        ...

    def erase_flash(self, address: int = 0, size: int = 1024*1024*16) -> None:
        '''Erase the flash.

        params
            address: The address.
            size: The size.
        '''
        ...

    def program_flash(self, firmware: Firmware) -> None:
        '''Program the flash.

        params
            firmware: The firmware.
        '''
        ...

    @property
    def on_flash(self) -> Signal:
        '''The on flash signal.

        This signal is emitted when the flash status changes.
        The callback function should have the signature:
        callback(sonarTestJig: SonarTestJig, status: FlashStatus) -> None
            sonarTestJig: The SonarTestJig object.
            status: The status.
        '''
        ...

    bytes_written: int
    '''The number of bytes written to the flash.'''

    class FlashStatus(Enum):
        '''The flash status.'''
        Error: int
        Connected: int
        Disconnected: int
        Erasing: int
        Erased: int
        Written: int
        WriteComplete: int