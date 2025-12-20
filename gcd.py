import math

def calculate_gcd(a, b):
    # Using math.gcd is efficient, but user might want logic.
    # Logic: Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The GCD of {num1} and {num2} is {calculate_gcd(num1, num2)}")
    except ValueError:
        print("Invalid input.")
