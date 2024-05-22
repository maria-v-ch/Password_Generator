import string
import secrets


def generate_password(length=12, include_letters=True, include_digits=True, include_special_characters=True):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def get_user_preferences():
    print("We will now create a password together. It may have preferred length of symbols and be generated from "
          "letters, digits, special characters - it's up to you to set up the recipe: the ingredients and their "
          "amount.")
    length = int(input(f'Please specify password length followed by Enter: '))
    include_letters = (input("Can we choose symbols from letters? Type 'yes' or 'no' followed by Enter: ").lower() ==
                       'yes')
    include_digits = (input("Can we choose symbols from digits? Type 'yes' or 'no' followed by Enter: ").lower() ==
                      'yes')
    include_special_characters = (input("Can we choose symbols from special characters? Type 'yes' or 'no' followed by "
                                        "Enter: ").lower() == 'yes')
    return length, include_letters, include_digits, include_special_characters


def main():
    length, include_letters, include_digits, include_special_characters = get_user_preferences()
    password = generate_password(length, include_letters, include_digits, include_special_characters)
    print(f'Your new password: {password}')


if __name__ == '__main__':
    main()
