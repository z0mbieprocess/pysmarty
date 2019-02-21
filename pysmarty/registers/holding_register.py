"""Holding Register."""

from .baseregister import BaseRegister
from ..exceptions import PysmartyException


class HoldingRegister(BaseRegister):
    """Smarty Holding Register."""

    def __init__(self, **kwargs):
        super().__init__(register_type='holding_register', **kwargs)

    @property
    def state_name(self):
        """Register State Name."""
        return [k for k, v in self._states.items() if v == self.state][0]

    async def update_state(self):
        """Read Register."""
        res = await self._connection.client.read_holding_registers(
            self.addr, unit=self._connection.slave)
        if not res.isError():
            self.state = res.registers[0]

    async def set_state(self, state):
        """Write Register."""
        if isinstance(state, int):
            if state not in self._states.values():
                raise PysmartyException('Invalid state.', state)
            value = state
        else:
            value = self._states[state]
        try:
            res = await self._connection.client.write_register(
                self.addr, value, unit=self._connection.slave)
            if not res.isError():
                self.state = value
        except KeyError as ex:
            raise PysmartyException('Invalid state.', ex.args)
        except Exception as ex:
            raise PysmartyException('Something went wrong.', ex.args)
