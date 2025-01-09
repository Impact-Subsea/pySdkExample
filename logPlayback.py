import pyIslSdk as sdk
import datetime
from devices.isa500Manager import Isa500Manager
from devices.isd4000Manager import Isd4000Manager
from devices.ism3dManager import Ism3dManager
from devices.sonarManager import SonarManager

class LogPlayback:
    def __init__(self):
        self.player = sdk.LogPlayer()
        self.player.on_error.connect(self.on_error)
        self.player.on_new_track.connect(self.on_new_track)
        self.player.on_record.connect(self.on_record)
        self.app_list = []

    def open(self, filename: str):
        if not self.player.open(filename):
            print("Log file", filename, "failed to open")

    def close(self):
        self.player.close()
    
    def play(self, speed: float):
        self.player.play(speed)
            
    def on_error(self, logger: sdk.LogPlayer, error: str):
         print("ERROR", logger, error)

    def on_new_track(self, logger: sdk.LogPlayer, track: sdk.LogFile.Track):
        device = logger.get_device_from_track(track)
        print("New track with device", device, "Start time:", datetime.datetime.fromtimestamp((logger.time_ms + track.start_time) / 1000.0), "duration:", track.duration_ms / 1000.0, "record count", track.record_count)
        app = None
        if type(device) is sdk.Isa500:
            app = Isa500Manager(device)
        elif type(device) is sdk.Isd4000:
            app = Isd4000Manager(device)
        elif type(device) is sdk.Ism3d:
            app = Ism3dManager(device)
        elif type(device) is sdk.Sonar:
            app = SonarManager(device)

        if app is not None:
            print(device, "data source is the log file.", device, "is being associated with a manager for playback")
            self.app_list.append(app)

    def on_record(self, logger: sdk.LogPlayer, data: sdk.LogPlayer.RecordData):
        #print("record", data.track_id, data.time_ms, data.record_index, data.record_type, data.data_type, data.data)
        pass
