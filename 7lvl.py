def stray(numbers):
    result=0
    for i in numbers:
        result ^= i
    return result
list=[1,1,1,1,1,1,2]
print(stray(list))

