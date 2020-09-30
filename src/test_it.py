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

