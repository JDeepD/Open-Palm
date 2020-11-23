"""This module will be used for interacting with the database file."""  # noqa pylint: disable=invalid-name 

import sqlite3


class make_db:
    """This class will mainly deal with connecting, creating the database
    and storing values into it.Its methods are:

    1. constructor method( __init__ ) takes the name of the database
       as argument and makes creates a database file with the given name
       This function also creates a `cursor` object that allows to handle
       Mysql commands through python strings.

    2. store_values(self, StudentName, Class, Section, RollNo)
        It takes in arguments : StudentName, Class, Section & Rollno
        and stores it into the database.

    3. `check_dup` method takes in Name, Class, Section, Rollno as parameter
        and returs the number of duplicate entries of the given entry.
    """
    def __init__(self, dbname):
        self.dbname = dbname
        self.mydb = sqlite3.connect(self.dbname + '.db')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS DATA (StudentName TEXT , Class TEXT , Section TEXT ,RollNo TEXT)""")  # noqa pylint: disable=all

    def store_values(self, StudentName, Class, Section, RollNo):
        """See the class docstring"""

        self.cursor.execute("INSERT INTO DATA VALUES( :StudentName , :Class, :Section , :Rollno)", {  # noqa
            'StudentName': StudentName, 'Class': Class, 'Section': Section, 'Rollno': RollNo})  # noqa

        self.mydb.commit()

    def check_dup(self, Name, Class, Section, Roll):
        """See the class docstring"""

        self.cursor.execute(f"SELECT COUNT (*) FROM DATA WHERE STUDENTNAME=:Name AND CLASS=:Class AND SECTION=:Section AND ROLLNO=:Roll", {  # noqa
            'Name': Name,
            'Class': Class,
            'Section': Section,
            'Roll': Roll
        })
        return(self.cursor.fetchall())


class get_response(make_db):
    """
    This is a child class of `make_db`. It has the following methods.

    1. constructor method(__init__)that takes in the Database name as parameter
       This database name is then used to create a connection with the `.db`
       file created earlier.
       Note: This class does not creates a `cursor` object on its own but it
       inherits the `cursor`object from its parent `make_db`.
       The `super().__init__(Database)` is same as calling the
       __init__ method from `make_db` class that creates a connection as
       well as  `cursor`. This cursor is accesible
       to all the methods of `get_response`.

    2. `get_data_by_query` that takes in the query (Student Name) as parameter
        and returns the entry containing that query.

    3. `delete_data` takes in Name, Class, Section, Roll as parameter and
        deletes the entry containing those values.
        This function returns nothing.

    """

    def __init__(self, Database):
        self.Database = Database
        super().__init__(Database)

    def get_data_by_query(self, query):
        """See the class docstring"""

        self.query = query
        try:
            self.cursor.execute(
                f'SELECT *FROM DATA WHERE STUDENTNAME = :studentname', {'studentname': self.query})  # noqa
            data = self.cursor.fetchall()
            return(data)
        except:  # noqa
            return('No Such Query Available Available')

    def get_all_data(self):
        """See the class docstring"""

        self.cursor.execute("Select * FROM DATA")
        data = self.cursor.fetchall()
        return(data)

    def delete_data(self, Name, Class, Section, Roll):
        """See the class docstring"""

        self.cursor.execute(f"DELETE FROM DATA WHERE STUDENTNAME=:Name AND CLASS=:Class AND SECTION=:Section AND ROLLNO=:Roll LIMIT 1", {  # noqa
            'Name': Name,
            'Class': Class,
            'Section': Section,
            'Roll': Roll
        })
        self.mydb.commit()
# if __name__ == '__main__':
    # db = make_db('Databs')  # Enter Database name
    # db.store_values(12, 'Nick', 24)  # Enter Rollno,Studentname,marks
    # d = get_response('Databs', 'Nick').get_data()
    # print(d)

















