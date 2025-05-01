#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging as lg
import os
from datetime import datetime

# creating a folder for the logs
logs_path = './logs/'
try:
    os.mkdir(logs_path)
except OSError:
    print("Creation of the directory %s failed - it does not have to be bad" % logs_path)
else:
    print("Successfully created log directory")

# renaming each log depending on the time

date = datetime.now().strftime("%Y%m%d_%H:%M:%S")
log_name = date + '.log'
currentLog_path = logs_path + log_name
lg.basicConfig(filename= currentLog_path, format='%(asctime)s - %(levelname)s: %(message)s', level=lg.DEBUG)
lg.getLogger().addHandler(lg.StreamHandler())  # to print in the console
#logging levels: DEBUG, INFO, WARNING, ERROR

lg.info('Something happened')
lg.debug('This is a debugging message!')
lg.warning('Watch out!')
lg.error('Something went wrong')