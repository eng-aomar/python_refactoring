# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------- Extract variable -----------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# [Problem] : You have an expression that’s hard to understand.
# [Solution] : Place the result of the expression or its parts in separate variables that are self-explanatory.
# ---------------------------------------------------------------------------------------------------------------

DIVDE_BY_ONE_HANDRED = 100

# [Problem] : You have an expression that’s hard to understand.


def calculate_interest(principle, time, rate):
    ''' This function calculates the interest where principle is loan amount, time = loan period in years, rate = interst_rate per year  '''
    if principle > 0:
        return (principle * time * rate) / 100
    else:
        return None

# [Solution] : Place the result of the expression or its parts in separate variables that are self-explanatory.


def calculate_interest(principle, time, rate):
    ''' This function calculates the interest where principle is loan amount, time = loan period in years, rate = interst_rate per year  '''
    loan_rate = principle * time * rate
    if principle > 0:
        return (loan_rate) / DIVDE_BY_ONE_HANDRED

    else:
        return None


intrest_rate = calculate_interest(100, 5, 5)
print("interst =", intrest_rate, 'JOD')
