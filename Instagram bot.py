from instabot import Bot


# Function to display menu options
def display_menu():
    print("\nChoose an action:")
    print("1. Follow a user")
    print("2. Upload a photo")
    print("3. Unfollow a user")
    print("4. Send a message")
    print("5. Get follower count and details")
    print("6. Get following info")
    print("7. Exit")


# Function to execute chosen menu option
def perform_action(choice, bot):
    if choice == "1":
        following = input("Enter the username you want to follow: ")
        bot.follow(following)
        print(f"Successfully followed {following}")

    elif choice == "2":
        photo = input("Enter the photo path you want to upload (use correct slashes): ")
        bot.upload_photo(photo)
        print("Photo uploaded successfully")

    elif choice == "3":
        unfollowing = input("Enter the username you want to unfollow: ")
        bot.unfollow(unfollowing)
        print(f"Successfully unfollowed {unfollowing}")

    elif choice == "4":
        count = int(input("Enter the number of users to send messages to: "))
        recipients = []
        for i in range(count):
            user = input(f"Enter username {i + 1}: ")
            recipients.append(user)
        message = input("Enter the message you want to send: ")
        bot.send_message(message, recipients)
        print(f"Message sent to {', '.join(recipients)}")

    elif choice == "5":
        follower_count = input("Enter the username to check followers: ")
        followers = bot.get_user_followers(follower_count)
        print(f"{follower_count} has {len(followers)} followers.")

        # Ask user how many followers to display
        num_followers = int(input("Enter the number of followers to display: "))
        print(f"Showing {min(num_followers, len(followers))} followers:")

        for follower in followers[:num_followers]:  # Display user-specified number of followers
            print(bot.get_user_info(follower))

    elif choice == "6":
        following_info_user = input("Enter the username to check following info: ")
        following_info = bot.get_user_following(following_info_user)
        print(f"{following_info_user} follows {len(following_info)} users.")

        # Ask user how many followings to display
        num_following = int(input("Enter the number of followings to display: "))
        print(f"Showing {min(num_following, len(following_info))} followings:")

        for following in following_info[:num_following]:  # Display user-specified number of followings
            print(bot.get_user_info(following))

    elif choice == "7":
        print("Exiting program")
        return False

    else:
        print("Invalid choice. Please enter a valid option.")

    return True  # Continue loop


# Main program
def main():
    # Instagram login
    bot = Bot()
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    bot.login(username=username, password=password)

    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        continue_running = perform_action(choice, bot)

        if not continue_running:
            break

        # Ask user if they want to continue
        repeat = input("\nDo you want to perform another action? (Y/N): ").strip().lower()
        if repeat not in ["y", "yes"]:
            print("Exiting program")
            break

    bot.logout()


# Run the program
if __name__ == "__main__":
    main()
