def linear_search_steps(arr, target):
    steps = []
    steps.append(f"Searching for {target} using Linear Search...\n")

    for i, val in enumerate(arr):
        if val == target:
            steps.append(f"Found {target} at index {i}")
            return "\n".join(steps)
        else:
            steps.append(f"Checked index {i}: {val} ≠ {target}")
    
    steps.append("\nTarget not found")
    return "\n".join(steps)


def binary_search_steps(arr, target):
    steps = []
    arr_copy = sorted(arr)
    left, right = 0, len(arr_copy) - 1

    steps.append(f"Searching for {target} using Binary Search...\n")
    steps.append(f"Sorted array: {arr_copy}\n")

    while left <= right:
        mid = (left + right) // 2
        steps.append(f"Middle index {mid}, value {arr_copy[mid]}")

        if arr_copy[mid] == target:
            steps.append(f"Found {target} at index {mid}")
            return "\n".join(steps)
        elif arr_copy[mid] < target:
            steps.append(f"{target} > {arr_copy[mid]} → Searching right half\n")
            left = mid + 1
        else:
            steps.append(f"{target} < {arr_copy[mid]} → Searching left half\n")
            right = mid - 1

    steps.append("Target not found")
    return "\n".join(steps)
