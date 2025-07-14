def bubble_sort_visualization(arr):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            result.append(f"Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                result.append(f"Swapping {arr[j]} and {arr[j+1]}")
                arr[j], arr[j+1] = arr[j+1], arr[j]
            result.append(str(arr))
    return '\n'.join(result)

def selection_sort_visualization(arr):
    result = []
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            result.append(f"Comparing {arr[j]} and {arr[min_idx]}")
            if arr[j] < arr[min_idx]:
                min_idx = j
        result.append(f"Swapping {arr[i]} and {arr[min_idx]}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        result.append(str(arr))
    return '\n'.join(result)

def insertion_sort_visualization(arr):
    result = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        result.append(f"Inserting {key}")
        while j >= 0 and key < arr[j]:
            result.append(f"Moving {arr[j]} to the right")
            arr[j+1] = arr[j]
            j -= 1
            result.append(str(arr))
        arr[j+1] = key
        result.append(str(arr))
    return '\n'.join(result)

def quick_sort_visualization(arr, depth=0):
    if len(arr) <= 1:
        return f"{'  '*depth}Returning {arr}"

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    result = [f"{'  '*depth}Pivot {pivot} → Left: {left}, Right: {right}"]
    result.append(quick_sort_visualization(left, depth+1))
    result.append(quick_sort_visualization(right, depth+1))
    return '\n'.join(result)

def merge_sort_visualization(arr, depth=0):
    indent = '  ' * depth
    if len(arr) <= 1:
        return f"{indent}Returning {arr}"

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    result = [f"{indent}Dividing {arr} -> {left} & {right}"]
    result.append(merge_sort_visualization(left, depth+1))
    result.append(merge_sort_visualization(right, depth+1))
    result.append(f"{indent}Merging {left} & {right}")
    return '\n'.join(result)
