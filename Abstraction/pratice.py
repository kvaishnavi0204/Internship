# Create a dictionary with fruit names as keys and their corresponding colors as values
fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'orange': 'orange',
    'grape': 'purple'
}

# Add a new key-value pair to the dictionary
fruit_colors['kiwi'] = 'green'

# Print the updated dictionary
print(fruit_colors)

# Create a tuple with three elements
my_tuple = (10, 'hello', True)

# Print the original tuple
print("Original Tuple:", my_tuple)

# Attempt to change the value of the first element to 20
try:
    my_tuple[1] = 'hello'
except TypeError as e:
    print("Error occurred while trying to change the value of the first element:", e)

names=['siri','akki','vaishu','gundu']
names.append('vaishu')
print(names)

n=int(input('enter the number:'))
sum=0
for i in range(1,n+1):
    sum += i
print("The sum of the first", n, "natural numbers is:", sum)

# Initialize the factorial to 1
fact = 1

# Use a loop to calculate the factorial of the given number
for i in range(1, num + 1):
    fact *= i

# Print the factorial of the given number
print("The factorial of", num, "is:", fact)

# Get the number from the user
n = int(input("Enter a number: "))

# Initialize the digit count to 0
digit_count = 0

# Count the number of digits in the given number
while n > 0:
    n = int(n/10)
    digit_count += 1

# Print the number of digits in the given number
print("The number of digits in", n, "is", digit_count)

# Get the number from the user
num = int(input("Enter a number to display its multiplication table: "))

# Print the multiplication table of the given number
print("Multiplication table of", num, ":")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)