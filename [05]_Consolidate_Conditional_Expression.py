# -----------------------------------------------------------------------------------
# -----------------------------Consolidate Conditional Expression--------------------
# -----------------------------------------------------------------------------------
# [problem] :You have multiple conditionals that lead to the same result or action.
# [Solution] :Consolidate all these conditionals in a single expression.
# -----------------------------------------------------------------------------------


seniority, monthsDisabled, isPartTime = 5, 17, True


def disabilityAmount():
    if seniority < 2:
        return 0
    if monthsDisabled > 12:
        return 0
    if isPartTime:
        return 0
    # Compute the disability amount.
    # ...


def disability_Amount():
    if is_Not_Eligible_For_Disability():
        return 0


def is_Not_Eligible_For_Disability():
    isNotEligibleForDisability = seniority < 2 and monthsDisabled > 12 and isPartTime
    return isNotEligibleForDisability
