"""Modbus Client."""

from pymodbus.client.sync import ModbusTcpClient


class Connection:
    """Modbus Client."""

    def __init__(self, host, port, slave=1, loop=None):
        """Modbus Connection init."""

        # pylint: disable=unsubscriptable-object
        self._client = ModbusTcpClient(host=host, port=port)
        self._slave = slave

    @property
    def client(self):
        """Get Modbus Client."""
        return self._client

    @property
    def host(self):
        """Get Host."""
        return self._client.host

    @property
    def port(self):
        """Get Port."""
        return self._client.port

    @property
    def slave(self):
        """Get Slave."""
        return self._slave

    def is_connected(self):
        """Return connection state."""
        return self._client.connect()
