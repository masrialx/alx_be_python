def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))

        for i in range(1, 10 + 1):
            result = number * i
            print(f"{number} * {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()
