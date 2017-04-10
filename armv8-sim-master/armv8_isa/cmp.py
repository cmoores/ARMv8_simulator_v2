"""
This module provides the CMP_format CMP instruction, which is used for Branching
"""
#CMP <Xn|SP>, #<imm>{, <shift>}

from armv8_isa import CMP

def operation(proc, operand1, operand2):
    # we want to take op1 - op2 and see if the condition flags need to be updated
    # flag_zero will be set to true if R2 == R1
    raw = operand1 - operand2
    if raw == 0:
        proc.Z = True
        proc.N = False

    else:
        if raw > 0:
            proc.Z = False
            proc.N = False

        else:
            proc.Z = False
            proc.N = True


#    result = int(raw % proc.reg[Rd].data_max())
#    proc.reg[Rd].set(result)

CMP = CMP(99, operation)
