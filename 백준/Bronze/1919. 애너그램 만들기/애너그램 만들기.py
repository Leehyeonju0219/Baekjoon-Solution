word1 = input()
word2 = input()

alpha_list1 = []
alpha_list2 = []
for i in word1:
    alpha_list1.append(i)

for i in word2:
    alpha_list2.append(i)

alpha_list1.sort()
alpha_list2.sort()
diff = []
while len(alpha_list1) > 0 and len(alpha_list2) > 0:
    if alpha_list1[len(alpha_list1)-1] == alpha_list2[len(alpha_list2)-1]:
        alpha_list1.pop()
        alpha_list2.pop()
    else:
        if alpha_list1[len(alpha_list1)-1] > alpha_list2[len(alpha_list2)-1]:
            diff.append(alpha_list1.pop())
        else:
            diff.append(alpha_list2.pop())

answer = len(diff) + len(alpha_list1) + len(alpha_list2)
print(answer)