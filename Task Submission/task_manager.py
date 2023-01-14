# Defining a boolean value for the login credentials.
login = True

# Defining empty dictionaries from the user.txt and tasks.txt files.
# The dictionaries will be used to locate the usernames and passwords.
user_dict = {}
pass_dict = {}

# After opening the user.txt file we can add the usernames and passwords
# To their respective dictionaries.
with open("user.txt", "r+") as f:
    for line in f:
        # First we strip the whitespace and newline character and then split the comma.
        login_items = line.strip("\n").split(", ")
        # Then we define keys and values for the dictionaries.
        user_dict[login_items[0]] = login_items[1]
        pass_dict[login_items[1]] = login_items[0]

while login:
    # We ask the user to enter a username and password
    username: str = input("Please enter your username: ")
    password = input("Please enter your password: ")
    # If they match the username and password saved in the user.txt file.
    # The user can log in.
    if username in user_dict and password == user_dict[username]:
        login = False

while True:
    # If the user logged in is the admin
    # They are shown a menu with options
    # To add a new user and view statistics
    if "admin" == username:
        menu = input("""Select one of the following Options below:
r - Register a new user
a - Adding a task
va - View all tasks
vm - view my tasks
s - Show statistics
e - Exit
: """).lower()

    # If the user is not the admin
    # They are shown a different menu
    else:
        menu = input("""Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my tasks
e - Exit
: """).lower()
    print("")

    # If the user selects "Register a new user"
    # The program will check that the user is the admin.
    if menu == "r" and username == "admin":
        with open("user.txt", "a+") as f:
            # Next I ask the admin to enter a username.
            # Then I ask the admin to enter a password and confirm it.
            new_username = input("Please enter a username: ").lower()
            print("")
            new_password = input("Please enter a password: ")
            password_confirmation = input("Please enter your password again: ")
            # If the password and the confirmed password match
            # The program writes the username and password to the user.txt file on a new line.
            if new_password == password_confirmation:
                f.write("\n")
                f.write(f"{new_username}, {new_password}")

        while new_password != password_confirmation:
            # If the passwords do not match, the admin is asked to re-enter them until they do match
            # Once they match, the program writes the new information to the file
            print("Your passwords do not match. Please try again")
            new_password = input("Please enter a password: ")
            password_confirmation = input("Please enter your password again: ")
            if new_password == password_confirmation:
                f.write("\n")
                f.write(f"{new_username}, {new_password}")
                print(menu)

                # This next section of code deals with the user adding a new task.
    elif menu == "a":
        # First we open the tasks.txt file and use the append function
        # To avoid overwriting the existing tasks.
        with open("tasks.txt", "a+") as f:
            # Then we ask the user to input the details of the task.
            username = input("Please enter the username of the person to whom you wish to assign the task: ")
            task_title = input("Please enter the title of the task: ")
            task_descr = input("Please enter a description of the task: ")
            task_date = input("When is the task due? ")
            task_complete = "No"
            # Once the user has entered the details of the task
            # We write the task on a single new line in the file.
            f.write("\n")
            f.writelines(f"{username}, {task_title}, {task_descr}, {task_date}, {task_complete}")
            print(menu)

            # This next section of code deals with the user wanting to view all existing tasks.
    elif menu == "va":
        # First we open the tasks.txt file and read it.
        with open("tasks.txt", "r+") as f:
            # Then we create a list out of each line in the file.
            # We strip the white lines and split the commas.
            # We use list comprehension for this.
            lines = [line.strip().split(", ") for line in f]
            for list in lines:
                # After the lists have been created
                # We print the information in an easy-to-read format.
                print(f"""
Task:\t{list[1]}
Assigned to:\t{list[0]}
Due Date:\t{list[3]}
Task Complete?\t{list[4]}
Task Description:\t{list[2]}""")
            print(menu)

    # This next section of code deals with the user
    # Only wanting to view the tasks assigned to them
    elif menu == "vm":
        with open("tasks.txt", "r+") as f:
            lines = [line.strip().split(", ") for line in f]
            # The code is the same as in the "view all tasks" blo ck above
            # But we also check which user is logged in
            # So that we only show that user their tasks
            for list in lines:
                if username == list[0]:
                    print(f"""
Task:\t{list[1]}
Assigned to:\t{list[0]}
Due Date:\t{list[3]}
Task Complete?\t{list[4]}
Task Description:\t{list[2]}""")
            print(menu)

    elif menu == "s" and username == "admin":
        # First we define empty counters for the totals and set the to 0
        total_users = 0
        total_tasks = 0

        # Open user.txt file
        with open("user.txt", "r") as f1:
            # Using a for loop we read each line in the file
            for line in f1:
                # Then we increase the counter each time
                total_users += 1
            # Then print the total users
            print(f"There are {total_users} users.")

        # Open user.txt file
        with open("tasks.txt", "r+") as f2:
            # Using a for loop we read each line in the file
            for line in f2:
                # Then we increase the counter each time
                total_tasks += 1
            # Then print the total users
            print(f"There are {total_tasks} tasks.")
        print(menu)

    # If the user chooses to exit the program,
    elif menu == "e":
        print("Goodbye.")
        # The program says goodbye to the user
        # And exits using the exit function.
        exit()

    # If the user does not enter a valid choice of option
    # They are asked to try again.
    else:
        print("You have made an invalid choice, please try again.")