# 1
# Write a function named greet that prints "Hello, World!". Call the function. 
# 
# def greet():
#     print("Hello, World!")


# greet()





# 2
# Write a function add that takes two numbers as arguments and returns their sum. Call the function with different inputs.

# def add(num1, num2):
#     return num1 + num2


# result1 = add(5, 3)
# result2 = add(10, 20)
# result3 = add(-2, 8)


# print(f"5 + 3 = {result1}")
# print(f"10 + 20 = {result2}")
# print(f"-2 + 8 = {result3}")




# 3
# Create a function multiply that takes two numbers and returns their product.

# def multiply(num1, num2):
#     return num1 * num2


# result1 = multiply(4, 5)
# result2 = multiply(10, 3)
# result3 = multiply(-2, 6)

# print(f"4 * 5 = {result1}")
# print(f"10 * 3 = {result2}")
# print(f"-2 * 6 = {result3}")



# 4
# Write a function personal_greet that takes a name as an argument and prints "Hello, [name]!".

# def personal_greet(name):
#     print(f"Hello, {name}!")


# personal_greet("Alice")
# personal_greet("Bob")
# personal_greet("Tom")




# 5
# Write a function calculate_area that takes length and width as parameters and returns the area of a rectangle.
# print(calculate_area(5, 10))  # Example call

# def calculate_area(length, width):
#     return length * width


# print(calculate_area(5, 10)) 




# 6
# Write a function greet_with_message that takes a name and an optional message. The default message should be "Welcome!".
# greet_with_message("Alice") # Default message greet_with_message("Bob", "Good morning!") # Custom message

# def greet_with_message(name, message="Welcome!"):
#     print(f"Hello, {name}! {message}")


# greet_with_message("Alice")          
# greet_with_message("Bob", "Good morning!")




# 7
# Write a function power that takes a number and an optional exponent. The default exponent should be 2 (square the number).
# print(power(3)) # 3^2 
# print(power(3, 3)) # 3^3

# def power(number, exponent=2):
#     return number ** exponent


# print(power(3))   
# print(power(3, 3))





# 8
# Write a program with a global variable x. Create a function that changes the value of x inside the function and prints both the global and local values.

# x = 10

# def change_x():
#     global x  
#     local_x = 20  
    
#     x = 30
    
#     print(f"Local x: {local_x}")
#     print(f"Global x: {x}")

# change_x()

# print(f"Global x outside function: {x}")




# 9
# Write a function is_even that takes a number and returns True if the number is even and False otherwise.
# print(is_even(4)) # True
# prin t(is_even(5)) # False


# def is_even(number):
#     return number % 2 == 0


# print(is_even(4)) 
# print(is_even(5)) 




# 10
# Write a function find_max that takes two numbers and returns the larger of the two.
# print(find_max(10, 20))  # Example call

# def find_max(num1, num2):
#     return num1 if num1 > num2 else num2

# print(find_max(10, 20))





# 11
# Write a function calculate_discount that takes a price and a discount percentage and returns the discounted price.
# print(calculate_discount(100, 20))  # 20% off on 100

# def calculate_discount(price, discount_percentage):
#     discount_amount = (discount_percentage / 100) * price
#     discounted_price = price - discount_amount
#     return discounted_price

# print(calculate_discount(100, 20))




# 12
# Write a function filter_positive that takes a list of numbers and returns a new list containing only the positive numbers.
# print(filter_positive([-5, 3, -1, 2, 0]))  # Example call

# def filter_positive(numbers):
#     return [num for num in numbers if num > 0]

# print(filter_positive([-5, 3, -1, 2, 0]))



# 13
# Write a function count_digits that takes an integer and returns the number of digits in it.
# print(count_digits(12345))  # Example call

# def count_digits(number):
#     return len(str(abs(number)))


# print(count_digits(12345)) 




# 14
# Write a function sum_of_digits that calculates the sum of all digits in an integer
# print(sum_of_digits(123))  # Example call

# def sum_of_digits(number):
#     return sum(int(digit) for digit in str(abs(number)))


# print(sum_of_digits(123)) 