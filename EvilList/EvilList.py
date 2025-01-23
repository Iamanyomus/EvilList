import os
import random
import time
from colorama import Fore, Style, init
from tqdm import tqdm


init(autoreset=True)

def print_banner():
    print("\033[1;31m" + "="*50)
    print("\033[1;31m" + " " * 10 + """
    _______    ________    __    _______________
   / ____/ |  / /  _/ /   / /   /  _/ ___/_  __/
  / __/  | | / // // /   / /    / / \__ \ / /   
 / /___  | |/ // // /___/ /____/ / ___/ // /    
/_____/  |___/___/_____/_____/___//____//_/     
                                                
""" + " " * 10)
    print("\033[1;31m" + "="*50)
    print("\033[1;31m" + "         \033[5mWELCOME TO THE EVILLIST TOOL!\033[0m" + "\033[0m")

def generate_variations(word):
    variations = set()
    word_length = len(word)
    
    
    for i in range(word_length):
        for j in range(i + 1, word_length + 1):
            variation = word[:i].lower() + word[i:j].upper() + word[j:].lower()
            variations.add(variation)
    
    return variations

def generate_wordlist(allow_symbols=False, allow_numbers=False):
    victim_first_name = input(f"{Fore.BLUE}\033[1mFirst name: {Style.RESET_ALL}")
    victim_last_name = input(f"{Fore.BLUE}\033[1mLast name: {Style.RESET_ALL}")
    victim_dob_day = input(f"{Fore.BLUE}\033[1mDOB (day): {Style.RESET_ALL}")
    victim_dob_month = input(f"{Fore.BLUE}\033[1mDOB (month): {Style.RESET_ALL}")
    victim_dob_year = input(f"{Fore.BLUE}\033[1mDOB (year): {Style.RESET_ALL}")
    special_words = [word.strip() for word in input(f"{Fore.BLUE}\033[1mSpecial words (comma-separated): {Style.RESET_ALL}").split(',')]
    hobbies = [word.strip() for word in input(f"{Fore.BLUE}\033[1mHobbies (comma-separated): {Style.RESET_ALL}").split(',')]

    base_wordlist = [
        victim_first_name,
        victim_last_name,
        victim_first_name + victim_last_name,
        victim_last_name + victim_first_name,
        victim_first_name + victim_dob_day,
        victim_first_name + victim_dob_month,
        victim_first_name + victim_dob_year,
        victim_last_name + victim_dob_day,
        victim_last_name + victim_dob_month,
        victim_last_name + victim_dob_year,
    ] + special_words + hobbies

    wordlist = set(base_wordlist)
    symbols = "!@#$%^&*."

    print(f"{Fore.RED}\033[1mPlease wait... Making wordlist...{Style.RESET_ALL}")
    time.sleep(1)  

    for word in tqdm(list(wordlist), desc="Generating variations"):
        wordlist.update(generate_variations(word))
        if allow_symbols:
            for symbol in symbols:
                for i in range(len(word)):
                    wordlist.update(generate_variations(word[:i] + symbol + word[i:]))
                    wordlist.update(generate_variations(word[:i] + symbol + word[i:] + symbol))
        if allow_numbers:
            for _ in range(100):  
                number = str(random.randint(0, 9999))
                wordlist.update(generate_variations(word + number))
                for i in range(len(word)):
                    wordlist.update(generate_variations(word[:i] + number + word[i:]))
                    wordlist.update(generate_variations(word[:i] + number + word[i:] + number))

    
    os.makedirs("WordLists", exist_ok=True)

    
    with open(f"WordLists/{victim_first_name}_wordlist.txt", "w") as file:
        for word in sorted(wordlist):
            file.write(word + "\n")

    
    print(f"{Fore.GREEN}\033[1m\nWordlist saved to WordLists/{victim_first_name}_wordlist.txt{Style.RESET_ALL}")

def show_credits():
    print("\n" + "-"*100)
    print("\033[1;36m" + "\033[1m                      CREDITS                       ".center(100) + "\033[0m")
    print("-"*100)
    print("\033[1;35m\033[1mTool owned by: Harshy(DaddyDark)".ljust(100) + "\033[0m")
    print("\033[1;33m\033[1mSpecial thanks to all contributors.".ljust(100) + "\033[0m")
    print("\n\033[1;32m\033[1mCopyright 2025 - All Rights Reserved.\033[0m")
    print("\033[1;31m\033[1mThis tool is provided for educational purposes only.\033[0m")
    print("\033[1;31m\033[1mUnauthorized use may violate laws in your jurisdiction.\033[0m")
    print("-"*100)
    time.sleep(20)
    main_menu()

def main_menu():
    while True:
        os.system('clear')
        print_banner()
        print(f"{Fore.RED}\033[1mMain Menu{Style.RESET_ALL}")
        print(f"{Fore.BLUE}\033[1m1. Generate Wordlist{Style.RESET_ALL}")
        print(f"{Fore.BLUE}\033[1m2. Wordlist with Numbers{Style.RESET_ALL}")
        print(f"{Fore.BLUE}\033[1m3. Wordlist with Symbols{Style.RESET_ALL}")
        print(f"{Fore.BLUE}\033[1m4. Wordlist with Numbers & Symbols{Style.RESET_ALL}")
        print(f"{Fore.BLUE}\033[1m5. Credits{Style.RESET_ALL}")
        print(f"{Fore.BLUE}\033[1m6. Exit{Style.RESET_ALL}")

        choice = input(f"{Fore.RED}\033[1mEnter your choice: {Style.RESET_ALL}")

        if choice == '1':
            generate_wordlist()
        elif choice == '2':
            generate_wordlist(allow_numbers=True)
        elif choice == '3':
            generate_wordlist(allow_symbols=True)
        elif choice == '4':
            generate_wordlist(allow_symbols=True, allow_numbers=True)
        elif choice == '5':
            show_credits()
        elif choice == '6':
            print(f"{Fore.RED}\033[1mExiting...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}\033[1mInvalid choice, please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}\033[1mExiting...{Style.RESET_ALL}")