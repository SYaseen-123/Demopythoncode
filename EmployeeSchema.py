import pyodbc

server = 'HCL-02-121\SQLEXPRESS01'
database = 'Employeee'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class employee_schema:
    def employe_table(self):
        try:

            query1 = cursor.execute('''use Employeee''')
            query2 = cursor.execute('''create table employe_table1
                                (
                                Name varchar(50),
                                project varchar(50),
                                salary int,
                                )
                                ''')
            query3=cursor.execute('''select * from employe_table1''')

            cnxn.commit()
        except:
            print("Table is already existing")
    def Add_column(self):
        query4 = ''' Alter table employe_table1 Add Emp_ID int '''
        cursor.execute(query4)
        cnxn.commit()
        print("Column has has been added")

obj=employee_schema()
obj.employe_table()
obj.Add_column()







