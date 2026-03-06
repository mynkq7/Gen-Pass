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
