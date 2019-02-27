"""Smarty Modbus Registers."""

import json
from os import path

from .holding_register import HoldingRegister
from .coil import Coil
from .discrete_input import DiscreteInput
from .input_register import InputRegister

THIS_DIR = path.abspath(path.dirname(__file__))

# read/write registers
with open(path.join(THIS_DIR, "holding_registers.json"), "r") as f:
    HOLDING_REGISTERS = json.load(f)

# read/write registers
with open(path.join(THIS_DIR, "coils.json"), "r") as f:
    COILS = json.load(f)

# read only
with open(path.join(THIS_DIR, "discrete_inputs.json"), "r") as f:
    DISCRETE_INPUTS = json.load(f)

# read only
with open(path.join(THIS_DIR, "input_registers.json"), "r") as f:
    INPUT_REGISTERS = json.load(f)


class Registers:
    """
    Smarty Registers.

    MCB 1.21 Modbus Table:
    http://salda.lt/mcb/downloads/doc/MCB%201.21%20Modbus%20table%202018-05-03.xlsx
    """

    def __init__(self, conn):
        self._connection = conn
        self.holding_registers = [HoldingRegister(connection=conn, **r)
                                  for r in HOLDING_REGISTERS]
        self.coils = [Coil(connection=conn, **r) for r in COILS]
        self.discrete_inputs = [DiscreteInput(connection=conn, **r)
                                for r in DISCRETE_INPUTS]
        self.input_registers = [InputRegister(connection=conn, **r)
                                for r in INPUT_REGISTERS]
        self._registers = [self.holding_registers,
                           self.coils,
                           self.discrete_inputs,
                           self.input_registers]

    def get_register(self, register_id):
        """Get a register."""
        for regs in self._registers:
            for reg in regs:
                if reg.get_id() == register_id:
                    return reg
        return None

    def update(self) -> bool:
        """Update all registers."""
        return (self._update_holding_registers() and
                self._update_coils() and
                self._update_input_registers() and
                self._update_input_registers())

    def _update_holding_registers(self) -> bool:
        """Read Holding Registers."""
        res1 = self._connection.client.read_holding_registers(
            1, 37, unit=self._connection.slave)
        res2 = self._connection.client.read_holding_registers(
            200, 3, unit=self._connection.slave)
        if res1.isError() or res2.isError():
            return False
        res = {k: v for k, v in zip(range(1, 37), res1.registers)}
        res.update({k: v for k, v in zip(range(200, 202), res2.registers)})

        update_states(res, self.holding_registers)
        return True

    def _update_coils(self) -> bool:
        """Update Coils."""
        res1 = self._connection.client.read_coils(
            1, 9, unit=self._connection.slave)
        if res1.isError():
            return False
        res = {k: v for k, v in zip(range(1, 10), res1.bits)}

        update_states(res, self.coils)
        return True

    def _update_discrete_inputs(self) -> bool:
        """Update Discrete Inputs."""
        res1 = self._connection.client.read_discrete_inputs(
            1, 67, unit=self._connection.slave)
        res2 = self._connection.client.read_discrete_inputs(
            188, 2, unit=self._connection.slave)
        if res1.isError() or res2.isError():
            return False
        res = {k: v for k, v in zip(range(1, 67), res1.bits)}
        res.update({k: v for k, v in zip(range(188, 190), res2.bits)})

        update_states(res, self.discrete_inputs)
        return True

    def _update_input_registers(self) -> bool:
        """Update input registers"""
        res1 = self._connection.client.read_input_registers(
            1, 66, unit=self._connection.slave)
        res2 = self._connection.client.read_input_registers(
            67, 66, unit=self._connection.slave)
        if res1.isError() or res2.isError():
            return False
        res = {k: v for k, v in zip(range(1, 132),
                                    res1.registers +
                                    res2.registers)}
        update_states(res, self.input_registers)
        return True


def update_states(res, registers) -> None:
    """Update Registers state."""
    for key, value in res.items():
        for reg in registers:
            if key == reg.addr:
                reg.state = value
