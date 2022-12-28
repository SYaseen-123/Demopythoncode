import pyodbc
import EmployeeSchema

server = 'HCL-02-121\SQLEXPRESS01'
database = 'Employeee'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class Employee:
    Bonus=2
    Project=['java','python','c']
    def __init__(self,Name,project,salary):

        self.Name=Name
        self.project=project
        self.salary=salary
    def insert_employee_details(self):
        query1='''
          
        INSERT INTO employe_table1(Name,project,salary)
                   VALUES
                   ('{0}','{1}',{2})
        ''finalQ= query1.format(self.Name,self.project,self.salary)
            cursor.execute(finalQ)
            query2=cursor.execute('''select *from employe_table1''')
            cnxn.commit()
            def Updated_Salary(self, New_Salary, Name):
                try:
                    if New_Salary != self.salary:
                        fileinfoQuery = '''
                                                Update Employee_details SET Salary ='{0}' WHERE Name = '{1}'
                                                '''
                        query1= fileinfoQuery.format(New_Salary, self.Name)
                        values=cursor.execute(query1)
                        cnxn.commit()
                    else:
                        print("trftuftf")
                except:
                    pass

obj=Employee('yaseen','python',30000)
obj1=EmployeeSchema.employee_schema()
#obj.insert_employee_details()



