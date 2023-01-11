#Creator: RMW 12/19/22

def maximum (numbers) :
    max_num = max (numbers)
    return max_num
#function finds the maximum number

def minimum (numbers) :
    min_num= min(numbers)
    return min_num
#function finds the minimum number

def maximum_minimum_numbers (numbers) :
    max_min={max (numbers), min(numbers)}
    return max_min
#function combines both functions

#Test Cases
print (maximum_minimum_numbers ([2, 4, 6, 8, 10]))
#Even numbers
print (maximum_minimum_numbers([1, 3, 5, 7, 9, 11]))
#Odd numbers
