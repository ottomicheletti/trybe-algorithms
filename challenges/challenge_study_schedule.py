def study_schedule(permanence_period, target_time=None):
    students = 0

    if not (isinstance(target_time, int)):
        return None

    for arrival, exit in permanence_period:
        if not (isinstance(arrival, int) and isinstance(exit, int)):
            return None
        if arrival <= target_time <= exit:
            students += 1

    return students
