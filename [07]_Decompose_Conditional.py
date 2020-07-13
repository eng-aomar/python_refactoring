# -------------------------------------------------------------------------------------------------------------------
# -------------------------------- Decompose Conditional ------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# [Problem]: ou have a complex conditional (if-then/else or switch)
# [Solution]: Decompose the complicated parts of the conditional into separate methods: the condition, then and else.
# -------------------------------------------------------------------------------------------------------------------

from datetime import date

SUMMER_START = '12/06/2020'
SUMMER_END = '31/10/2020'
winterRate, summerRate = 0.5, 0.6
quantity = int(input('please enter quantity: '))

winterServiceCharge = float(input('please enter winterServiceCharge: '))
# [Problem]: ou have a complex conditional (if-then/else or switch)
if date.before(SUMMER_START) or date.after(SUMMER_END):
    charge = quantity * winterRate + winterServiceCharge
else:
    charge = quantity * summerRate


# [Solution]: Decompose the complicated parts of the conditional into separate methods: the condition, then and else.

def is_winter():
    return date.before(SUMMER_START) or date.after(SUMMER_END)


def winter_rate():
    return quantity * winterRate + winterServiceCharge


def summar_rate():
    return quantity * summerRate


if is_winter():
    charge = winter_rate()
else:
    charge = summar_rate()


# Solution ---- > Extract Methods
