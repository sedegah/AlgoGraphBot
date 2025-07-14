def bubble_sort_visualization(arr):
    result = []
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            result.append(f"Compare {a[j]} and {a[j+1]}")
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                result.append(f"Swap → {a}")
    result.append(f"Sorted: {a}")
    return "\n".join(result)

def selection_sort_visualization(arr):
    a = arr[:]
    result = []
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            result.append(f"Compare {a[min_idx]} and {a[j]}")
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        result.append(f"Swap index {i} and {min_idx} → {a}")
    result.append(f"Sorted: {a}")
    return "\n".join(result)

def insertion_sort_visualization(arr):
    a = arr[:]
    result = []
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        result.append(f"Insert {key}")
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            result.append(f"Shift → {a}")
        a[j + 1] = key
        result.append(f"Inserted → {a}")
    result.append(f"Sorted: {a}")
    return "\n".join(result)

def quick_sort_visualization(arr):
    result = []
    def quicksort(a, depth=0):
        if len(a) <= 1:
            return a
        pivot = a[0]
        left = [x for x in a[1:] if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        result.append(f\"{'  '*depth}Pivot {pivot} → Left: {left}, Right: {right}\")
        return quicksort(left, depth+1) + [pivot] + quicksort(right, depth+1)
    sorted_arr = quicksort(arr)
    result.append(f\"Sorted: {sorted_arr}\")
    return \"\\n\".join(result)
