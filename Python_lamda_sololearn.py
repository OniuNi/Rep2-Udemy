#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.

x1 = lambda a1:a1+15
print(x1(5))

#Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def func1(n):
 return lambda x:x*n
result = func1(2)
print("Double the number of result ",result(15))
result = func1(3)
print("Triple the number of result ",result(15))
result = func1(4)
print("Quadraple the number of result ",result(15))
result = func1(5)
print("Quindraple the number of result ",result(15))

#Write a Python program to sort a list of tuples using Lambda.
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x1: x1[-1])
print("\nSorting the List of Tuples:")
print(subject_marks)

#Write a Python program to extract year, month, date and time using Lambda.
import datetime
now=datetime.datetime.now()
print(now)
year = lambda x:x.year
month= lambda x:x.month
day = lambda x:x.day
t= lambda x:x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))

#Write a Python program to find intersection of two given arrays using Lambda.
arr1=[1,2,3,4,5]
arr2=[2,5,6,7,9]
print("Original list ",arr1,arr2)
intersection=list(filter(lambda x3:x3 in arr1,arr2))
print("intersection is ",intersection)

#Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
array4=[1,2,4,12,67,56,32]
print("original array is ",array4)
odd1=len(list(filter(lambda x3:(x3%2==0),array4)))
even1=len(list(filter(lambda x3:(x3%2!=0),array4)))
print("even numbers are",odd1)
print("even numbers are",even1)

#Write a Python program to add two given lists using map and lambda.
nums5 = [1, 2, 3]
nums6 = [4, 5, 6]
print("Original list:")
print(nums6)
print(nums5)
result = map(lambda x4, y4: x4 + y4, nums5, nums6)
print("\nResult: after adding two list")
print(list(result))

#Write a Python program to find the values of length six in a given list using Lambda.
weekdays=['monday','tuesday','wednesday','thursday','friday']
days=filter(lambda day:day if len(day)==6 else '',weekdays )
for d in days:
 print(d)

#Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda
def sort_matrix(M):
    result = sorted(M, key=lambda matrix_row: sum(matrix_row))
    return result

matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

print("Original Matrix:")
print(matrix1)
print("\nSort the said matrix in ascending order according to the sum of its rows")
print(sort_matrix(matrix1))
print("\nOriginal Matrix:")
print(matrix2)
print("\nSort the said matrix in ascending order according to the sum of its rows")
print(sort_matrix(matrix2))

#Write a Python program to reverse strings in a given list of string values using lambda.
def reverse_strings_list(string_list):
    result = list(map(lambda x: "".join(reversed(x)), string_list))
    return result

colors_list = ["Red", "Green", "Blue", "White", "Black"]
print("\nOriginal lists:",colors_list)
print("\nReverse strings of the said given list:")
print(reverse_strings_list(colors_list))
