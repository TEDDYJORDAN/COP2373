import re

def validate_phone_number(phone_number):
    # Regular expression for phone number
    pattern = r'^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$'
    return re.match(pattern, phone_number) is not None

def validate_ssn(ssn):
    # Regular expression for social security number
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.match(pattern, ssn) is not None

def validate_zip_code(zip_code):
    # Regular expression for zip code
    pattern = r'^\d{5}(-\d{4})?$'
    return re.match(pattern, zip_code) is not None

def main():
    phone_number = input("Enter a phone number (in the format XXX-XXX-XXXX or (XXX) XXX-XXXX): ")
    ssn = input("Enter a social security number (in the format XXX-XX-XXXX): ")
    zip_code = input("Enter a zip code (in the format XXXXX or XXXXX-XXXX): ")

    # Validate
    phone_valid = validate_phone_number(phone_number)
    ssn_valid = validate_ssn(ssn)
    zip_valid = validate_zip_code(zip_code)

    # Display results
    print("\nValidation Results:")
    print(f"Phone Number ({phone_number}): {'Valid' if phone_valid else 'Invalid'}")
    print(f"Social Security Number ({ssn}): {'Valid' if ssn_valid else 'Invalid'}")
    print(f"Zip Code ({zip_code}): {'Valid' if zip_valid else 'Invalid'}")

if __name__ == "__main__":
    main()