def solution(my_string, queries):
    for query in queries:
        temp = my_string[query[0]: query[1]+1]
        temp = temp[::-1]
        my_string = my_string[:query[0]] + temp + my_string[query[1]+1:]
    return my_string