class Employee:
    def AcceptEmp(self):
        self.Id=int(input("enter emp id:"))
        self.Name=input("enter emp name:")
        self.Dept=input("enter emp dpt:")
        self.Sal=int(input("enter emp salary:"))
    def DisplayEmp(self):
        print("Emp id:",self.Id)
        print("Emp Name:",self.Name)
        print("Emp Dept:",self.Dept)
        print("Emp salary:".self.sal)
class Manager(Employee):
    def AcceptMgr(self):
        self