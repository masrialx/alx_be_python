def main():
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Check if the input number is valid (a non-zero integer)
        if number == 0:
            print("Please enter a non-zero number.")
            return

        # Generate and print the multiplication table from 1 to 10
        for i in range(1, 11):
            result = number * i
            print(f"{number} * {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Run the main function
if __name__ == "__main__":
    main()