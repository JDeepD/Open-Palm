"""This module will deal with password management"""


import csv


def storepass(user, passwd, target="admins.csv"):
    """This function is used for storing user-pass combo
    as elements to a csv file. By default, the values will be
    stored in `creds/admins.csv`. The csvs will always be
    saved in the `creds` directory but the filenames can
    be changed by using the optional `target` parameter
    """

    with open(f"creds/{target}", 'a+') as fil:
        writer = csv.writer(fil)
        writer.writerow([user, passwd])


def cipherpass(passwd):
    """Inputs a string. Ciphers it using the following
    algorithm and returns the ciphered password
    Algo:
    1. Takes the string.
    2. Tranverse though each letter.
    3. Take the ascii value of that letter
       and doubles it using `chr` function
    4. Converts the new ascii value back to
       a new letter.
    5. Adds that letter to an empty string and
       repeat from Step 1 until all letters are
       traversed.
    6. Returns the `ciphered` string.
    """
    tmp = ""
    for i in passwd:
        tmp += chr(ord(i)*2)
    return tmp


def decipherpass(encr):
    """Inputs a strings. Deciphers in using the same algorithm
    that was used in `cipherpass`. Returns the original passwd
    """
    tmp = ""
    for i in encr:
        tmp += chr(int(ord(i)/2))
    return tmp


def get_pass(target="admins.csv"):  # gets the user info from the Csv file
    """This function is used for reading a csv file
    and returning the contents in the form of a
    dictionary
    """
    with open(f"creds/{target}", 'r+', encoding="utf8") as fil:
        reader = csv.reader(fil)
        print(list(reader))
        dic = {}
        for i in reader:
            dic[i[0]] = i[1]
        return dic

