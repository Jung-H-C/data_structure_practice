def binary_search(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(target, start, end, data)

test_list = [10, 1, 3, 2, 9, 8, 7, 6, 5, 4]

test_list.sort()
target = 7
index = binary_search(target, 0, 10, test_list)

print(test_list)
print(index)