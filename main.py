# selection sort
print("정수 8개를 입력하시오 (space)")
num_list = list(map(int, input().split()))
# map(func, 적용할 값)
# ex) map(int, input().split())

print(num_list)

for i in range(len(num_list)):
    j = i
    for k in range(i+1, len(num_list)):
        if(num_list[k] < num_list[j]):
            j = k
        num_list[i], num_list[j] = num_list[j], num_list[i]


print(num_list)