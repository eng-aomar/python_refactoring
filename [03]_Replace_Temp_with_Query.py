
# --------------------------------------------------------------------------------------------------------------
# ------------------------------------------Replace Temp with Query---------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# [Problem] : You place the result of an expression in a local variable for later use in your code.
# [Solution] : Move the entire expression to a separate method and return the result from it. Query the method
# instead of using a variable. Incorporate the new method in other methods, if necessary.
# --------------------------------------------------------------------------------------------------------------


quantity = 10
itemPrice = 5

# [Problem] : You place the result of an expression in a local variable for later use in your code.


def calculateTotal():
    basePrice = quantity * itemPrice
    if basePrice > 1000:
        return basePrice * 0.95
    else:
        return basePrice * 0.98

 # [Solution] : Move the entire expression to a separate method and return the result from it. Query the method


def calculateTotal():
    if basePrice() > 1000:
        return basePrice() * 0.95
    else:
        return basePrice() * 0.98


def basePrice():
    return quantity * itemPrice
