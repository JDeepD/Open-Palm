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


