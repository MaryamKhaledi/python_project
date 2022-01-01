import logging_file
import hashlib
from sing_up_login import User
from message_box import *
from tabulate import tabulate


def user_system(username):
    """
    This method is for users who successfully log in and have a desktop.
    """
    while True:
        try:
            logged_user = int(input('Dear user, what do you want to do?\n1)I just wanted to be online!'
                                    '\n2)I want to check the `Inbox` folder.\n3)I want to check the `Draft` folder.'
                                    '\n4)I want to check the `Sent` folder\n5)I want to send a message to someone.'
                                    '\n6)Exit\n--->>>'))
            if logged_user == 1:
                print('Have fun ! *☻* ')
            elif logged_user == 2:
                create_object = Messages("Desktop_users\\" + username + "_inbox.csv",
                                         "inbox_message")
                print(create_object.number_message())
                create_object1 = Inbox("Desktop_users\\" + username +
                                       "_inbox.csv", "inbox_message", "")
                list_contacts = create_object1.users_message()
                if len(list_contacts) > 0:
                    while True:
                        try:
                            question_from_user_1 = int(input("Want to see who sent the message??\n1)Yes\n2)No and exit"
                                                             "\nYour response: "))
                            if question_from_user_1 == 1:
                                # create_object1 = Inbox("Desktop_users\\" + username +
                                #                        "_inbox.csv", "inbox_message", "")
                                # list_contacts = create_object1.users_message()
                                # if len(list_contacts) > 0:
                                print("\n", tabulate(list_contacts,
                                                     headers=["Contacts", "time to receive", "Has_been_read"]))
                                while True:
                                    question_from_user_2 = input("\nWhich person's message would you like to read?"
                                                                 "\nEnter the name of the person you want : ")
                                    # create_object2 = Messages(received_messages, "users")
                                    create_object2 = Messages("Desktop_users\\" +
                                                              username + "_inbox.csv", "users")
                                    if create_object2.check_user(question_from_user_2):

                                        time_seen = create_object2.time_now()
                                        logging_file.info_logger.info(
                                            f"{username} in {time_seen} time read {question_from_user_2}'s message.")
                                        create_object3 = Inbox("Desktop_users\\" +
                                                               username + "_inbox.csv", "users", question_from_user_2)

                                        message_show = create_object3.show_message()
                                        print("\n", tabulate(message_show, headers=["Contact", "Message text"]))
                                        question_from_user_3 = input("\nDo you want to respond to her(his) message?"
                                                                     "\n1)Yes\n2)No\n3)exit\nYour response:")
                                        create_object3.update_seen(time_seen)
                                        if question_from_user_3 == "1":
                                            question_from_user_5 = input("Please enter your desired message:")
                                            writing_time = create_object2.time_now()
                                            create_object4 = Sent("", "", "Desktop_users\\" +
                                                                  username + "_sent.csv",
                                                                  "Desktop_users\\" +
                                                                  question_from_user_2 + "_inbox.csv")
                                            create_object4.reply_to_message(question_from_user_5, writing_time,
                                                                            question_from_user_2, username)
                                            logging_file.info_logger.info(f"The message was successfully sent from"
                                                                          f" {username} to {question_from_user_2}.")
                                            print(f"The message was successfully sent from {username} to "
                                                  f"{question_from_user_2}.")
                                            break
                                        # elif question_from_user_3 == "2" or question_from_user_3 == "3":
                                        #     break
                                        else:
                                            question_from_user_6 = input(
                                                "the dude! It is good not to waste time and if "
                                                "you have nothing to do,log out of the system."
                                                "Do you want to stay or do you want to go out?"
                                                "\n1)I stay\t\t2)I'm leaving"
                                                "\nEnter the option you want:")
                                            if question_from_user_6 == "1" or question_from_user_6 == "2":
                                                print("have a good time")
                                                break
                                            else:
                                                print(f"{username}, you answered the question incorrectly.")
                                                logging_file.warning_logger.error(f"{username} gave the wrong "
                                                                                  f"answer to the question.")

                                    elif not create_object2.check_user(question_from_user_2):
                                        print("Sorry, you entered the contact name incorrectly")
                                        logging_file.warning_logger.error(f"{username} entered the contact name "
                                                                          f"incorrectly")


                            elif question_from_user_1 == 2:
                                print("You did not want to see who sent you the message.\n")
                                break
                            elif str(logged_user).isdigit():
                                print("Dear audience, you have entered a number outside the range")
                                logging_file.warning_logger.error(f"{username} entered a number out of range")
                        except ValueError:
                            print("you must enter a integer!")
                            logging_file.warning_logger.error(f"Instead of selecting the numeric option, {username} "
                                                              f"unfortunately entered the string.")
                else:
                    print("You have not received a message yet.")

                while True:
                    msg = input("What are you going to do now? \n1)exit\n(Please enter only the option number)-->> ")
                    if msg == "1":
                        break
                    else:
                        logging_file.warning_logger.error(f"Instead of selecting the numeric option, {username} "
                                                          f"unfortunately entered the string.")
                        print("Please enter only the option number !")
                        continue

            elif logged_user == 3:
                create_object1 = Messages("Desktop_users\\" + username + "_draft.csv",
                                          "draft_message")
                number_messages = create_object1.number_message()
                print(number_messages)
                create_object2 = Draft("Desktop_users\\" + username +
                                       "_draft.csv", "draft_message")
                list_draft = create_object2.draft_message()
                if len(list_draft) > 0:
                    question_from_user_2 = input("Do you want to see the written text?\n1)Yes\n2)No"
                                                 "\nYour response: ")
                    if question_from_user_2 == "1":
                        print("\n", tabulate(list_draft, headers=["draft message", "Date of drafting"]))
                        msg = input("Do you want to send a message?\n1)Yes\n2)No\nYour response:")
                        if msg == "1":
                            selected_message = input("\nWhich message do you want to send?"
                                                     "\nCopy the full text of the message here:-->")
                            check_message = [True for i in list_draft if i[0] == selected_message]
                            if len(check_message) != 0:
                                question_from_user_3 = input("Do you want to send the written text to a user?\n1)Yes"
                                                             "\n2)No\nYour response: ")
                                if question_from_user_3 == "1":
                                    create_object3 = Messages("login_users.csv", "username")
                                    create_object4 = Draft("login_users.csv", "username")
                                    list_users = create_object4.show_users(username)
                                    print("\n", tabulate(list_users, headers=["users"]))
                                    question_from_user_4 = input("\nWhich person do you like to send a message to?"
                                                                 "\nEnter the name of the person you want : ")
                                    if create_object3.check_user(question_from_user_4):
                                        sent_time = create_object2.time_now()
                                        create_object5 = Sent("", "", "Desktop_users\\" +
                                                              username + "_sent.csv",
                                                              "Desktop_users\\" +
                                                              question_from_user_4 + "_inbox.csv")
                                        create_object5.reply_to_message(selected_message, sent_time,
                                                                        question_from_user_4, username)
                                        print(f"The message was successfully sent from {username} to "
                                              f"{question_from_user_2}.")
                                        logging_file.info_logger.info(
                                            f"The message was successfully sent from {username} "
                                            f"to {question_from_user_2}.")
                                        # break
                                        continue
                                    elif not create_object3.check_user(question_from_user_4):
                                        logging_file.warning_logger.error(f"{username}! entered the contact name "
                                                                          f"incorrectly")
                                        print("Sorry, you entered the contact name incorrectly")
                                        continue
                                else:
                                    print("You did not want to message the user")

                            else:
                                print("The message you selected is incorrect")
                        elif msg == "2":
                            pass
                        else:
                            print("Please enter the option correctly")
                            continue
                    elif question_from_user_2 == "2":
                        while True:
                            question_from_user_5 = input("What should I do with the message you wrote?\n1)clean"
                                                         "\n2)stay\n(Please enter the number you want)-->>")
                            if question_from_user_5 == "1":
                                print("\n", tabulate(list_draft, headers=["draft message", "Date of drafting"]))
                                selected_message = input("\nWhich message do you want to delete??"
                                                         "\nCopy the full text of the message here:-->")
                                create_object2.delete_message_draft(selected_message)

                                break
                            elif question_from_user_5 == "2":
                                break
                            else:
                                print("Please pay attention to the question and the type of answer requested.")
                                continue

                        # print("You did not want to be shown a draft of the messages.")
                    else:
                        print("Your answer to the question was wrong and you should pay attention to enter "
                              "the number 1 or 2")
                        logging_file.warning_logger.error(f"{username} answered the question incorrectly.Note: "
                                                          f"The numbers mentioned in the question must be entered")
                else:
                    print("You do not have pre-written messages.")
                    logging_file.info_logger.info(f"{username} did not have any pre-written messages in the box.")
                while True:
                    try:
                        question_from_user_2 = int(input("Do you want to write a new message?\n1)Yes\n2)No and exit"
                                                         "\nYour response: "))
                        if question_from_user_2 == 1:
                            question_from_user_3 = input("Write the text of your message : ")
                            question_from_user_4 = int(
                                input("Do you want to send the written text to a user?\n1)Yes\n2)No"
                                      "\nYour response: "))
                            if question_from_user_4 == 1:
                                create_object3 = Messages("login_users.csv", "username")
                                create_object4 = Draft("login_users.csv", "username")
                                list_users = create_object4.show_users(username)
                                print("\n", tabulate(list_users, headers=["users"]))
                                question_from_user_5 = input("Which person do you like to send a message to?"
                                                             "\nEnter the name of the person you want : ")
                                if create_object3.check_user(question_from_user_5):
                                    sent_time = create_object2.time_now()
                                    create_object5 = Sent("", "", "Desktop_users\\" +
                                                          username + "_sent.csv",
                                                          "Desktop_users\\" +
                                                          question_from_user_5 + "_inbox.csv")
                                    create_object5.reply_to_message(question_from_user_3, sent_time,
                                                                    question_from_user_5, username)
                                    print(f"The message was successfully sent from {username} to "
                                          f"{question_from_user_5}.")
                                    logging_file.info_logger.info(f"The message was successfully sent from {username} "
                                                                  f"to {question_from_user_2}.\nThe message was saved "
                                                                  f"in {username} Sent and {question_from_user_5} "
                                                                  f"inbox the message.")

                                    break
                                elif not create_object3.check_user(question_from_user_5):
                                    print("Sorry, you entered the contact name incorrectly")
                                    logging_file.warning_logger.error(f"{username}! entered the contact name "
                                                                      f"incorrectly")
                                    continue
                            else:
                                print("The user did not send the message she just wrote to anyone")
                                create_object6 = Messages("Desktop_users\\" + username + "_draft.csv", "draft_message")
                                draft_time = create_object6.time_now()
                                create_object_7 = Draft("Desktop_users\\" + username + "_draft.csv", "draft_message")
                                create_object_7.new_message_draft(draft_time, question_from_user_3)
                                logging_file.info_logger.info(f"A new message was saved in {username}'s Draft.")
                                break
                        elif question_from_user_2 == 2:
                            print("You did not want to write a new message.")
                            break
                        elif str(question_from_user_2).isdigit():
                            print("Dear audience, you have entered a number outside the range")
                            logging_file.warning_logger.error(f"{username} entered a number out of range")
                    except ValueError:
                        print("you must enter a integer!")
                        logging_file.warning_logger.error(f"Instead of selecting the numeric option, "
                                                          f"{username} unfortunately entered the string.")

            elif logged_user == 4:
                create_object = Messages("Desktop_users\\" + username + "_sent.csv", "sent_message")
                print(create_object.number_message())
                create_object1 = Sent("Desktop_users\\" + username + "_sent.csv", "sent_message", "", "")
                list_sent = create_object1.show_message()
                if len(list_sent) > 0:
                    print("\n", tabulate(list_sent, headers=["Contact", "Message text", "Date of submit"]))
                else:
                    print("You have not sent any messages yet.")
                question_from_user_1 = input("Do you want to send a message to someone?\n1)Yes\n2)No\nYour response : ")
                if question_from_user_1 == "1":
                    create_object2 = Messages("login_users.csv", "username")
                    create_object3 = Draft("login_users.csv", "username")
                    list_users = create_object3.show_users(username)
                    print("\n", tabulate(list_users, headers=["users"]))
                    while True:
                        question_from_user_2 = input("\nWhich person do you like to send a message to?"
                                                     "\nEnter the name of the person you want : ")
                        if create_object2.check_user(question_from_user_2):
                            question_from_user_3 = input("Please enter the text of your message :")
                            sent_time = create_object2.time_now()
                            question_from_user_4 = input("Are you sure you want to send the message?\n1)Yes\n2)No"
                                                         "\n(Please enter the number you want)-->> ")
                            if question_from_user_4 == "1":
                                create_object4 = Sent("", "", "Desktop_users\\" +
                                                      username + "_sent.csv",
                                                      "Desktop_users\\" +
                                                      question_from_user_2 + "_inbox.csv")
                                create_object4.reply_to_message(question_from_user_3, sent_time,
                                                                question_from_user_2, username)
                                print(f"The message was successfully sent from {username} to "
                                      f"{question_from_user_2}.")
                                logging_file.info_logger.info(f"The message was successfully sent from {username} to "
                                                              f"{question_from_user_2}.\nThe message was saved in "
                                                              f"{username} Sent and {question_from_user_2} "
                                                              f"inbox the message.")
                            elif question_from_user_4 == "2":
                                while True:
                                    question_from_user_5 = input("What should I do with the message you wrote?\n1)clean"
                                                                 "\n2)stay\n(Please enter the number you want)-->>")
                                    if question_from_user_5 == "1":
                                        print("Message deleted successfully.")
                                        break
                                    elif question_from_user_5 == "2":
                                        obj = Messages("Desktop_users\\" + username + "_draft.csv", "draft_message")
                                        obj1 = Draft("Desktop_users\\" + username + "_draft.csv", "draft_message")
                                        obj1.new_message_draft(sent_time, question_from_user_3)
                                        print(f"Message was successfully saved in {username} draft box. ")
                                        logging_file.info_logger.info(f"Message was successfully saved in {username} "
                                                                      f"draft box. ")
                                        break
                                    else:
                                        print("Please pay attention to the question and the type of answer requested.")
                                        continue
                            else:
                                print("Please pay attention to the question and the type of answer requested.")
                                continue
                            question_from_user_6 = input("What are you going to do now?\n1)exit\n2)I want to text "
                                                         "someone again\n(Please enter the number you want)-->> ")
                            if question_from_user_6 == "1":
                                break
                            else:
                                continue
                        else:
                            print(f"{username}! entered the person's name incorrectly")
                            continue
                elif question_from_user_1 == "2":
                    pass
                else:
                    print("You entered the option incorrectly")
                    continue
            elif logged_user == 5:
                create_object1 = Messages("login_users.csv", "username")
                create_object2 = Draft("login_users.csv", "username")
                list_users = create_object2.show_users(username)
                print("\n", tabulate(list_users, headers=["users"]))
                question_from_user_1 = input("\nWhich person do you like to send a message to?"
                                             "\nEnter the name of the person you want : ")
                if create_object1.check_user(question_from_user_1):
                    question_from_user_2 = input("Enter the text of your message :")
                    sent_time = create_object1.time_now()
                    create_object3 = Sent("", "", "Desktop_users\\" +
                                          username + "_sent.csv",
                                          "Desktop_users\\" +
                                          question_from_user_1 + "_inbox.csv")
                    create_object3.reply_to_message(question_from_user_2, sent_time,
                                                    question_from_user_1, username)
                    print(f"The message was successfully sent from {username} to "
                          f"{question_from_user_1}.")
                    logging_file.info_logger.info(f"The message was successfully sent from {username} "
                                                  f"to {question_from_user_1}.")
                    # break
                elif not create_object1.check_user(question_from_user_1):
                    logging_file.warning_logger.error(f"{username}! entered the contact name "
                                                      f"incorrectly")
                    print("Sorry, you entered the contact name incorrectly")
                    continue
            elif logged_user == 6:
                print("You requested to log out.\n*___`Have a good day buddy!☻`___*")
                logging_file.info_logger.info(f"{username} left her(his) user page.")
                break
            elif str(logged_user).isdigit():
                print("Dear audience, you have entered a number outside the range")
                logging_file.warning_logger.error(f"{username} entered a number out of range")
        except ValueError:
            print("you must enter a integer!")
            logging_file.warning_logger.error(f"Instead of selecting the numeric option, {username} "
                                              f"unfortunately entered the string.")


while True:
    try:
        question1 = int(input("Dear friend, have you registered before??"
                              "\n(* Please enter only the option number. *)\n1)Yeah\n2)No\n3)exit"
                              "\nPlease enter your answer:"))
        if question1 == 1:
            """
            log in
            """
            username = input("Please enter your username:")
            check_username = User(username, "")
            entity_user = check_username.existence_user()
            if entity_user:
                check_lock = check_username.check_locked
                check_unlock = check_username.unlock_account
                if check_lock:
                    if check_unlock:
                        counter = 0
                        while counter < 3:
                            password = input("please enter your password:")
                            check_password = User(username, password)
                            p_hash = check_password.hash_password()
                            if check_password.matching_user_password(p_hash):
                                print(f"welcome {username} ! are now logged in to your desktop.")
                                logging_file.info_logger.info(f"{username} successfully logged in.")
                                received_messages = check_password.matching_user_password(p_hash)
                                online_user = user_system(username)
                                counter += 4
                                break
                            elif not check_password.matching_user_password(p_hash):
                                print("You entered the wrong password, please try again.")
                                counter += 1
                                if counter == 3:
                                    lock_account = check_username.lock_account()
                                    logging_file.warning_logger.error("Your account has been locked.")
                                    print(f'You entered the wrong password several times'
                                          f'\n*___Sorry your account has been locked.___*')
                                    break
                                else:
                                    continue
                    else:
                        print(f"Your account is still locked.")
                else:
                    print(f"{username}!Your account is locked")
                    logging_file.warning_logger.error(f"{username} account is locked and can not be logged in.")

            elif not entity_user:
                print("Sorry, you have not registered with this name before.")
                logging_file.warning_logger.error(f"{username} could not log in due to incorrect username")

                # try:
                #     question3 = int(input("Are you sure you registered?!\n1)Yeah\n2)No\n3)Excuse me, I want to "
                #                           "go out.\n(Remember to enter only the number of the option you want)"
                #                           "-->> Please enter your answer:"))
                #     if question3 == 1:
                #         username = input("Please enter your username:")
                #         check_username = User(username, "")
                #         entity_user = check_username.existence_user()
                #         if entity_user:
                #             break
                #         else:
                #             continue
                #     else:
                #         continue
                # except ValueError:
                #     logging_file.warning_logger.error(f"{username} answer was wrong.")
                #     print("Oops! your answer was wrong. -->> Remember you must enter an integer.")
        elif question1 == 2:
            """
            sign up
            """
            while True:
                try:
                    question2 = int(input("Would you like to register?\n1)Yeah\n2)No\n(Remember to enter only the "
                                          "number of the option you want)\nPlease enter your answer --> "))
                    if question2 == 1:
                        while True:
                            username = input("Please enter a new username:")
                            check_username = User(username, "")
                            if check_username.validation_user():
                                if not check_username.existence_user():
                                    while True:
                                        new_email = input("Please enter your new email:")
                                        check_email = User.validation_address_email(new_email)
                                        if check_email:
                                            break
                                    while True:
                                        new_password = input("Please enter a new password:")
                                        check_password = User(username, new_password)
                                        if check_password.validation_password():
                                            while True:
                                                confirm_password = input("Please Confirm password:")
                                                if new_password == confirm_password:
                                                    hash_new_password = check_password.hash_password()
                                                    logging_file.info_logger.info(f"You are now logged in to "
                                                                                  f"your desktop.")
                                                    print("welcome. You are now logged in to your desktop.")
                                                    check_password.add_new_user(hash_new_password)
                                                    online_user = user_system(username)
                                                    break
                                                else:
                                                    print("sorry! The password you selected does not match "
                                                          "the password you finally approved.")
                                            break
                                else:
                                    print("Someone has already registered under this username."
                                          "So you can not register with this username."
                                          "\nPlease choose another username.")
                                break
                    elif question1 == 2:
                        print("You requested to log out.")
                        logging_file.info_logger.info('The user did not register and logged out')
                    break
                except ValueError:
                    logging_file.warning_logger.error(f"username answer was wrong")
                    print("Oops! your answer was wrong. Please try again.\nRemember you must enter an integer .")
        elif question1 == 3:
            print("You requested to log out.\n*__`Have a good day buddy!☻`__*")
            logging_file.info_logger.info('User logged out')
            break
        elif str(question1).isdigit():
            logging_file.warning_logger.error(f"Dear friend, you have entered a number outside the range")
            print("Dear audience, you have entered a number outside the range")
    except ValueError:
        print("Oops! your answer was wrong. Please try again.\nRemember you must enter an integer .")
        logging_file.warning_logger.error(f"username answer was wrong")
