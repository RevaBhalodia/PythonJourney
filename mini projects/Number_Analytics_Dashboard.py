#Create a Python program that performs statistical analysis on a list of numbers entered by the user.

# Number Analytics Dashboard
# Function to calculate Mean
def calculate_mean(numbers):
    total = 0
    count = 0
    
    for num in numbers:
        total += num
        count += 1
    
    return total / count


# Function to sort list (Bubble Sort - manual sorting)
def sort_numbers(numbers):
    n = len(numbers)
    sorted_list = numbers[:]   # copy list
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # swap
                temp = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = temp
    
    return sorted_list


# Function to calculate Median
def calculate_median(numbers):
    sorted_list = sort_numbers(numbers)
    n = len(sorted_list)
    
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2


# Function to calculate Mode
def calculate_mode(numbers):
    frequency = {}
    
    # Count frequency manually
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    max_count = 0
    mode = None
    
    for key in frequency:
        if frequency[key] > max_count:
            max_count = frequency[key]
            mode = key
    
    return mode


# Function to check if number is prime
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


# Function to count prime numbers
def count_primes(numbers):
    count = 0
    
    for num in numbers:
        if is_prime(num):
            count += 1
    
    return count


# Function to count even and odd numbers
def count_even_odd(numbers):
    even = 0
    odd = 0
    
    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    
    return even, odd


# Function to calculate Standard Deviation (Population formula)
def calculate_std(numbers):
    mean = calculate_mean(numbers)
    total = 0
    n = len(numbers)
    
    for num in numbers:
        total += (num - mean) ** 2
    
    variance = total / n
    std_dev = variance ** 0.5
    
    return std_dev


# -------------------------------------
# Main Program
# -------------------------------------

print("📊 Number Analytics Dashboard")
print("---------------------------------")

# Take input from user
user_input = input("Enter numbers separated by space: ")

# Convert input string to list of integers
numbers = []
for value in user_input.split():
    numbers.append(int(value))

# Results
mean = calculate_mean(numbers)
median = calculate_median(numbers)
mode = calculate_mode(numbers)
prime_count = count_primes(numbers)
even_count, odd_count = count_even_odd(numbers)
std_dev = calculate_std(numbers)

# Display Results
print("\n----- Analysis Result -----")
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Prime Count:", prime_count)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Standard Deviation:", std_dev)