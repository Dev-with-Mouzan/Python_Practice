def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"The sum of digits of {num} is {sum_of_digits(num)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
