def can_complete_circuit(gas, cost):
    total = 0
    curr = 0
    start = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]
        curr += gas[i] - cost[i]

        if curr < 0:
            start = i + 1
            curr = 0

    return start if total >= 0 else -1

# Example
print(can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3  
