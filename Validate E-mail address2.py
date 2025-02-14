import re


def is_valid_email(email):
    # Strict regex pattern enforcing all validation rules
    pattern = r"^(?!.*\.\.)[a-zA-Z0-9][a-zA-Z0-9._%+-]*[a-zA-Z0-9]@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"

    # Check basic format using regex
    if not re.match(pattern, email):
        return False

    # Ensure there is only **one `@` symbol**
    if email.count("@") != 1:
        return False

    # Split email into username and domain
    username, domain = email.split("@")

    # Ensure username does NOT start or end with a dot, hyphen, or special character
    if username.startswith(".") or username.startswith("-") or username.endswith(".") or username.endswith("-"):
        return False

    # Ensure domain does NOT start or end with a hyphen
    if domain.startswith("-") or domain.endswith("-"):
        return False

    #Ensure domain does NOT contain consecutive dots
    if ".." in domain:
        return False

    #Extract TLD (Top-Level Domain) and validate length (2 to 4 characters)
    tld = domain.split(".")[-1]
    if len(tld) < 2 or len(tld) > 4:
        return False

    #Allow only specific valid TLDs
    valid_tlds = {"com", "org", "net", "edu", "gov", "mil", "int", "co", "uk", "in", "us", "fr", "de", "au", "ca", "jp"}
    if tld not in valid_tlds:
        return False

    return True


email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid Email!")
else:
    print("Invalid Email!")
