def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // calculate_gcd(a, b)

if __name__ == "__main__":
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The LCM of {num1} and {num2} is {calculate_lcm(num1, num2)}")
    except ValueError:
        print("Invalid input.")
