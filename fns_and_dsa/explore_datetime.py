from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time"""
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """Calculate a future date based on user input"""
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()