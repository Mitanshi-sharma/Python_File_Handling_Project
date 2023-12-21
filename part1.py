import re
from datetime import datetime

# def home_page():
#     while True:
#         print("There are multiple functions here to perform.")
#         print("1. login.")
#         print("2. Register.")
#         print("3. quite.")
#         action = input("Enter your action: ")
        
        
#         if action== '1':
#             login_user()
#         elif action=='2':
#             register_user()
#         elif action=='3':
#             break 
#         else:
#             print("Invalid choice. Please try again.")
# home_page()


def valid_username(name):
    
    if(len(name)<5):
        print("false")
        return False
    
    p =  re.search('[a-zA-Z]',name)
    special_char =  re.search('[@_!$%^&*()?/|\}{;:~#]',name)
    
    if(p==None or special_char!=None or re.search(r'^[A-Za-z]',name)==None):
        #print("False")
        return False
    else:
        #print("True")  
        return True  
    
        

def valid_password(password):
        if(len(password)<5):
            print("False")
            return False
        #return
        p =  re.search('[a-z]',password)
        q= re.search('[0-9]',password)
        r= re.search('[A-Z]',password)
        special_char =  re.search('[@_!$%^&*()?/|\}{;:~#]',password)
    
        if(p==None or q==None or r == None or special_char!=None or re.search(r'^[A-Za-z]',password)==None):
            #print("not valid")
            return False
        else:
            #print("True")   
            return True 





def username_exists(username):
    with open('user_info.txt', 'r') as file:
        for line in file:
            try:
                stored_username, _ = line.strip().split(',')
            except ValueError:
                continue
            if stored_username == username:
                return True
    return False

def check_password(username, password):
    with open('user_info.txt', 'r') as file:
        for line in file:
            try:
                stored_username, stored_password = line.strip().split(',')
            except ValueError:
                continue
            if stored_username == username and stored_password == password:
                return True
    return False

def send_message(sender, recipient, message):
    if not username_exists(recipient):
        print("Recipient does not exist. Cannot send message.")
        return False

    current_time = datetime.now().strftime('%m/%d/%Y %H:%M:%S')

    sender_chat_file = f'messages/{sender}.txt'
    with open(sender_chat_file, 'a') as sender_file:
        sender_file.write(f'{recipient}|{current_time}|{message}\n')

    messages_filename = f'messages/{recipient}.txt'
    with open(messages_filename, 'a') as messages_file:
        messages_file.write(f'{sender}|{current_time}|{message}\n')

    print("Message sent successfully.")
    return True




def register_user():
    print("\nRegister User:")
    
    # Get username and password from the user
    new_username = input("Enter a username: ")
    new_password = input("Enter a password: ")

    # Validate username and password
    if not valid_username(new_username):
        print("Invalid username. Please choose a valid username.")
        return

    if not valid_password(new_password):
        print("Invalid password. Please choose a valid password.")
        return

    # Check if the username already exists
    if username_exists(new_username):
        print("Username already taken. Please choose a different username.")
        return

    # If all checks pass, add the user to the system
    with open('user_info.txt', 'a') as file:
        file.write(f'{new_username},{new_password}\n')
        
    messages_filename = f'messages/{new_username}.txt'
    with open(messages_filename, 'w') as messages_file:
        send_message('admin', new_username, 'Welcome to your account')    

    print("User registered successfully!")

# Example usage:
# register_user()


def login_user():
    print("\nLogin User:")
    
    # Get username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match the data in user_info.txt
    if check_password(username, password):
        print("Login successful! Welcome, {}!".format(username))
        user_menu(username)  # Redirect to user menu
    else:
        print("Login failed. Incorrect username or password.")

# Sample implementation of read_messages, send_message, delete_messages
def print_messages(username):
    messages_filename = f'messages/{username}.txt'

    try:
        with open(messages_filename, 'r') as messages_file:
            messages = messages_file.readlines()

        if not messages:
            print("No messages in your inbox")
        else:
            for idx, message in enumerate(messages, start=1):
                sender, timestamp, content = message.strip().split('|')
                print(f"Message #{idx} received from {sender}")
                print(f"Time: {timestamp}")
                print(content)
                print()
    except FileNotFoundError:
        print(f"No messages found for {username}")

# def send_message(sender, recipient, message):
#     if not username_exists(recipient):
#         print("Recipient does not exist. Cannot send message.")
#         return False

#     current_time = datetime.now().strftime('%m/%d/%Y %H:%M:%S')

#     sender_chat_file = f'messages/{sender}.txt'
#     with open(sender_chat_file, 'a') as sender_file:
#         sender_file.write(f'{recipient}|{current_time}|{message}\n')

#     messages_filename = f'messages/{recipient}.txt'
#     with open(messages_filename, 'a') as messages_file:
#         messages_file.write(f'{sender}|{current_time}|{message}\n')

#     print("Message sent successfully.")
#     return True


def  delete_messages(username):
    messages_filename = f'messages/{username}.txt'

    try:
        with open(messages_filename, 'w') as messages_file:
            # Truncate the file, effectively erasing all data
            pass
        print(f"All messages for {username} have been deleted.")
    except FileNotFoundError:
        print(f"No messages found for {username}")

# Example usage:
#delete_messages(input("Enter username to delete all his messages: "))

def home_page():
    while True:
        print("There are multiple functions here to perform.")
        print("1. login.")
        print("2. Register.")
        print("3. quite.")
        action = input("Enter your action: ")
        
        
        if action== '1':
            login_user()
        elif action=='2':
            # new_username = input("Enter a username: ")
            # new_password = input("Enter a password: ")
            register_user()
        elif action=='3':
            break 
        else:
            print("Invalid choice. Please try again.")


def user_menu(username):
    while True:
        print("\nUser Menu - {}".format(username))
        print("1. Read Messages")
        print("2. Send Message")
        print("3. Delete Messages")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_messages(username)
        elif choice == '2':
            recipient = input("Enter recipient username: ")
            message = input("Enter your message: ")
            send_message(username, recipient, message)
        elif choice == '3':
            delete_messages(username)
        elif choice == '4':
            print("Logout successful. Returning to the main menu.")
            break  # Break out of the user menu loop and return to the main menu
        else:
            print("Invalid choice. Please try again.")

# Example usage:
# Assuming you have implemented the necessary functions like check_password
home_page()
#login_user()
# user_menu(username)