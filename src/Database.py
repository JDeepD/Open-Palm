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

import sqlite3

class make_db:
    def __init__(self, dbname):
        self.dbname = dbname
        self.mydb = sqlite3.connect(self.dbname + '.db')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS DATA (StudentName TEXT , Class TEXT , Section TEXT ,RollNo TEXT)""")

    def store_values(self,StudentName,Class,Section,RollNo):
        self.cursor.execute("INSERT INTO DATA VALUES( :StudentName , :Class, :Section , :Rollno)", {
            'StudentName': StudentName ,'Class': Class , 'Section': Section,'Rollno': RollNo })

        self.mydb.commit()

    def check_dup(self,Name,Class,Section,Roll):
        self.cursor.execute(f"SELECT COUNT (*) FROM DATA WHERE STUDENTNAME=:Name AND CLASS=:Class AND SECTION=:Section AND ROLLNO=:Roll",{
            'Name': Name,
            'Class':Class,
            'Section':Section,
            'Roll':Roll
        })
        return(self.cursor.fetchall())


class get_response(make_db):

    def __init__(self, Database):
        self.Database = Database
        super().__init__(Database)

    def get_data_by_query(self , query):
        self.query = query
        try:
            self.cursor.execute(
                f'SELECT *FROM DATA WHERE STUDENTNAME = :studentname', {'studentname': self.query})
            data = self.cursor.fetchall()
            return(data)
        except:
            return('No Such Query Available Available')

    def get_all_data(self):
        self.cursor.execute("Select * FROM DATA")
        data = self.cursor.fetchall()
        return(data)

    def delete_data(self,Name,Class,Section,Roll):
        self.cursor.execute(f"DELETE FROM DATA WHERE STUDENTNAME=:Name AND CLASS=:Class AND SECTION=:Section AND ROLLNO=:Roll", {
            'Name': Name,
            'Class':Class,
            'Section':Section,
            'Roll':Roll
        })
        self.mydb.commit()
#if __name__ == '__main__':
    # db = make_db('Databs')  # Enter Database name
    # db.store_values(12, 'Nick', 24)  # Enter Rollno,Studentname,marks
    #d = get_response('Databs', 'Nick').get_data()
    #print(d)

















