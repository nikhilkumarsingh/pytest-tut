def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be less than 0")
