#   求1+2!+3!+...+20!的和
def facSum(count):
    addSum = 0
    for i in range(1, count + 1):
        addSum += factorial(i)
    return addSum


def factorial(num):
    factorSum = 1
    for i in range(1, num+1):
        factorSum *= i
    return factorSum


print(facSum(20))