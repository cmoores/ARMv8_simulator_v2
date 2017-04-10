"""
This package provides the ARMv8 ISA
"""
# Import instruction classes
from instruction import R, I, D, B, CB, IW, CMP

# Import instructions from modules below
from add import ADD
from sub import SUB
from addi import ADDI
from subi import SUBI
from udiv import UDIV
from mul import MUL
from umulh import UMULH
from sdiv import SDIV
from andr import AND
from andi import ANDI
from eor import EOR
from eori import EORI
from lsl import LSL
from lsr import LSR
from orr import ORR
from orri import ORRI
from adds import ADDS
from addis import ADDIS
from subs import SUBS
from subis import SUBIS
from cmp import CMP
from b_eq import B_EQ
from b_ne import B_NE
from b_hs import B_HS
from b_lo import B_LO
from b_mi import B_MI
from b_pl import B_PL
from b_vs import B_VS
from b_vc import B_VC
from b_hi import B_HI
from b_ls import B_LS
from b_ge import B_GE
from b_lt import B_LT
from b_gt import B_GT
from b_le import B_LE
from b_al import B_AL
from b_nv import B_NV


instset = {
    "ADD": ADD,
    "SUB": SUB,
    "ADDI": ADDI,
    "SUBI": SUBI,
    "UDIV": UDIV,
    "MUL": MUL,
    "UMULH": UMULH,
    "SDIV": SDIV,
    "AND": AND,
    "ANDI": ANDI,
    "EOR": EOR,
    "EORI": EORI,
    "LSL": LSL,
    "LSR": LSR,
    "ORR": ORR,
    "ORRI": ORRI,
    "ADDS": ADDS,
    "ADDIS": ADDIS,
    "SUBS": SUBS,
    "SUBIS": SUBIS,
    "CMP": CMP,
    "B.EQ": B_EQ,
    "B.NE": B_NE,
    "B.HS": B_HS,
    "B.LO": B_LO,
    "B.MI": B_MI,
    "B.PL": B_PL,
    "B.VS": B_VS,
    "B.VC": B_VC,
    "B.HI": B_HI,
    "B.LS": B_LS,
    "B.GE": B_GE,
    "B.LT": B_LT,
    "B.GT": B_GT,
    "B.LE": B_LE,
    "B.AL": B_AL,
    "B.NV": B_NV
}
