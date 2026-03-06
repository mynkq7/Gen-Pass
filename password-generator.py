# Password Generator 

# Importing modules.
import secrets # for genrating random numbers and strings
import hashlib # for hashing 
import json # for storing data in json format 
import string # for generating random characters

# name of the tool 
tool_name = "Gen-Pass"

# Printing welcome message and instructions to the user
print(f"Welcome to {tool_name} - Your unique password generator!")
print("Press enter without typing anything to quit.")

# user input for password length plus while loop to keep asking until user wants to quit or enters valid input .
while True:
 pass_length = (input("Enter the desired length of your password:...")).strip() # removing leading and trailing white spaces


# if user input is empty then it will show the printed message and quit the program.
 if pass_length == "":
  print("Empty input, quitting the program...")
  break

# if user input is not a digit then it will show the printed message.
 elif not pass_length.isdigit():
  print("Invalid input, please enter a valid number for password length.")
 
 # now it has no options but to genrate the password if the input is valid.
 elif pass_length.isdigit():
  length = int(pass_length) # coverting user input to integer. 
  char = string.ascii_letters + string.digits + string.punctuation # character pool. 
  password = "".join(secrets.choice(char) for _ in range(length)) # genrating the password.
  print(f"Generated Password: {password}") # Printing the generated password to the user.


  # Hashing the Password 
  hashed_password = hashlib.sha256(password.encode()).hexdigest() # hashed using sha256 algorithm, converted to hexadecimal format.


  # storing the password in json file 
  # asking for user input to save the password or not, if yes then it will ask for a label and store the password with the label in json file.
  ask = input("Do you want to save this password? (yes/no):").strip().lower() # removed spaces, converted to lower case

  if ask == "no":
    print("Password not saved.")

  elif ask == "yes":
    label = input("Enter a label for this password (e.g., 'Email', 'Bank', etc.):").strip()

    # creating dictionary to store label and hashed password
    data = {label: hashed_password}

    try:
      with open("passwords.json", "r") as file:
        existing_data = json.load(file)
    except FileNotFoundError:
      existing_data = {}

    existing_data.update(data)

    with open("passwords.json", "w") as file:
      json.dump(existing_data, file, indent=4)

    print("Password saved successfully.")