def task_scheduler(tasks, space):
    last_seen = {}
    day = 0

    for task in tasks:
        day += 1

        if task in last_seen and day - last_seen[task] <= space:
            day = last_seen[task] + space + 1

        last_seen[task] = day

    return day
# Example
print(task_scheduler(["A","B","A"], 2))  # Output: 4    