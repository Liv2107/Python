
def linearSearch(numbers, num):

    for i in range(len(numbers)):
        if num == numbers[i]:
            return "We have found your number: " + str(num) + "\nOn count: " + str(i+1)

    return "Number not found"

numbers = [2, 6, 23, 78, 4, 56, 23]
num = 78

result = linearSearch(numbers, num)
print(result)

