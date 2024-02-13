def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = 2024
        age = current_year - birth_year
        print(f"You are {age} years old.")
    except ValueError:
        print("Please enter a valid integer for the birth year.")

calculate_age()

def helloWorld():
	print(‘Hello World’)


helloWorld()

