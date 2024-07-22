input = input()
inputs = input[:len(input)-1].split(', ')

tmp = inputs[0].split()
types = [tmp[0]]*len(inputs)
inputs[0] = tmp[1]

for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if inputs[i][j] == "[" or inputs[i][j] == "*" or inputs[i][j] == "&":
            additional_type = inputs[i][-(len(inputs[i])-j):]
            types[i] += additional_type[::-1].replace("][", "[]")
            types[i] = types[i]
            inputs[i] = inputs[i][:j]
            break

for i in range(len(inputs)):
    print(types[i], " ", inputs[i], ";", sep='')