

"""
@author : Ranjit
Created Date : 28/02/2021
Updated Date : 28/02/2021
Title : User Registration Form Using Regex
"""
from logger import Logger
import re
logger = Logger('logfile').get()

def validate_userName(user_name):
    """This function is used for the validate the user first name"""
    try:
        regex = '^[A-Z]{1}[a-z]{2}'
        if re.findall(regex,user_name):
            print("validte")
            return True
        else:
            None
    except ValueError as e:
        logger.error(str(e))
    except Exception  as e:
        logger.error(str(e))    

def Validate_lastName(last_name):
    """This function is used for the validate the user last name"""
    try:
        regex = '^[A-Z]{1}[a-z]{2}'
        if re.findall(regex,last_name):
            print("validte")
            return True
        else:
            return None
    except ValueError as e:
        logger.error(str(e))
    except Exception  as e:
        logger.error(str(e))

def check_email(email):
    """This function is used for the validate the user email"""
    try:
        regex ="^[a-zA-Z0-9]+([._+-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.][a-zA-Z]{2,3}){1,2}$"  
        if(re.search(regex,email)):  
            print("validte")
            return True  
        else:  
            return None  
    except ValueError as e:
        logger.error(str(e))
    except Exception  as e:
        logger.error(str(e)) 



if __name__ == '__main__':
    try:
        user_name = input("Please Provide user_name :")
        validate_userName(user_name)
        last_name = input("Please Provide Last name :")
        Validate_lastName(last_name)
        email = input("Please Provide eamil :")
        check_email(email)
        mobile= input("Please Provide mobile number :")
        check_mobileNumber(mobile)
        password= input("Please Provide password :")
        check_password(password)
    except Exception as e:
        logger.error(e)
