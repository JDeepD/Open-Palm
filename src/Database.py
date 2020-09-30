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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS DATA (RollNo INTEGER,StudentName TEXT,Class TEXT )""")

    def store_values(self, RollNo, StudentName, Class):
        self.cursor.execute("INSERT INTO DATA VALUES(:Rollno , :StudentName , :Class)", {
                            'Rollno': RollNo, 'StudentName': StudentName, 'Class': Class})
        self.mydb.commit()
class get_response(make_db):
    def __init__(self, Database, query):
        self.query = query
        self.Database = Database
        super().__init__(Database)

    def get_data(self):
        try:
            self.cursor.execute(
                f'SELECT *FROM DATA WHERE STUDENTNAME = :studentname', {'studentname': self.query})
            data = self.cursor.fetchall()
            return(data)
        except:
            return('No Such Query Available Available')


#if __name__ == '__main__':
    # db = make_db('Databs')  # Enter Database name
    # db.store_values(12, 'Nick', 24)  # Enter Rollno,Studentname,marks
    #d = get_response('Databs', 'Nick').get_data()
    #print(d)
