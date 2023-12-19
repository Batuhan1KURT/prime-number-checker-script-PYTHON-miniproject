
from math import sqrt

# Function to check if a number is prime
def is_prime(number):
    # Check if the number is less than or equal to 1
    if number <= 1:
        return print(f"The {number} is not a prime number!")

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(sqrt(number)) + 1):
        # If the number is divisible by any value in the range, it's not prime
        if number % i == 0:
            return print(f"The {number} is not a prime number!")

    # If no factors are found, the number is prime
    return print(f"The {number} is a prime number!")

# Main program
if __name__ == "__main__":
    # Get user input for a number
    number = int(input("Enter a number: "))
    
    # Call the is_prime function to check if the entered number is prime
    is_prime(number)