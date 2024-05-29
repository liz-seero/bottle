def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial of", num, "is", factorial(num))
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
