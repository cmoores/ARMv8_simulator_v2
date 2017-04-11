"""
This module provides the R-format SUB instruction
"""
from armv8_isa import R

def operation(proc, Rm, shamt, Rn, Rd):
    raw = proc.reg[Rn.upper()].get() - proc.reg[Rm].get()
    result = int(raw % proc.reg[Rd.upper()].data_max())
    #if raw < proc.reg[Rd].data_min():
    #    result = 0
    #else:
    #    result = raw
    proc.reg[Rd.upper()].set(result)

SUB = R(0x658, operation)
