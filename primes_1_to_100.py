def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("Prime numbers between 1 and 100:")
    for num in range(1, 101):
        if is_prime(num):
            print(num, end=" ")
    print()
