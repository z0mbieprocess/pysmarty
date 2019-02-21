"""Python Smarty."""

from .registers import Registers
from .connection import Connection


class Smarty:
    """Smarty Class."""

    def __init__(self, host, port=502, slave=1, loop=None):
        self.connection = Connection(host, port, slave, loop)
        self._registers = Registers(self.connection)

    @property
    def fan_speed(self) -> int:
        """Get Current Fan Speed."""
        register = self._registers.get_register(
            'HR_USER_CONFIG_CURRENT_SYSTEM_MODE')
        return register.state

    @property
    def fan_speed_name(self) -> str:
        """Get Current Fan Speed Name."""
        register = self._registers.get_register(
            'HR_USER_CONFIG_CURRENT_SYSTEM_MODE')
        return register.state_name

    @property
    def system_state(self) -> str:
        """Get Current System State."""
        register = self._registers.get_register(
            'IR_CURRENT_SYSTEM_STATE')
        return register.state_name

    @property
    def filter_timer(self) -> int:
        """Get Filter Timer Days Left."""
        register = self._registers.get_register(
            'IR_FILTERS_TIMER_DAYS_LEFT')
        return register.state

    @property
    def supply_fan_speed(self) -> int:
        """Get Supply Fan Speed (RPM)."""
        register = self._registers.get_register(
            'IR_SUPPLY_FAN_SPEED_RPM')
        return register.value

    @property
    def extract_fan_speed(self) -> int:
        """Get Extract Fan Speed (RPM)."""
        register = self._registers.get_register(
            'IR_EXTRACT_FAN_SPEED_RPM')
        return register.value

    @property
    def supply_air_temperature(self) -> int:
        """Get Supply Air Temperature."""
        register = self._registers.get_register(
            'IR_SUPPLY_AIR_TEMPERATURE')
        return register.value

    @property
    def extract_air_temperature(self) -> int:
        """Get Extract Air Temperature."""
        register = self._registers.get_register(
            'IR_EXTRACT_AIR_TEMPERATURE')
        return register.value

    @property
    def outdoor_air_temperature(self) -> int:
        """Get Outdoor Air Temperature."""
        register = self._registers.get_register(
            'IR_OUTDOOR_AIR_TEMPERATURE')
        return register.value

    @property
    def alarm(self) -> bool:
        """Get Alarm."""
        register = self._registers.get_register(
            'HR_ALARM_A')
        return bool(register.state)

    @property
    def warning(self) -> bool:
        """Get Warning."""
        register = self._registers.get_register(
            'HR_ALARM_B')
        return bool(register.state)

    def get_software_version(self) -> str:
        """Software version."""
        register = self._registers.get_register(
            'IR_SOFTWARE_VERSION')
        return register.state

    def get_configuration_version(self) -> str:
        """Configuration version."""
        register = self._registers.get_register(
            'IR_CONFIGURATION_VERSION')
        return register.state

    async def update(self) -> bool:
        """Update registers."""
        if self.connection.is_connected():
            await self._registers.update()
            return True
        return False

    async def set_fan_speed(self, speed) -> bool:
        """Set Current Fan Speed."""
        if self.connection.is_connected():
            register = self._registers.get_register(
                'HR_USER_CONFIG_CURRENT_SYSTEM_MODE')
            await register.set_state(speed)
            return True
        return False

    async def boost(self) -> bool:
        """Set Intensive Air Flow (limited)."""
        if self.connection.is_connected():
            register = self._registers.get_register(
                'COIL_INTENSIVE_AIR_FLOW_BOOST')
            await register.set_state(1)
            return True
        return False

    async def reset_filters_timer(self) -> bool:
        """Reset Filter Timer."""
        if self.connection.is_connected():
            register = self._registers.get_register(
                'COIL_FILTER_TIMER_RESET')
            await register.set_state(1)
            return True
        return False
