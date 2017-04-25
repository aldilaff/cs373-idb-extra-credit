#!/usr/bin/env python3

# -------------
# logger_levels_examples.py
# -------------

import logging

logger = logging.getLogger('logger')

logger.debug('Debug message.')
logger.info('Info message.')
logger.warning('This is a warning.')
logger.error('THERE IS AN ERROR')
logger.critical('NOOOOO!!!')

# --------- CONSOLE OUTPUT ---------
# This is a warning.
# THERE IS AN ERROR
# NOOOOO!!!
# ----------------------------------

print('------- logger Level: DEBUG -------')
logging.basicConfig(level=logging.DEBUG)
logger.setLevel(logging.DEBUG)

logger.debug('Debug message.')
logger.info('Info message.')
logger.warning('This is a warning.')
logger.error('THERE IS AN ERROR')
logger.critical('NOOOOO!!!')

# --------- CONSOLE OUTPUT ---------
# DEBUG:root:Debug message.
# INFO:root:Info message.
# WARNING:root:This is a warning.
# ERROR:root:THERE IS AN ERROR
# CRITICAL:root:NOOOOO!!!
# ----------------------------------

print('------- logger Level: INFO -------')
logger.setLevel(logging.INFO)

logger.debug('Debug message.')
logger.info('Info message.')
logger.warning('This is a warning.')
logger.error('THERE IS AN ERROR')
logger.critical('NOOOOO!!!')

# --------- CONSOLE OUTPUT ---------
# INFO:root:Info message.
# WARNING:root:This is a warning.
# ERROR:root:THERE IS AN ERROR
# CRITICAL:root:NOOOOO!!!
# ----------------------------------

print('------- logger Level: ERROR -------')
logger.setLevel(logging.ERROR)

logger.debug('Debug message.')
logger.info('Info message.')
logger.warning('This is a warning.')
logger.error('THERE IS AN ERROR')
logger.critical('NOOOOO!!!')

# --------- CONSOLE OUTPUT ---------
# ERROR:root:THERE IS AN ERROR
# CRITICAL:root:NOOOOO!!!
# ----------------------------------
