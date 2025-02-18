import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

email = input("Enter your email id: ")
password = input("Enter your password: ")

try:
    ob.login(email, password)
    print("Login successful")
except s.SMTPAuthenticationError:
    print("Login failed. Check your email and password.")
    exit()

while True:
    subject = input("Enter the subject: ")
    body = input("Enter the body of the mail: ")

    while True:
        to = input("Enter the recipient's email: ")
        ob.sendmail(email, to, f"Subject: {subject}\n\n{body}")
        print(f"Email sent to {to} successfully!")

        repeat = input("Do you want to send another email? (Y/N): ").strip().lower()
        if repeat in ["n", "no"]:
            break

    exit_choice = input("Do you want to quit the program? (Y/N): ").strip().lower()
    if exit_choice in ["n", "no"]:
        print("Exiting program...")
        break

ob.quit()

