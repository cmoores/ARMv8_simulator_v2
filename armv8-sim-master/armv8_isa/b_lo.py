"""
This module provides the B-format B.LO instruction
"""
from armv8_isa import B

#consumes a core, a branch condition (ie. EQ or NEQ), and an address
def operation(proc, BR_address):
    # the logic of branch eq is to only branch if the the proc.flag_zero == 1
    # if true we will increment the PC to label + 4
    if not proc.C:
        proc.reg["PC"].set(proc.labels[BR_address])

B_LO = B(95, operation)
