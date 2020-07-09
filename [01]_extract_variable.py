# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------- Extract variable -----------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# [Problem] : You have an expression that’s hard to understand.
# [Solution] : Place the result of the expression or its parts in separate variables that are self-explanatory.
# ---------------------------------------------------------------------------------------------------------------


def calculate_interest(principle, time, rate):
    ''' This function calculates the interest where principle is loan amount, time = loan period in years, rate = interst_rate per year  '''
    if principle > 0:
        return (principle * time * rate) / 100
    else:
        return None


intrest_rate = calculate_interest(100, 5, 5)
print("interst =", intrest_rate, 'JOD')
