#!/usr/bin/env python3

# -------------
# logging_handlers_examples.py
# -------------

import logging

# create logger
info_logger = logging.getLogger('info_logger')
info_logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# create console handler
console_output = logging.StreamHandler()
console_output.setLevel(logging.DEBUG)
console_output.setFormatter(formatter)
info_logger.addHandler(console_output)

# create file handler
file_output = logging.FileHandler(filename='log.txt')
file_output.setLevel(logging.WARNING)
file_output.setFormatter(formatter)
info_logger.addHandler(file_output)

info_logger.debug('Debug message.')
info_logger.info('Info message.')
info_logger.warning('This is a warning.')
info_logger.error('THERE IS AN ERROR')
info_logger.critical('NOOOOO!!!')

# --------- CONSOLE OUTPUT ---------
# info_logger - INFO - Info message.
# info_logger - WARNING - This is a warning.
# info_logger - ERROR - THERE IS AN ERROR
# info_logger - CRITICAL - NOOOOO!!!
# ----------------------------------

# --------- FILE OUTPUT ---------
# info_logger - WARNING - This is a warning.
# info_logger - ERROR - THERE IS AN ERROR
# info_logger - CRITICAL - NOOOOO!!!
# ----------------------------------