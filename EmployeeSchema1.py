import pyodbc

server = 'HCL-02-121\SQLEXPRESS01'
database = 'Employee_data'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Passed(Exception):
    pass
class Failed(Exception):
    pass
class employee_schema:
    def employee_table(self):
        try:
            query='''select *from employee_table'''
            values=cursor.execute(query)
            if(not(values)):
                query1 = cursor.execute('''use Employee_data''')
                query2 = cursor.execute('''create table employee_table
                                (
                                Name varchar(50),
                                project varchar(50),
                                salary int,
                                )
                                ''')
                query3=cursor.execute('''select * from employee_table''')

                cnxn.commit()
            else:
                raise Failed
        except Failed:
            print("Table is already existing")
