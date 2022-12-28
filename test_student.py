from student import student
import unittest


class test_assert(unittest.TestCase):
    def setUp(self):
        #self.somevalue=somevalue
        print("\nsetup")
        self.std1=student("yaseen","shaik",80)
    def tearDown(self):
        print("\nteardown")

    def test_email(self):
        print("email")
        self.std1 = student("yaseen", "shaik", 57)
        print("testemail")
        self.assertEqual(self.std1.email(),"yaseen.shaik@gmail.com")
    def test_fullname(self):
        self.assertEqual(self.std1.fullname(),"yaseen shaik")
    def test_apply_bonus(self):
        std1=student("duyrh","oiy8t",78)
        std1.apply_bonus()
        print("testbonus")
        self.assertEqual(std1.marks,90,90)
    def test_something(self):
        std1 = student("yaseen", "shaik", 57)
        self.assertEqual(std1.somevalue,"")
        self.std1.something()


#obj=test_assert()
#obj.setUp("hi")
if __name__=="__main__":
    unittest.main()