class AgeRestrictionError(Exception):
    """Exception raised for voters under the required age."""
    def __init__(self, age, message="You must be at least 18 years old to vote."):
        self.age = age
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    """Check if the given age is eligible for voting."""
    if age < 18:
        raise AgeRestrictionError(age)
    print("Congratulations! You are eligible to cast your vote.")

try:
    user_age = int(input("Enter your age to check voting eligibility: "))
    validate_age(user_age)
except AgeRestrictionError as error:
    print(f"Error: {error.message} (Provided Age: {error.age})")
except ValueError:
    print("Invalid input! Please enter a numerical value for age.")
