# Debugging Exercise: Learn to identify and fix common errors in Python

# 1. Descriptive print statements
def odd_or_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# 2. Off-by-one errors
def count_to_five():
    for i in range(1, 6):  # fixed range
        print(i)

# 3. Handling user input safely
def safe_division():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# 4. Debugging a simple game (FizzBuzz logic)
def fizzbuzz():
    for number in range(1, 21):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

if __name__ == "__main__":
    print("Debugging and Error Handling Examples")
    print("-------------------------------------")

    odd_or_even(7)
    count_to_five()
    safe_division()
    fizzbuzz()