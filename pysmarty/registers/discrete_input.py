"""Discrete Input."""

from .baseregister import BaseRegister


class DiscreteInput(BaseRegister):
    """Smarty Input Register."""

    def __init__(self, **kwargs):
        super().__init__(register_type='discrete_input', **kwargs)

    def update_state(self):
        """Read Register."""
        res = self._connection.client.read_discrete_inputs(
            self.addr, unit=self._connection.slave)
        if not res.isError():
            self.state = res.bits[0]

