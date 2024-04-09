import pyIslSdk

class PortCtrl:
    def __init__(self, port):
        self.port = port
        self.port.on_error.connect(self.on_error)
        self.port.on_delete.connect(self.on_delete)
        self.port.on_open.connect(self.on_open)
        self.port.on_close.connect(self.on_close)
        #self.port.on_port_stats.connect(self.on_stats)
        self.port.on_discovery_started.connect(self.on_discovery_started)
        self.port.on_discovery_event.connect(self.on_discovery_events)
        self.port.on_discovery_finished.connect(self.on_discovery_finished)
        #self.port.on_rx_data.connect(self.on_rx_data)
        #self.port.on_tx_data.connect(self.on_tx_data)
        if port.type == pyIslSdk.SysPort.Type.Net and port.name == "NETWORK":
            print("Discovering isl devices on", port, port.type) 
            port.discover_isl_devices(0xffff, 0xffff, 0xffff, "192.168.1.255", 33005, 1000)
        elif port.type == pyIslSdk.SysPort.Type.Sol:
            port.discover_isl_devices()
        elif port.type == pyIslSdk.SysPort.Type.Serial:
            port.discover_isl_devices()

    def unsubscribe(self):
        self.port.on_error.disconnect(self.on_error)
        self.port.on_delete.disconnect(self.on_delete)
        self.port.on_open.disconnect(self.on_open)
        self.port.on_close.disconnect(self.on_close)
        self.port.on_port_stats.disconnect(self.on_stats)
        self.port.on_discovery_started.disconnect(self.on_discovery_started)
        self.port.on_discovery_event.disconnect(self.on_discovery_events)
        self.port.on_discovery_finished.disconnect(self.on_discovery_finished)
        self.port.on_rx_data.disconnect(self.on_rx_data)
        self.port.on_tx_data.disconnect(self.on_tx_data)

    def on_error(self, port, error):
        print(port, error)

    def on_delete(self, port):
        self.unsubscribe()
        print(port, "about to be deleted from SDK")

    def on_open(self, port, failed):
        print(port, "open", not failed)

    def on_close(self, port):
        print(port, "closed")

    def on_stats(self, port, tx_bytes, rx_bytes, bad_packets):
        print(port, "tx bytes:", tx_bytes, "rx bytes:", rx_bytes, "bad packets:", bad_packets)

    def on_discovery_started(self, port, type):
        print(port, "discovery started", type)

    def on_discovery_events(self, port, meta, type, device_count):
        print(port, "discovery events", meta, type, device_count)

    def on_discovery_finished(self, port, type, device_count, cancelled):
        print(port, "discovery finished", type, device_count)

    def on_rx_data(self, port, data):
        print(port, "rx data", data.size)
        #print(data.to_bytes())
       
    def on_tx_data(self, port, data):
        print(port, "tx data", data.size)
        #print(data.to_bytes())