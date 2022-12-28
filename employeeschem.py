import pyodbc

server = 'HCL-02-121\SQLEXPRESS01'
database = 'Employeee'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


class InvalidBonus(Exception):
    pass


class EmployeeNew:
    projects = ['python', 'c', 'java']
    bonus = 2

    def __init__(self, Name, salary, project):
        self.Name = Name
        self.salary = salary
        self.project = project

    def insert_Employee_Details(self):
        try:
            query = '''  
                            INSERT INTO employe_table1 (Name,salary,project)
                            VALUES
                            ('{0}',{1},'{2}')  '''

            insertQuery = query.format(self.Name, self.salary, self.project)
            cursor.execute(insertQuery)
            cnxn.commit()
            print("New file search results committed to DB")
        except:
            pass

    def Display_Employee_Details(self):
        try:
            query = ''' select * from employe_table1 where Name = '{0}' '''
            searchQuery = query.format(self.Name)
            values = cursor.execute(searchQuery)
            if (values):
                for fileInfo in values:
                    print("==========================")
                    print("File name: {}".format(fileInfo.Name))
                    print("File path: {}".format(fileInfo.salary))
                    print("project: {}".format(fileInfo.project))
                    print("==========================")
                return True
            return False
        except:
            pass

    def Add_Bonus(self, currentBonus):
        try:
            self.currentBonus = currentBonus
            if self.currentBonus > 0 and self.currentBonus <= self.bonus:
                self.salary = self.salary + self.salary * self.currentBonus
                print(self.salary)
                query = ''' select * from employe_table1 where Name = '{0}' '''
                searchQuery = query.format(self.Name)
                values = cursor.execute(searchQuery)

                Query = '''
                       Update employe_table1 SET salary ={0} WHERE Name = '{1}'
                                                                 '''
                updateQuery = Query.format(self.salary, self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
        except InvalidBonus:
            print("Bonus should be greater than 0 and less than or equal to 2")

    def Update_salary(self):
        New_salary = int(input())
        if New_salary == self.salary:
            print("salary doesnot change")
        else:
            Query = '''
                        Update employe_table1 SET salary ='{0}' WHERE Name = '{1}'
                                                                                   '''
            updateQuery = Query.format(New_salary, self.Name)
            cursor.execute(updateQuery)
            cursor.commit()

    def Change_Project(self, project, Name):
        self.project = project
        self.Name = Name

        if self.project in self.projects:
            if self.project == self.project:
                print("Project is Already exists")
            else:
                Query = ''' Update employe_table1 SET Project ='{0}' WHERE Name = '{1}' 
                '''
                updateQuery = Query.format(self.project, self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")

    def Insert_valueto_Emp_ID(self, Emp_ID, Name):
        self.Name = Name
        self.Emp_ID = Emp_ID
        query = ''' Update employe_table1 SET Emp_ID='{0}' WHERE Name = '{1}' '''
        updateQuery = query.format(self.Emp_ID, self.Name)
        cursor.execute(updateQuery)
        cursor.commit()

    def Updating_column_value(self, salary, Name):
        self.salary = salary
        self.Name = Name
        query = ''' Update employe_table1 SET salary='{0}' WHERE Name = '{1}' '''
        updateQuery = query.format(self.salary, self.Name)
        cursor.execute(updateQuery)
        cursor.commit()

    def delete_row(self,Emp_ID ):
        query = ''' delete from employe_table1 WHERE Emp_ID='52130552' '''
        updateQuery = query.format(self.Name)
        cursor.execute(updateQuery)
        cursor.commit()


object = EmployeeNew("Nandu", 40000, "c")
#object.insert_Employee_Details()
# object.Display_Employee_Details()
# object. Add_Bonus(2)
# object.Update_salary()
# object.Change_Project("python",'cerdo')
#object.Insert_valueto_Emp_ID(52130979, 'Nandu')
# object.Updating_column_value(60000,'vyshu')
object.delete_row(52130552)
