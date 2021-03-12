"""This module will be used for storing the username and email id"""

import passmanager as pm  # noqa pylint: disable=import-error


def storemail(user, mail):
    """
    This function will take two arguments
    1. Username
    2. eMail id
    """
    pm.storepass(user, mail, target="maildata.csv")


storemail("jaydeep", "test@gmail.com")
