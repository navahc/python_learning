def is_prime(num):
    # Check if number is less than 2, which is not prime
    if num < 2:
        return False
    print(num**0.5)
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        print(i)
        if num % i == 0:
            return False
    
    return True

# Example usage
number = 2
if is_prime(number):
    print(f"{number} is a prime number:",number)
else:
    print(f"{number} is not a prime number.")
