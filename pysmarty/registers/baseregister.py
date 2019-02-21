"""Base Register."""


class BaseRegister:
    """Smarty Register."""

    def __init__(self, connection, **kwargs):
        self._connection = connection
        self._register_id = kwargs.get('ID')
        self._name = kwargs.get('NAME')
        self._states = kwargs.get('STATES')
        self._register_type = kwargs.get('register_type')
        self.state = None
        self.addr = kwargs.get('ADDR')

    @property
    def name(self) -> str:
        """Get the name of the register."""
        return self._name

    @property
    def register_type(self) -> str:
        """Get the register type."""
        return self._register_type

    def get_id(self) -> str:
        """Get the ID of the register."""
        return self._register_id
