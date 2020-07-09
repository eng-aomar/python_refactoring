# -----------------------------------------------------------------------------------
# -----------------------------Consolidate Duplicate Conditional Fragments-----------
# -----------------------------------------------------------------------------------
# [problem] : Identical code can be found in all branches of a conditional.
# [Solution] :Move the code outside of the conditional.
# ----------------------------------------------------------------------------------

price = int(input('Please enter your price: '))
if isSpecialDeal():
    total = price * 0.95
    send()
else:
    total = price * 0.98
    send()


def send():
    pass


def isSpecialDeal():
    pass
