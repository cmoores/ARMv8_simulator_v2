"""
This module provides a base class for all B type ARMv8 instructions.
"""
from inspect import getargspec
from instruction import core


class cmp_inst:
    """
    This class provides a base for a B format instructions.
    """

    inst_format = 'CMP'
    opcode = 0b0

    operation = None
    op_args = ["proc", "operand1","operand2"]

    
    def __eq__(self, other):
        if self.inst_format != other.inst_format:
            return False
        elif self.opcode != other.opcode:
            return False
        elif self.operation != other.operation:
            return False
        elif self.op_args != other.op_args:
            return False
        else:
            return True


    def execute(self, proc, operand1, operand2):
        if not isinstance(proc, core):
            raise TypeError("proc must be an ARMv8Core")
        if type(operand1) is not int:
            raise TypeError("operand1 must be of type int")
        if type(operand2) is not int:
            raise TypeError("operand2 must be of type int")

        if self.operation is not None:
            self.operation(proc, operand1, operand2)

    def __init__(self, opcode, operation):
        if type(opcode) is not int:
            raise TypeError("opcode must be of type int")
        args = getargspec(operation).args
        if len(args) > len(self.op_args) or args != self.op_args:
            err_str = ("operation must be a function " +
                       "accepting {} ".format(len(self.op_args)) +
                       "arguments: {}".format(self.op_args))
            raise TypeError(err_str)
        self.opcode = opcode
        self.operation = operation
