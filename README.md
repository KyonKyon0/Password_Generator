# Password Manager

## Description
This is a simple Python-based password manager that allows users to:
1. Generate random passwords.
2. Store passwords in the `PLC_PSWD.json` file.
3. Search for passwords by ID.
4. Display saved passwords.

The program uses **JSON** to store data and includes input error handling to enhance security and ease of use.

## Features
- **Generate Password:** Creates a random 16-character password.
- **Save Password:** Generated passwords are stored based on the user ID.
- **Search Password:** Retrieves stored passwords by ID.
- **Menu Navigation:** Allows users to continue or exit the program.
- **Error Handling:** Manages incorrect inputs and missing JSON files.

## Prerequisites
Ensure you have Python installed before running the program.

## How to Use
1. Run the program using:
   ```bash
   python script.py
   ```
2. Choose from the available menu options:
   - `1` to generate a new password.
   - `2` to search for a password by ID.
   - `3` to exit the program.
3. Follow the on-screen instructions.

## Storage Format
Passwords are stored in `PLC_PSWD.json` in the following format:
```json
{
    "exampleID": "AbcD1234EfGh5678"
}
```

## Notes
- If the `PLC_PSWD.json` file is missing, the program will display an error message.
- Use an easy-to-remember ID for saving and retrieving passwords.
- Do not share your JSON file with others to maintain data security.

## License
This program is open-source and can be used or modified as needed.# Password_Generator
Program ini adalah pengelola kata sandi berbasis Python yang memungkinkan pengguna untuk menghasilkan kata sandi acak, menyimpannya dalam file JSON, dan mencarinya berdasarkan ID. Program memiliki menu interaktif untuk navigasi, menangani kesalahan input, serta memastikan keamanan dengan membersihkan layar setelah setiap operasi.
