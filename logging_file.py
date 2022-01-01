import logging

warning_logger = logging.getLogger('warning')
info_logger = logging.getLogger(__name__)
info_logger.setLevel(logging.INFO)

info_handler = logging.FileHandler('info.log')
warning_handler = logging.FileHandler('warning.log')

info_handler.setLevel(logging.INFO)
warning_handler.setLevel(logging.WARNING)

log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

info_handler.setFormatter(log_format)
warning_handler.setFormatter(log_format)

info_logger.addHandler(info_handler)
warning_logger.addHandler(warning_handler)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler('msg.log')
# file_handler.setLevel(level=logging.INFO)
# formatter = logging.Formatter("levelname)s - %(filename)s :%(message)s - %(asctime)s  ", datefmt='%Y-%m-%d %H:%M:%S')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# logging.basicConfig(level=logging.INFO, filename='msg.log', filemode='a',
#                     format='%(levelname)s -%(filename)s :%(message)s %(asctime)s', datefmt='%d-%b-%y %H:%M:%S')
