def study_schedule(permanence_period, target_time):
    valor = 0
    for period in permanence_period:
        if (period[0] is None or period[1] is None or target_time is None):
            return None
        if (not isinstance(period[0], int) or
                not isinstance(period[1], int)):
            return None
        if ((period[0]) <= (target_time) <= (period[1])):
            valor += 1

    return valor


if __name__ == "__main__":
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    x = study_schedule(permanence_period, 2)
    print(x)
    raise NotImplementedError
