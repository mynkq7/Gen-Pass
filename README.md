# Gen Pass

A simple password generator that takes the desired password length from the user. Based on the provided length, it generates a strong random password, converts it into a hash value, and stores the hashed password in a JSON file with a user-provided label.

## Features

* Generates strong random passwords
* Uses secure randomness with `secrets`
* Hashes passwords using `SHA-256`
* Stores hashed passwords in a JSON file
* Allows labeling passwords for easy identification

## Modules Used

* `secrets`
* `hashlib`
* `json`
* `string`

## How to Run

Run the script using Python from the terminal:

```bash
python Gen-Pass.py
```

Make sure Python 3 is installed on your system before running the script.

## Example

```
Enter the desired length of your password: 12
Generated Password: 8@fD!2kLp#9Q

Do you want to save this password? (yes/no): yes
Enter a label: Email
```
