
def main():
    try:
        # Prompt the user for a positive integer
        size = int(input("Enter the size of the pattern: "))

        # Ensure the size is a positive integer
        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Use a while loop to iterate through each row
        row = 0
        while row < size:
            # Use a for loop to print asterisks for each column in the row
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Run the main function
if __name__ == "__main__":
    main()