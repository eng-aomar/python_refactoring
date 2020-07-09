# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------- Extract Method variable -----------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# [Problem] : You have an expression that’s hard to understand.
# [Solution] : Place the result of the expression or its parts in separate variables that are self-explanatory.
# ---------------------------------------------------------------------------------------------------------------


def calculate_interest(principle, time, rate):
    if principle > 0:
        return (principle * time * rate) / 100
    else:
        return None


#intrest_rate = calculate_interest(5, 6, 12)
# print(intrest_rate)
