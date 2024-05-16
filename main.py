import string
import secrets


def generate_password(length=12, include_letters=True, include_digits=True, include_special_symbols=True):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_symbols:
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def get_user_preferences():
    print("Let's set up password features.")
    length = int(input(f'Please specify password length: '))
    include_letters = input("If you want the password to contain letters then enter '+': ") == '+'
    include_digits = input("If you want the password to contain digits then enter '+': ") == '+'
    include_special_symbols = input(f"If you want the password to contain special symbols then enter '+': ") == '+'
    return length, include_letters, include_digits, include_special_symbols


def main():
    length, include_letters, include_digits, include_special_symbols = get_user_preferences()
    password = generate_password(length, include_letters, include_digits, include_special_symbols)
    print(f'Your new password: {password}')


if __name__ == '__main__':
    main()
