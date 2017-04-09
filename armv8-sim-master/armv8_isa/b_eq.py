"""
This module provides the R-format ADD instruction
"""
from armv8_isa import B_cond

#consumes a core, a branch condition (ie. EQ or NEQ), and an address
def operation(proc, cond, label): 
    # the logic of branch eq is to only branch if the the proc.flag_zero == 1
    # if true we will increment the PC to label + 4
    
    if proc.flag_zero == True:
        proc.reg[32].set = label + 4

B_eq = B_cond(98, operation)