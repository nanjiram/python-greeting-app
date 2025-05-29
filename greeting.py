# greeting.py

def greet_user():
    name = input("Enter your name: ")
    day = input("Enter the day of the week: ")
    print(f"Hello, {name}! Happy {day}!")

def get_feedback():
    feedback = input("What do you think about this greeting program? ")
    print("Thank you for your feedback!")

# Run both functions
greet_user()
get_feedback()
