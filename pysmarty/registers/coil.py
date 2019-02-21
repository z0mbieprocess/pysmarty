"""Coil."""

from .baseregister import BaseRegister
from ..exceptions import PysmartyException


class Coil(BaseRegister):
    """Smart Coil Register."""

    def __init__(self, **kwargs):
        super().__init__(register_type='coil', **kwargs)

    async def update_state(self):
        """Read Register."""
        res = await self._connection.client.read_coils(
            self.addr, unit=self._connection.slave)
        if not res.isError():
            self.state = res.bits[0]

    async def set_state(self, state):
        """Write Register."""
        res = await self._connection.client.write_coil(
            self.addr, state, unit=self._connection.slave)
        if not res.isError():
            self.state = state
