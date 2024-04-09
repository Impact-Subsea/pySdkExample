
class App:
    def __init__(self):
        self.device = None
        self.logger = None

    def set_device(self, device):
        if self.device is not None:
            self.unsubscribe()
        self.device = device
        if self.logger is not None:
            self.set_logger(self.logger)
        self.subscribe()
        self.device.connect()

    def subscribe(self):
        self.device.on_error.connect(self.on_error)
        self.device.on_delete.connect(self.on_delete)
        self.device.on_connect.connect(self.on_connect)
        self.device.on_disconnect.connect(self.on_disconnect)
        self.device.on_port_added.connect(self.on_port_added)
        self.device.on_port_changed.connect(self.on_port_changed)
        self.device.on_port_removed.connect(self.on_port_removed)
        self.device.on_info_changed.connect(self.on_info_changed)
        #self.device.on_packet_count.connect(self.on_packet_count)

    def unsubscribe(self):
        self.device.on_error.disconnect(self.on_error)
        self.device.on_delete.disconnect(self.on_delete)
        self.device.on_connect.disconnect(self.on_connect)
        self.device.on_disconnect.disconnect(self.on_disconnect)
        self.device.on_port_added.disconnect(self.on_port_added)
        self.device.on_port_changed.disconnect(self.on_port_changed)
        self.device.on_port_removed.disconnect(self.on_port_removed)
        self.device.on_info_changed.disconnect(self.on_info_changed)
        self.device.on_packet_count.disconnect(self.on_packet_count) 

    def do_task(self, key):
        pass
    
    def set_logger(self, logger):
        pass
    
    def on_error(self, device, error):
        print("ERROR", device, error)

    def on_delete(self, device):
        self.unsubscribe()
        print(device, "about to be deleted from SDK")

    def on_connect(self, device):
        self.connectionEvent()
        print(device, "connected")

    def on_disconnect(self, device):
        print(device, "disconnected")

    def on_port_added(self, device, port, meta):
        print(device, "port added", port, meta)

    def on_port_changed(self, device, port, meta):
        print(device, "port changed", port, meta)

    def on_port_removed(self, device, port):
        print(device, "port removed", port)

    def on_info_changed(self, device, info):
        print(device, "info changed", info)

    def on_packet_count(self, device, tx_packets, rx_packets, resends, missed):
        print(device, "packet count", tx_packets, rx_packets, resends, missed)

    def connectionEvent(self):
        pass