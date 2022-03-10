def binary_func(any_list, start, end, ans):

    if start > end:
        return None

    middle = (start + end) // 2

    if ans == any_list[middle]:
        return middle
    elif ans > any_list[middle]: # start = middle + 1
        start = middle + 1
    else:
        end = middle - 1

    return binary_func(any_list, start, end, ans)


print("10개 정수를 입력하시오 (space): ")
num_list = list(map(int, input().split()))

num_list.sort()
print("값을 입력하세요")
target = input() # target 은 str

print("{}이 당신이 찾던 index예요!".format(binary_func(num_list, 0, len(num_list) - 1, int(target))))

print(num_list)