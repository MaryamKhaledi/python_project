import csv
import os


class FileHandler:
    """
    This class collects the operations that we are going to do in the file to make it easier
    for us to access the file and to avoid duplication.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """
        This method reads the file and saves it in the list.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8-sig') as myfile:
                reader = csv.DictReader(myfile)
                return list(reader)
        else:
            return "path is incorrect"

    def write_file(self, info, mode="a"):
        """
        This method does the job of writing to the file.
        """
        if isinstance(info, dict):
            fields = info.keys()
            info = [info]
        elif isinstance(info, list):
            fields = info[0].keys()
        with open(self.file_path, mode, encoding='utf-8-sig', newline="") as myfile:
            writer = csv.DictWriter(myfile, fieldnames=fields)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows(info)

    def write_new_inbox(self):
        """
        Create a new inbox file.
        """
        with open(self.file_path, 'w', encoding='utf-8-sig') as myfile:
            field_header = ["username", "inbox_message", "time_to_receive_inbox", "Has_been_read", "seen_time"]
            writer = csv.DictWriter(myfile, fieldnames=field_header)
            writer.writeheader()

    def write_new_draft(self):
        """
        Create a new draft file.
        """
        with open(self.file_path, 'w', encoding='utf-8-sig') as myfile:
            field_header = ["draft_message", "time_to_receive_draft"]
            writer = csv.DictWriter(myfile, fieldnames=field_header)
            writer.writeheader()

    def write_new_sent(self):
        """
        Create a new sent file
        """
        with open(self.file_path, 'w', encoding='utf-8-sig') as myfile:
            field_header = ["username", "sent_message", "message_sending_time"]
            writer = csv.DictWriter(myfile, fieldnames=field_header)
            writer.writeheader()
