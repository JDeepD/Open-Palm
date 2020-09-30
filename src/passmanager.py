# MIT License

# Copyright (c) 2020 Jdeep

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This is very very bad ciphering technique and is only implemented for simplicity of the Project.
# Please donot store the same password as your other accounts like Gmail,Facebook etc. Use this at your own risk
import csv

def storepass(user,passwd):
    with open("data.csv",'a+') as fil :
        writer = csv.writer(fil)
        writer.writerow([user,passwd])

def cipherpass(passwd):
    tmp = ""
    for i in passwd:
       tmp += chr(ord(i)*2)
    return(tmp)

def decipherpass(encr):
    tmp = ""
    for i in encr:
        tmp += chr(int(ord(i)/2))
    return(tmp)

def get_pass():     #gets the user info from the Csv file
    with open("data.csv",'r+') as fil:
        reader = csv.reader(fil)
        dic = {}
        for i in reader:
            dic[i[0]] = i[1]
        return(dic)
