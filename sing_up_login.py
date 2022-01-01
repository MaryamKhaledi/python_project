import logging_file
import hashlib
import binascii
import os
import re
import file_handler
from datetime import datetime, time


class User:
    """
    This class checks the people who log in for the correct name, the correct password, the existence of the username,
    the creation of the user page, and so on. And creates a user page if needed.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.lock = False

    def validation_user(self):
        """
        Checks the validity of the username and its compliance with the standard.
        """
        regex = '^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$'
        pattern = re.compile(regex)
        if re.search(pattern, self.username):
            print('Valid username')
            logging_file.info_logger.info('Username is valid')
            return True
        else:
            print("Sorry! invalid username")
            logging_file.info_logger.info('Username is not valid')
            return False

    def validation_password(self):
        """
        Checks the validity of the password and its compliance with the standard.
        """
        regex = '[A-Za-z0-9@#$%^&+=]{8,}'
        pattern = re.compile(regex)
        if re.search(pattern, self.password):
            print('Valid password')
            return True
        else:
            print("Sorry! invalid password")
            return False

    @staticmethod
    def validation_address_email(email):
        """
        Checks the validity of the address email and its compliance with the standard.
        """
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3}[.com])+$'
        pattern = re.compile(regex)
        if re.search(pattern, email):
            print('Email is correct.')
            return True
        else:
            print("invalid password")
            return False

    def existence_user(self):
        """
        Checks if the user is in the users file or not
        """
        open_file = file_handler.FileHandler("login_users.csv")
        read_file = open_file.read_file()
        for row in read_file:
            if row["username"] == self.username:
                logging_file.info_logger.info('This username was in our file.')
                return True
        else:
            logging_file.info_logger.info('This username did not exist in our file.')
            return False

    def hash_password(self):
        """
        Hash a password for storing.
        At this point, the password that has already been verified is encrypted.
        """
        check_password = self.password.encode()
        hash_p = hashlib.sha3_512(check_password).hexdigest()
        return hash_p

    def check_locked(self):
        """
        Check locked users
        """
        open_file = file_handler.FileHandler("locked_users.csv")
        read_file = open_file.read_file()
        for row in read_file:
            if row["username"] == self.username:
                return True
        else:
            return False

    def lock_account(self):
        """
        This method locks the user's account for up to 2 hours.
        """
        now = datetime.now()
        time_now = time(now.hour, now.minute, now.second)
        time_now1 = datetime.combine(now.date(), time_now)
        open_file = file_handler.FileHandler("locked_users.csv")
        write_file = open_file.write_file({'username': self.username, 'time_locked': time_now1})

    def unlock_account(self):

        open_file = file_handler.FileHandler("locked_users.csv")
        read_file = open_file.read_file()
        for row in read_file:
            if row["username"] == self.username:
                time_lock_account = row["time_locked"]
                now = datetime.now()
                time_unlock_account = time(now.hour + 2, now.minute, now.second)
                time_unlock_account = datetime.combine(now.date(), time_unlock_account)
                if time_lock_account >= time_unlock_account:
                    return True
                else:
                    return False
            else:
                return False

    def matching_user_password(self, provided_password):
        """
        Match the name with the password and return the word "True" if it is correct and
        the word "False" if it was incorrect.
        """
        open_file = file_handler.FileHandler("login_users.csv")
        read_file = open_file.read_file()
        for row in read_file:
            if row["username"] == self.username:
                if row["hash_password"] == provided_password:
                    logging_file.info_logger.info('The name matched the password')
                    return True
                else:
                    logging_file.info_logger.info('The name did not match the password')
                    return False

    def add_new_user(self, hash_new_password):
        """
        In this method, the person who has just registered is added to the user file and his / her own page is created.
        """
        open_file1 = file_handler.FileHandler("login_users.csv")
        write_file = open_file1.write_file({'username': self.username, 'hash_password': hash_new_password})

        open_file2 = file_handler.FileHandler("Desktop_users\\" + self.username + "_inbox.csv")
        write_inbox = open_file2.write_new_inbox()

        open_file3 = file_handler.FileHandler("Desktop_users\\" + self.username + "_draft.csv")
        write_draft = open_file3.write_new_draft()

        open_file4 = file_handler.FileHandler("Desktop_users\\" + self.username + "_sent.csv")
        write_sent = open_file4.write_new_sent()
