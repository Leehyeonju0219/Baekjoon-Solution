n = input()

nums = []
for i in n:
    nums.append(i)

answer = 0
plastic_nums = []
num_set = ['0','1','2','3','4','5','6','7','8','9']
for num in nums:
    if num not in plastic_nums:
        if num == '6':
            if '9' in plastic_nums:
                plastic_nums.pop(plastic_nums.index('9'))
                continue
        elif num == '9':
            if '6' in plastic_nums:
                plastic_nums.pop(plastic_nums.index('6'))
                continue
        plastic_nums.extend(num_set)
        answer += 1
        plastic_nums.pop(plastic_nums.index(num))
    else:
        plastic_nums.pop(plastic_nums.index(num))

print(answer)