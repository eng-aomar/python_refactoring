# -------------------------------------------------------------------------------------------------------------------
# -------------------------------- Remove Control Flag ------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# [Problem]:You have a boolean variable that acts as a control flag for multiple boolean expressions.
# [Solution]: Instead of the variable, use break, continue and return and remove the contditional statment.
# -------------------------------------------------------------------------------------------------------------------


found = False
people = ('Ahmad', 'Samer', 'Rahaf', 'Sara', 'Lujain')
# [Problem]:You have a boolean variable that acts as a control flag for multiple boolean expressions.

for name in people:
    if not found:
        if name == 'Ahmad':
            sendAlert()
            found = True

# [Solution]: Instead of the variable, use break, continue and return and remove the contditional statment.

for name in people:

    if name == 'Ahmad':
        sendAlert()
        break


def sendAlert():
    print("Found !")
