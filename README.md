# EvilList

EvilList is a tool for generating customized wordlists based on user input. It can create variations of words with symbols and numbers, making it useful for various purposes such as password generation and testing.

## Features

- Generate wordlists based on user-provided names, dates, special words, and hobbies.
- Create variations of words with uppercase and lowercase combinations.
- Optionally include symbols and numbers in the wordlists.
- Save generated wordlists to a file.

## Requirements

- Python 3.x
- `colorama` library
- `tqdm` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Iamanyomus/EvilList/
    cd EvilList/EvilList/
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script:
```sh
python EvilList.py
```

Follow the on-screen prompts to generate your wordlist. You can choose to include symbols and/or numbers in the wordlist.

### Example

```sh
First name: John
Last name: Doe
DOB (day): 01
DOB (month): 01
DOB (year): 1990
Special words (comma-separated): password , secret
Hobbies (comma-separated): reading , hiking
```

The generated wordlist will be saved in the [`WordLists`](WordLists ) directory with the filename `John_wordlist.txt`.

## How It Works

1. **Input Collection**: The script collects various inputs from the user, including names, dates, special words, and hobbies.
2. **Base Wordlist Generation**: It creates a base wordlist using the provided inputs.
3. **Variations Generation**: The script generates variations of each word by changing the case of letters and optionally adding symbols and numbers.
4. **Saving the Wordlist**: The final wordlist is saved to a file in the [`WordLists`](WordLists ) directory.

## Main Menu Options

1. **Generate Wordlist**: Creates a wordlist based on the provided inputs without adding any symbols or numbers.
2. **Wordlist with Numbers**: Generates a wordlist and includes variations with random numbers.
3. **Wordlist with Symbols**: Generates a wordlist and includes variations with special symbols.
4. **Wordlist with Numbers & Symbols**: Generates a wordlist and includes variations with both random numbers and special symbols.
5. **Credits**: Displays the credits for the tool.
6. **Exit**: Exits the program.

## Comparison with CUPP

EvilList offers several advantages over CUPP (Common User Passwords Profiler):

- **More Options**: EvilList provides more customization options, including the ability to add symbols and numbers to the wordlist.
- **Ease of Use**: EvilList features a user-friendly interface with clear prompts, making it easier to use compared to CUPP.
- **Fully GUI**: EvilList has a fully graphical user interface, enhancing the user experience.
- **Larger Wordlists**: EvilList can generate wordlists with up to 1 billion passwords, whereas CUPP has limitations on the size of the wordlists it can generate.
- **Better Aesthetics**: EvilList has a more visually appealing design, making it more pleasant to use.

## Disclaimer

This tool is provided for educational purposes only. Unauthorized use may violate laws in your jurisdiction. Use it responsibly.

## Warning for Phone Users

Generated wordlists can be very large, especially when including symbols and numbers. Be cautious when using this tool on a phone, as it may consume significant storage space and processing power.

## Screenshots

![Image](https://github.com/user-attachments/assets/9e9441dc-f016-4aae-bfb7-0a39feb2fc63)


![Image](https://github.com/user-attachments/assets/fac599ea-7bd8-4a28-a6a9-131dee9f78e5)


![Image](https://github.com/user-attachments/assets/e111ddf5-4176-4ce4-b070-75280bc236c7)


## Credits

- Tool owned by: Harshy (DaddyDark)
- Special thanks to all contributors.

## License

This tool is provided for educational purposes only. Unauthorized use may violate laws in your jurisdiction.
```
https://github.com/Iamanyomus/EvilList
