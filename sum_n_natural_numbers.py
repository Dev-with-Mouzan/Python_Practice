def sum_natural_numbers(n):
    if n < 0:
        return 0
    return n * (n + 1) // 2

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer N: "))
        if n < 0:
            print("Please enter a positive integer.")
        else:
            print(f"The sum of first {n} natural numbers is {sum_natural_numbers(n)}")
    except ValueError:
        print("Invalid input.")
