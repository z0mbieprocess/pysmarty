"""Input Register."""

from .baseregister import BaseRegister


class InputRegister(BaseRegister):
    """Smarty Input Register."""

    def __init__(self, **kwargs):
        super().__init__(register_type='input_register', **kwargs)
        self.multiplier = kwargs.get('MULTIPLIER')
        self.unit_of_mesurement = kwargs.get('UNIT_OF_MESUREMENT')

    @property
    def value(self):
        """Register State With Multiplier."""
        return round(self.state * self.multiplier, 2) if self.state else self.state

    @property
    def state_name(self):
        """Register State Name."""
        return self._states.get(str(self.state))

    def update_state(self):
        """Read Register."""
        res = self._connection.client.read_input_registers(
            self.addr, unit=self._connection.slave)
        if not res.isError():
            self.state = res.registers[0]
