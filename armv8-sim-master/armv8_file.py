"""
This module handles file parsing for armv8-sim.
"""
from armv8_core import ARMv8Core
import armv8_isa


def coreParseFile(core, file):
    """
    Parse a given file with a given ARMv8Core.
    """
    #labels = {}
    #code = {}

    lines = file.read().splitlines()

    PC = 0
    for line in lines:
        if line.endswith(":"):
            if " " not in line:
                core.labels[line[:-1]] = PC

        PC = PC + 4

    PC = 0
    for line in lines:
        cline = [x.replace((','or':'),'') for x in line.lstrip().split()]
        core.code[PC] = cline

        PC = PC + 4

    while core.reg["PC"].get() < PC:
        corePC = core.reg["PC"].get()
        if core.code[corePC]:
            if isinstance(core.code[corePC][0], str):
                print(core.code[corePC][0])
            if core.code[corePC][0].upper() in armv8_isa.instset:
                i = armv8_isa.instset[core.code[corePC][0].upper()]
                if i.inst_format == "B":
                    print "B"
                    i.execute(core,core.code[corePC][1])
                elif i.inst_format == "CB":
                    print "CB"
                elif i.inst_format == "D":
                    print "D"
                elif i.inst_format == "I":
                    print "I"
                elif i.inst_format == "IW":
                    print "IW"
                elif i.inst_format == "R":
                    print "R"
                    print(core.code[corePC][3])
                    print(core.code[corePC][2])
                    print(core.code[corePC][1])
                    i.execute(core,
                          core.code[corePC][3],
                          0,
                          core.code[corePC][2],
                          core.code[corePC][1])

        core.reg["PC"].set(corePC + 4)

    #print core.labels
    #print core.code

    return


def parseFile(file):
    """
    Method for quickly parsing a file with a new ARMv8Core.
    """
    c = ARMv8Core()
    return coreParseFile(c, file)
