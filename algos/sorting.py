def bubble_sort_steps(arr):
    steps = []
    n = len(arr)
    arr_copy = arr.copy()

    steps.append(f"Starting Bubble Sort on: {arr_copy}\n")

    for i in range(n):
        for j in range(0, n - i - 1):
            step_desc = f"Compare {arr_copy[j]} and {arr_copy[j + 1]}"
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                step_desc += f"\n → Swap → {arr_copy}\n"
            else:
                step_desc += f"\n → No swap → {arr_copy}\n"
            steps.append(step_desc)

    steps.append(f"Sorted array: {arr_copy}")
    return "\n".join(steps)


def insertion_sort_steps(arr):
    steps = []
    arr_copy = arr.copy()

    steps.append(f"Starting Insertion Sort on: {arr_copy}\n")

    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        steps.append(f"Inserting {key} into sorted section: {arr_copy[:i]}")

        while j >= 0 and key < arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            steps.append(f" → Move {arr_copy[j]} to the right → {arr_copy}")
            j -= 1

        arr_copy[j + 1] = key
        steps.append(f" → Insert {key} at position {j + 1} → {arr_copy}\n")

    steps.append(f"Sorted array: {arr_copy}")
    return "\n".join(steps)


def selection_sort_steps(arr):
    steps = []
    arr_copy = arr.copy()
    n = len(arr_copy)

    steps.append(f"Starting Selection Sort on: {arr_copy}\n")

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps.append(f"Compare {arr_copy[j]} with current min {arr_copy[min_idx]}")
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j

        if min_idx != i:
            steps.append(f"Swap {arr_copy[i]} with {arr_copy[min_idx]}")
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
            steps.append(f" → {arr_copy}\n")
        else:
            steps.append(f"No swap needed → {arr_copy}\n")

    steps.append(f"Sorted array: {arr_copy}")
    return "\n".join(steps)


def quick_sort_steps(arr):
    steps = []
    arr_copy = arr.copy()

    steps.append(f"Starting Quick Sort on: {arr_copy}\n")

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            steps.append(f" → Partitioned at index {pi} → {arr}\n")
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        steps.append(f"Using pivot {pivot}")

        for j in range(low, high):
            steps.append(f"Compare {arr[j]} with pivot {pivot}")
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(f" → Swap → {arr}")

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(f" → Place pivot at index {i + 1} → {arr}")
        return i + 1

    quick_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    steps.append(f"\nSorted array: {arr_copy}")
    return "\n".join(steps)
