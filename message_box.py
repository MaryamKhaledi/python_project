import csv
from datetime import datetime, time
import logging
import file_handler
import logging_file
import os
# import pandas as pd


# import operator


class Messages:
    """
    This is the parent class. It is supposed to perform message counting operations and message history and so on.
    """

    def __init__(self, desk_user, file_lines):
        self.desk_user = desk_user
        self.file_lines = file_lines

    def number_message(self):
        """
        Display the number of messages in the 'Inbox' package.
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()  # dict list is output
        list_msg = []
        # cont = 0
        for row in read_file:
            # if row[self.file_lines] != None:
            # cont +=1
            list_msg.append(row[self.file_lines])
        logging_file.info_logger.info("Display the number of messages in the 'Inbox' package.")
        return f"You have received {len(list_msg)} messages."
        # return cont

    @staticmethod
    def time_now():
        """
        Displays the date on which each message was received.
        """
        now = datetime.now()
        time_now = time(now.hour, now.minute, now.second)
        now_time = datetime.combine(now.date(), time_now)
        return now_time

    def check_user(self, check_user):
        """
        Checks users to see if they are in the list
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        for row in read_file:
            if row["username"] == check_user:
                return True

    # def show_message(self, check_user):
    #     """
    #     Select the desired username and read her(his) message.
    #     """
    #     open_file = file_handler.FileHandler(self.desk_user)
    #     read_file = open_file.read_file()
    #     for row in read_file:
    #         if row["users"] == check_user:
    #             print(f"The text of {check_user}'s message :\n--->>> {row['self.file_lines']}")
    #     logging.info("The message text was displayed to the user.")


class Inbox(Messages):
    """
    This class is a class of incoming messages that contains methods such as
    users_message and show_message and update_seen.
    """

    def __init__(self, desk_user, file_lines, check_user):
        super().__init__(desk_user, file_lines)
        self.check_user = check_user

    # def number_message(self):
    #     super().number_message()

    # def time_now(self):
    #     super().time_now()

    def users_message(self):
        """
        Show list of names of people who sent messages.As well as the date the message was sent.
        :return:List of names of people who sent messages. As well as the date the message was sent.
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        list_contacts = []
        for row in read_file:
            if row[self.file_lines] != "":
                list_contacts.append([row["username"], row["time_to_receive_inbox"], row["Has_been_read"]])
        logging_file.info_logger.info("Incoming messages were displayed to the user.")
        return list_contacts

    # def check_user(self, check_user):
    #     super().check_user()

    # def show_message(self):
    #     super().show_message()

    def show_message(self):
        """
        Select the desired username and read her(his) message.
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        list_msg = []
        for row in read_file:
            if row["username"] == self.check_user:
                list_msg.append([self.check_user, row['inbox_message']])
        logging_file.info_logger.info("The message text was displayed to the user.")
        return list_msg

    def update_seen(self, time):
        """
        This method if reading a message from the Inbox,The message receives the read mark.
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        list_update = []
        for row in read_file:
            if row["username"] == self.check_user:
                if row["Has_been_read"] == "":
                    row['Has_been_read'] = "yes"
                    # df.to_csv("AllDetails.csv", index=False)
                    row['seen_time'] = time
                    # read_file.to_csv(self.desk_user, index=False)
                    list_update.append(row)
        for row in read_file:
            if row["username"] != self.check_user:
                list_update.append(row)

        with open(self.desk_user, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            # csvwriter.writerow(["username", "inbox_message", "time_to_receive_inbox", "Has_been_read", "seen_time"])
            csvwriter.writerows(list_update)

        # or:
        # open_file = file_handler.FileHandler(self.desk_user)
        # read_file = open_file.read_file()
        # df = pd.DataFrame(read_file)
        # df.replace("", "yes", inplace=True)
        # df.replace("", time, inplace=True)
        # write_file = read_file.write_file(df, mode="w")

        logging_file.info_logger.info("The user reads the messages of one of their contacts in the Inbox.")
        return f"The message was seen"


class Draft(Messages):
    """
    This class contains messages that have been written but not sent, and we can perform operations on them.
    """

    def __init__(self, desk_user, file_lines):
        super().__init__(desk_user, file_lines)

    # def number_message(self):
    #     super().number_message()

    # def time_now(self):
    #     super().time_now()

    def show_users(self, user_online):
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        list_users = []
        for row in read_file:
            if row[self.file_lines] != user_online:
                list_users.append([row[self.file_lines]])
        return list_users

    def draft_message(self):
        """
        Show list of names of people who sent messages.As well as the date the message was sent.
        :return:List of names of people who sent messages. As well as the date the message was sent.
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        list_contacts = []
        for row in read_file:
            list_contacts.append([row["draft_message"], row["time_to_receive_draft"]])
        logging_file.info_logger.info("Incoming messages were displayed to the user.")
        return list_contacts

    # def check_user(self, check_user):
    #     super().check_user()

    # def show_message(self):
    #     super().show_message()

    def show_message(self):
        """
        Select the desired username and read her(his) message.
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        list_msg = []
        for row in read_file:
            if row["users"] == self.check_user:
                list_msg.append([self.check_user, row['draft_message']])
                # print(f"The text of {self.check_user}'s message :\n--->>> {row['inbox_message']}")
        logging_file.info_logger.info("The message text was displayed to the user.")
        return list_msg

    def new_message_draft(self, draft_time, question_from_user_3):
        open_file = file_handler.FileHandler(self.desk_user)
        write_file = open_file.write_file({self.file_lines: question_from_user_3, "time_to_receive_draft": draft_time})

    def delete_message_draft(self, msg):
        """
        This method removes messages from the draft.
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        lists = []
        for row in read_file:
            if row[self.file_lines] == msg:
                read_file.remove(row)
                del row
            else:
                lists.append(row)

        with open(self.desk_user, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["draft_message", "time_to_receive_draft"])
            csvwriter.writerows(lists)
        print("Message deleted successfully.")


class Sent(Messages):
    """
    This class performs operations related to sending messages.
    """

    def __init__(self, desk_user, file_lines, transmitter_user, recipient_user):
        super().__init__(desk_user, file_lines)
        self.transmitter_user = transmitter_user
        self.recipient_user = recipient_user

    def reply_to_message(self, question5, writing_time, question3, username):
        """
        A message or messages are sent to the intended user. And the part file of both users is updated.
        """
        open_file1 = file_handler.FileHandler(self.transmitter_user)
        write_file1 = open_file1.write_file({"username": question3, "sent_message": question5,
                                             "message_sending_time": writing_time})
        open_file2 = file_handler.FileHandler(self.recipient_user)
        write_file2 = open_file2.write_file({"username": username, "inbox_message": question5,
                                             "time_to_receive_inbox": writing_time, "Has_been_read": "",
                                             "seen_time": ""})

    def show_message(self):
        """
        Select the desired username and read her(his) message.
        """
        open_file = file_handler.FileHandler(self.desk_user)
        read_file = open_file.read_file()
        list_msg = []
        for row in read_file:
            if row["username"] != None:
                list_msg.append([row["username"], row['sent_message']])
                # print(f"The text of {self.check_user}'s message :\n--->>> {row['inbox_message']}")
        logging_file.info_logger.info("The message text was displayed to the user.")
        return list_msg
        # print(list_msg)
