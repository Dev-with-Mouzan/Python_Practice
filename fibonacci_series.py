def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

if __name__ == "__main__":
    try:
        n = int(input("Enter number of terms for Fibonacci series: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            print(f"Fibonacci series ({n} terms):")
            print(*fibonacci_series(n))
    except ValueError:
        print("Invalid input.")
