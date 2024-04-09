import pyIslSdk
import datetime
from isa500App import Isa500App
from isd4000App import Isd4000App
from ism3dApp import Ism3dApp
from sonarApp import SonarApp

class LogPlayback:
    def __init__(self):
        self.player = pyIslSdk.LogPlayer()
        self.player.on_error.connect(self.on_error)
        self.player.on_new_track.connect(self.on_new_track)
        self.player.on_record.connect(self.on_record)
        self.app_list = []

    def open(self, filename):
        if not self.player.open(filename):
            print("Log file", filename, "failed to open")

    def close(self):
        self.player.close()
    
    def play(self, speed):
        self.player.play(speed)
            
    def on_error(self, logger, error):
         print("ERROR", logger, error)

    def on_new_track(self, logger, track):
        device = logger.get_device_from_track(track)
        print("New track with device", device, "Start time:", datetime.datetime.fromtimestamp((logger.time_ms + track.start_time) / 1000.0), "duration:", track.duration_ms / 1000.0, "record count", track.record_count)
        app = None
        if type(device) is pyIslSdk.Isa500:
            app = Isa500App()
        elif type(device) is pyIslSdk.Isd4000:
            app = Isd4000App()
        elif type(device) is pyIslSdk.Ism3d:
            app = Ism3dApp()
        elif type(device) is pyIslSdk.Sonar:
            app = SonarApp()

        if app is not None:
            print(device, "data source is the log file.", device, "is being associated with an app for playback")
            app.set_device(device)
            self.app_list.append(app)

    def on_record(self, logger, data):
        pass
        #print("record", data.track_id, data.time_ms, data.record_index, data.record_type, data.data_type, data.data)
