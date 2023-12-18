
def binarySearch(numbers, num):

    n = False
    count = 0
    while not n:

        count += 1
        pointer = round(len(numbers)/2)
        if numbers[pointer] == num:
            return("We have found your number: " + str(num) + "\nOn search " + str(count) + "!")
        elif numbers[pointer] > num:
            numbers = numbers[:pointer]

        elif numbers[pointer] < num:
            numbers = numbers[pointer + 1:]

        if not numbers:  # Check if the list is empty
                return("Number not found")

def sort(numbers, num):

    numbers.sort()
    print(numbers)
    result = binarySearch(numbers, num)
    print(result)

numbers = [2, 4, 7, 3, 45, 78, 23, 34]
sort(numbers, 7)
