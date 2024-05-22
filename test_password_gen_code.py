import unittest
from password_gen_code import generate_password, get_user_preferences


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password(self):
        password = generate_password()
        self.assertEqual(len(password), 12)

        password = generate_password(length=8, include_letters=False, include_digits=True,
                                     include_special_characters=True)
        self.assertTrue(any(char.isdigit() for char in password))

    def test_get_user_preferences(self):
        length, include_letters, include_digits, include_special_characters = get_user_preferences()
        self.assertIsInstance(length, int)
        self.assertIsInstance(include_letters, bool)
        self.assertIsInstance(include_digits, bool)
        self.assertIsInstance(include_special_characters, bool)


if __name__ == '__main__':
    unittest.main()
