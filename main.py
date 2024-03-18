from Employee import Employee
from Role import Role

if __name__ == '__main__':


    engineer_role = Role("Engineer", "Develops software.", 1.2)
    manager_role = Role("Manager", "Manages projects.", 1.5)

    employee1 = Employee("Alice", "EMP123", "Engineering", "2020-01-01", "Software Engineer", 5000, engineer_role)
    employee2 = Employee("Bob", "EMP456", "Product", "2019-05-04", "Product Manager", 7000, manager_role)

    employee1.get_bonus()
    employee2.get_bonus()

    employee1.print_employee()
    employee2.print_employee()



