import pyIslSdk as sdk

class DeviceManager:
    managers = {}
    id_counter = 1

    def __init__(self, device: sdk.Device) -> None:
        self.device = device
        self.id = DeviceManager.id_counter
        self.logger = None
        DeviceManager.id_counter += 1
        DeviceManager.managers[self.id] = self
        self._subscribe()

    def _subscribe(self) -> None:
        self.device.on_error.connect(self.__on_error)
        self.device.on_delete.connect(self.__on_delete)
        self.device.on_connect.connect(self.__on_connect)
        self.device.on_disconnect.connect(self.__on_disconnect)
        self.device.on_port_added.connect(self.__on_port_added)
        self.device.on_port_changed.connect(self.__on_port_changed)
        self.device.on_port_removed.connect(self.__on_port_removed)
        self.device.on_info_changed.connect(self.__on_info_changed)
        #self.device.on_packet_count.connect(self.__on_packet_count)
        self.device.on_xml_config.connect(self.__on_xml_config)
        self.device.on_comms_timeout.connect(self.__on_comms_timeout)

    def _unsubscribe(self) -> None:
        self.device.on_error.disconnect(self.__on_error)
        self.device.on_delete.disconnect(self.__on_delete)
        self.device.on_connect.disconnect(self.__on_connect)
        self.device.on_disconnect.disconnect(self.__on_disconnect)
        self.device.on_port_added.disconnect(self.__on_port_added)
        self.device.on_port_changed.disconnect(self.__on_port_changed)
        self.device.on_port_removed.disconnect(self.__on_port_removed)
        self.device.on_info_changed.disconnect(self.__on_info_changed)
        self.device.on_packet_count.disconnect(self.__on_packet_count)
        self.device.on_xml_config.disconnect(self.__on_xml_config)
        self.device.on_comms_timeout.disconnect(self.__on_comms_timeout)

    def process_tasks(self) -> None:
        pass

    def process_command(self, cmd: str) -> None:
        pass

    def set_logger(self, logger):
        pass
    
    def __on_error(self, device: sdk.Device, error: str) -> None:
        print('ERROR', device, error)

    def __on_delete(self, device: sdk.Device) -> None:
        self._unsubscribe()
        DeviceManager.managers.pop(self.id)
        print(device, 'about to be deleted from SDK')

    def __on_connect(self, device: sdk.Device) -> None:
        self._connection_event()
        print(device, 'connected')

    def __on_disconnect(self, device: sdk.Device) -> None:
        print(device, 'disconnected')

    def __on_port_added(self, device: sdk.Device, port: sdk.SysPort, meta: sdk.ConnectionMeta) -> None:
        print(device, 'port added', port, meta)

    def __on_port_changed(self, device: sdk.Device, port: sdk.SysPort, meta: sdk.ConnectionMeta) -> None:
        print(device, 'port changed', port, meta)

    def __on_port_removed(self, device: sdk.Device, port: sdk.SysPort) -> None:
        print(device, 'port removed', port)

    def __on_info_changed(self, device: sdk.Device, info: sdk.Device.Info) -> None:
        print(device, 'info changed', info)

    def __on_packet_count(self, device: sdk.Device, tx_packets: int, rx_packets: int, resends: int, missed: int) -> None:
        print(device, 'packet count', tx_packets, rx_packets, resends, missed)

    def __on_xml_config(self, device: sdk.Device, xml: str) -> None:
        print(device, 'xml config', xml)
        
    def __on_comms_timeout(self, device: sdk.Device, is_disconnecting: bool) -> None:
        print(device, 'comms timeout', is_disconnecting)

    def _connection_event(self) -> None:
        self.start_logging()

    def start_logging(self) -> None:
        if self.logger is not None:
            if self.device.start_logging():
                print("Logging started for", self.device)
            else:
                print("Logging failed to start for", self.device)