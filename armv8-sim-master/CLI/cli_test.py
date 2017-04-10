# package imports
from CLI import ARMv8Core
from CLI import armv8_file
from CLI import armv8_isa
from CLI import instruction
import sys

# main function
def main1():
    c = ARMv8Core()
    print("Welcome to our ARMv8 simulator!")
    print("Type help at any time for a list of commands, instructions, and tips")
    print ""
    running = True
    armv8_isa.CMP.execute(c,0,0)
    print_flags(c)
    #armv8_isa.CMP.execute(c,1,0)
    #print_flags(c)
    #armv8_isa.CMP.execute(c,0,1)
    #print_flags(c)

    f = open("../fact.s", 'r')
    armv8_file.coreParseFile(c, f)
    armv8_isa.B_EQ.execute(c,"fact")
    print(c.labels)
    print(c.labels["fact"])
    print(c.reg["PC"].data)

    #print(c.labels)
    #print(c.code)


def print_flags(core):
    print "Zero Flag: {}".format(core.flag_zero)
    print "Negative Flag: {}".format(core.flag_negative)
    print "Carry Flag: {}".format(core.flag_carry)
    print "Overflow Flag: {}".format(core.flag_overflow)
    print ""
