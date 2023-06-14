
def P_SCORE(estimate, weight, reference):
    hit1, hit2 = 0, 0
    if abs(estimate[0] - reference)/reference <= 0.08:
        hit1 = 1
    if abs(estimate[1] - reference)/reference <= 0.08:
        hit2 = 1
    return weight * hit1 + (1 - weight) * hit2


def ALOTC_SCORE(estimate, reference):
    hit1, hit2 = 0, 0
    if abs(estimate[0] - reference)/reference <= 0.08:
        hit1 = 1
    if abs(estimate[1] - reference)/reference <= 0.08:
        hit2 = 1
    if hit1 or hit2:
        return 1
    return 0
