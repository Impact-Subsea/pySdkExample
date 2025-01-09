import pyIslSdk
import time
import console

from logPlayback import LogPlayback 
from portManager import PortManager
from devices.deviceManager import DeviceManager
from devices.isa500Manager import Isa500Manager
from devices.isd4000Manager import Isd4000Manager
from devices.ism3dManager import Ism3dManager
from devices.sonarManager import SonarManager

logger = pyIslSdk.LogWriter()
sdk = pyIslSdk.Sdk()

def on_new_port(port):
    print(f'New port found {port}')
    PortManager(port)

def on_new_device(device, port, meta):
    print(f'New {device} found on port {port} {meta}')
    mgr = None
    if isinstance(device, pyIslSdk.Isa500):
        mgr = Isa500Manager(device)
    elif isinstance(device, pyIslSdk.Isd4000):
        mgr = Isd4000Manager(device)
    elif isinstance(device, pyIslSdk.Ism3d):
        mgr = Ism3dManager(device)
    elif isinstance(device, pyIslSdk.Sonar):
        mgr = SonarManager(device)
    elif isinstance(device, pyIslSdk.MultiPcp):
        mgr = MultiPcpManager(device, sdk)
    else:
        mgr = DeviceManager(device)

    mgr.set_logger(logger) 
    device.connect()

print('Impact Subsea Test App SDK version', sdk.version)
print(f'{console.TermColor.YELLOW}press "x" to exit and "d" to discover{console.TermColor.ENDC}')
sdk.ports.on_new.connect(on_new_port)
sdk.devices.on_new.connect(on_new_device)
kb = console.KBHit()

#logger.start_new_file("/pylog.islog")

log_player = LogPlayback()
#log_player.open("/pylog.islog")
log_player.play(1)

#pyIslSdk.ports.create_sol("sol1", False, True, "192.168.1.70", 1000)

try:
    while True:
        time.sleep(0.02)
        sdk.run()

        log_player.player.process()

        for manager in DeviceManager.managers.values():
            manager.process_tasks()

        if kb.kbhit():
            key = kb.getch()
            if key == 'x':
                break
            elif key == 'd':
                for port_mgr in PortManager.managers.values():
                    port = port_mgr.port
                    port.stop_discovery()
                    if port.type == pyIslSdk.SysPort.Type.Net and port.name == 'NETWORK':
                        port.discover_isl_devices(0xFFFF, 0xFFFF, 0xFFFF, '192.168.1.236', 33005, 1000)
                    elif port.type == pyIslSdk.SysPort.Type.Serial:
                        port.discover_isl_devices()
            else:  
                for device_mgr in DeviceManager.managers.values():
                    device_mgr.process_command(key)

except KeyboardInterrupt:
    pass

kb.set_normal_term()
