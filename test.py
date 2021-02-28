import unittest
from user_registration import (
                            validate_userName,
                              Validate_lastName,
                              check_email,
                              check_mobileNumber,
                              check_password
                            )

class UserTestCase(unittest.TestCase):

    def test_for_Checking_user_first_name(self):
        """checking the user first name """
        self.assertEqual(validate_userName('Ranjit'),True)
        self.assertEqual(validate_userName('ranjit'),None)
        self.assertTrue(validate_userName('Ranjit'),True)
        self.assertNotEqual(validate_userName('Ranit'),None)
        self.assertFalse(validate_userName('ram'),None)

    def test_for_Checking_user_last_name(self):
        """checking the user last name """
        self.assertEqual(Validate_lastName('Jadhav'),True)
        self.assertEqual(Validate_lastName('ranjit'),None)
        self.assertTrue(Validate_lastName('Ranjit'),True)
        self.assertNotEqual(Validate_lastName('Ranit'),None)
        self.assertFalse(Validate_lastName('ram'),None)

    def test_for_Checking_user_email(self):
        """checking the user email"""
        self.assertEqual(check_email('ranjit@yopmial.com'),True)
        self.assertEqual(check_email('ranjit.jadhav@yopmail.com'),True)
        self.assertTrue(check_email('ranjit@yopmial.com'),True)
        self.assertNotEqual(check_email('ranit@yopmail.com'),None)
        self.assertFalse(check_email('ram@'),None)

    def test_for_Checking_user_mobile_number(self):
        """checking the user last name """
        self.assertEqual(check_mobileNumber('917276341996'),True)
        self.assertEqual(check_mobileNumber('91 7276341996'),None)
        self.assertTrue(check_mobileNumber('917276341996'),True)
        self.assertNotEqual(check_mobileNumber('Ran12334it'),True)
        self.assertFalse(check_mobileNumber('ram'),None)

    def test_for_Checking_user_password(self):
        """checking the user last name """
        self.assertEqual(check_password('Ranjit@123'),True)
        self.assertEqual(check_password('Ranjit'),None)
        self.assertTrue(check_password('Ranjit@123'),True)
        self.assertNotEqual(check_password('Ranit@123'),None)
        self.assertFalse(check_password('ram'),None)

if __name__ == '__main__':
    unittest.main()
