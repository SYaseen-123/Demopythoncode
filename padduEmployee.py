import pyodbc

import Schema_1
#from Schema_1 import Employee_schema
server = 'HCL-02-24\SQLEXPRESS'
database = 'SearchEngine'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Existing(Exception):
    pass
class Not_in_Range(Exception):
    pass
class Employees_data:
    Bonus=2
    Projects=['Python','C','Java']
    def _init_(self,Name,Salary,Project):
        self.Name=Name
        self.Salary=Salary
        self.Project=Project
    def insert_values_in_table(self):
        query = '''  
                            INSERT INTO Employee_details (Name, Salary, Project)
                            VALUES
                            ('{0}',{1},'{2}')  '''

        insertQuery = query.format(self.Name, self.Salary, self.Project)
        cursor.execute(insertQuery)
        #query_4 = cursor.execute('''select * from Employee_details''')

        cnxn.commit()
    def Update_Salary(self,New_Salary,Name):
        try:
            self.New_Salary = New_Salary
            self.Name=Name
            if self.New_Salary != self.Salary:
                fileinfoQuery = '''
                                                Update Employee_details SET Salary ='{0}' WHERE Name = '{1}'
                                                '''
                updateQuery = fileinfoQuery.format(New_Salary,self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise Existing
        except Existing:
            print("No Change in Salary")
    def Add_Bonus(self,bonus,Name):
        self.bonus=bonus
        self.Name=Name
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise Not_in_Range
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''
                        Update Employee_details SET Salary ='{0}' WHERE Name = '{1}'
                                                                '''
                updateQuery = Query.format(self.Salary, self.Name)
                cursor.execute(updateQuery)
                cursor.commit()
        except Not_in_Range:
            print("Bonus is Not in Range")
    def Change_Project(self,project,Name):
        self.project=project
        self.Name=Name

        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update Employee_details SET Project ='{0}' WHERE Name = '{1}' '''
                updateQuery = Query.format(project, Name)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")
    def Display_details(self):
        query=''' select * from Employee_details WHERE Name='{0}' '''
        query1=query.format(self.Name)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0}  Salary:{1}  Project:{2}".format(details.Name , details.Salary , details.Project))










obj1=Employees_data('Padmavathi',30000,'Python')
obj=Schema_1.Employee_schema()
obj.Employee_table()
#obj1.Add_Bonus(2,'padmavathi')
#obj1.insert_values_in_table()
obj1.Update_Salary(35000,'Vyshnavi')
obj1.Add_Bonus(2,'Vyshnavi')
obj1.Change_Project('Java','Suresh')
obj1.Display_details()

#obj1=Employees_data('Padmavathi',30000,'Python')