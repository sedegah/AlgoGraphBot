# Searching Algorithms - Step by Step

def linear_search_steps(arr, target):
    steps = []
    for i, val in enumerate(arr):
        if val == target:
            steps.append(f"Found {target} at index {i}")
            return "\n".join(steps)
        else:
            steps.append(f"Checked index {i}: {val} ≠ {target}")
    steps.append("Target not found")
    return "\n".join(steps)


def binary_search_steps(arr, target):
    steps = []
    arr_copy = sorted(arr)
    left, right = 0, len(arr_copy) - 1

    while left <= right:
        mid = (left + right) // 2
        steps.append(f"Middle index {mid}, value {arr_copy[mid]}")
        if arr_copy[mid] == target:
            steps.append(f"Found {target} at index {mid}")
            return "\n".join(steps)
        elif arr_copy[mid] < target:
            steps.append(f"{target} > {arr_copy[mid]} → Search right half")
            left = mid + 1
        else:
            steps.append(f"{target} < {arr_copy[mid]} → Search left half")
            right = mid - 1

    steps.append("Target not found")
    return "\n".join(steps)
