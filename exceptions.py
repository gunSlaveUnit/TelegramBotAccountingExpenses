#! usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: gunSlaveUnit

The file contains classes of custom exceptions
that occur during the operation of the bot.
"""


class NotCorrectMessage(Exception):
    """This exception is thrown
    if it was not possible to parse the message from the user.
    """
    pass
