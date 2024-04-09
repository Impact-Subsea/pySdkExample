import pyIslSdk
import time
import console

from portCtrl import PortCtrl
from logPlayback import LogPlayback 
from app import App
from isa500App import Isa500App
from isd4000App import Isd4000App
from ism3dApp import Ism3dApp
from sonarApp import SonarApp

port_list = []
app_list = []
log_player_list = []
logger = pyIslSdk.LogWriter()
        
def on_new_port(port):
    print("Found new", port, port.type)
    port_list.append(PortCtrl(port))

def on_new_device(device, port, meta):
    app = None
    if type(device) is pyIslSdk.Isa500:
        app = Isa500App()
    elif type(device) is pyIslSdk.Isd4000:
        app = Isd4000App()
    elif type(device) is pyIslSdk.Ism3d:
        app = Ism3dApp()
    elif type(device) is pyIslSdk.Sonar:
        app = SonarApp()             #
    else:
        app = App()

    if app is not None:
        app.set_logger(logger) 
        app.set_device(device)
        app_list.append(app)
        
    print(device, type(device), "discovered on port", port, meta)


sdk = pyIslSdk.Sdk()
print("Impact Subsea Python SDK version", sdk.version)
print("press 'x' to exit")
sdk.ports.on_new.connect(on_new_port)
sdk.devices.on_new.connect(on_new_device)

log_player = LogPlayback()
#log_player.open("log.islog")
log_player_list.append(log_player)
log_player.play(1)

#pyIslSdk.ports.create_sol("sol1", False, True, "192.168.1.70", 1000)
#logger.start_new_file("log.islog")

kb = console.KBHit()

try:
    while True:
        time.sleep(0.02)
        sdk.run()

        for log_player in log_player_list:
            log_player.player.process()
        
        if kb.kbhit():
            key = kb.getch()
            if key == 'x':
                break
            else:
                for app in app_list:
                    app.do_task(key)
except KeyboardInterrupt:
    pass

kb.set_normal_term()