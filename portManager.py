import pyIslSdk as sdk

class PortManager:
    managers = {}
    id_counter = 1
    
    def __init__(self, port) -> None:
        self.port = port
        self.id = PortManager.id_counter
        PortManager.id_counter += 1
        self.port.on_error.connect(self.__on_error)
        self.port.on_delete.connect(self.__on_delete)
        self.port.on_open.connect(self.__on_open)
        self.port.on_close.connect(self.__on_close)
        #self.port.on_port_stats.connect(self.__on_stats)
        self.port.on_discovery_started.connect(self.__on_discovery_started)
        self.port.on_discovery_event.connect(self.__on_discovery_events)
        self.port.on_discovery_finished.connect(self.__on_discovery_finished)
        #self.port.on_rx_data.connect(self.__on_rx_data)
        #self.port.on_tx_data.connect(self.__on_tx_data)
        PortManager.managers[self.id] = self

    def _unsubscribe(self) -> None:
        self.port.on_error.disconnect(self.__on_error)
        self.port.on_delete.disconnect(self.__on_delete)
        self.port.on_open.disconnect(self.__on_open)
        self.port.on_close.disconnect(self.__on_close)
        self.port.on_port_stats.disconnect(self.__on_stats)
        self.port.on_discovery_started.disconnect(self.__on_discovery_started)
        self.port.on_discovery_event.disconnect(self.__on_discovery_events)
        self.port.on_discovery_finished.disconnect(self.__on_discovery_finished)
        self.port.on_rx_data.disconnect(self.__on_rx_data)
        self.port.on_tx_data.disconnect(self.__on_tx_data)

    def __on_error(self, port: sdk.SysPort, msg: str) -> None:
        print(port, 'ERROR', msg)

    def __on_delete(self, port: sdk.SysPort) -> None:
        self._unsubscribe()
        PortManager.managers.pop(self.id)
        print(port, 'about to be deleted from SDK')

    def __on_open(self, port: sdk.SysPort, is_open: bool) -> None:
        print(port, "Open" if is_open else "Open Failed")

    def __on_close(self, port: sdk.SysPort) -> None:
        print(port, 'Closed')

    def __on_stats(self, port: sdk.SysPort, tx_bytes: int, rx_bytes: int, bad_rx_packets: int) -> None:
        print(port, 'stats', tx_bytes, rx_bytes, bad_rx_packets)

    def __on_discovery_started(self, port: sdk.SysPort, type: sdk.AutoDiscovery.Type) -> None:
        print(port, 'discovery started', type)

    def __on_discovery_events(self,  port: sdk.SysPort, meta: sdk.ConnectionMeta, type: sdk.AutoDiscovery.Type, discovery_count: int) -> None:
        print(port, 'discovery event', meta, type, discovery_count)

    def __on_discovery_finished(self, port: sdk.SysPort, type: sdk.AutoDiscovery.Type, discovery_count: int, cancelled: bool) -> None:
        print(port, 'discovery finished', type, 'found', discovery_count, 'devices')

    def __on_rx_data(self, port: sdk.SysPort, data: sdk.ConstArray) -> None:
        print(port, 'rx data', data.size)
        #print(data.to_bytes())
       
    def __on_tx_data(self, port: sdk.SysPort, data: sdk.ConstArray) -> None:
        print(port, 'tx data', data.size)
        #print(data.to_bytes())

    def autoDiscover(self) -> None:
        self.port.stop_discovery()
        if isinstance(self.port, sdk.NetPort) and self.port.name == 'NETWORK':
            print('Discovering ISL devices on network')
            self.port.discover_isl_devices(0xFFFF, 0xFFFF, 0xFFFF, '192.168.1.236', 33005, 1000)
        else:
            self.port.discover_isl_devices()

    def process_command(self, cmd: str) -> None:
        if cmd == 'd':
            self.autoDiscover()
        elif cmd == 'a':
            if type(self.port) == sdk.PoweredComPort:
                self.autoDiscover()

