"""Modbus Client."""

from pymodbus.exceptions import ConnectionException
from pymodbus.client.asynchronous import schedulers
from pymodbus.client.asynchronous.tcp import AsyncModbusTCPClient
from pymodbus.client.asynchronous.asyncio import ModbusClientProtocol


class Connection:
    """Modbus Client."""

    def __init__(self, host, port, slave=1, loop=None):
        """Modbus Connection init."""

        # pylint: disable=unsubscriptable-object
        self._client = AsyncModbusTCPClient(host=host, port=port,
                                            loop=loop, timeout=20,
                                            scheduler=schedulers.ASYNC_IO)[1]
        self._slave = slave

    @property
    def client(self) -> ModbusClientProtocol:
        """Get Modbus Client."""
        return self._client.protocol

    @property
    def host(self) -> str:
        """Get Host."""
        return self._client.host

    @property
    def port(self) -> int:
        """Get Port."""
        return self._client.port

    @property
    def slave(self) -> int:
        """Get Slave."""
        return self._slave

    def is_connected(self) -> bool:
        """Return connection state."""
        return bool(self._client.protocol)
