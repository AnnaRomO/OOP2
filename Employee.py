class Employee:
    def __init__(self, name, employee_id, department, hire_date, position, monthly_salary, role):
        self.__name = name
        self.__employee_id = employee_id
        self.__department = department
        self.__hire_date = hire_date
        self.__position = position
        self.__monthly_salary = monthly_salary
        self.__role = role

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Getters and Setters for ID
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getters and Setters for Department
    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        self.__department = department

    # Getters and Setters for Hire Date
    @property
    def hire_date(self):
        return self.__hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        self.__hire_date = hire_date

    # Getters and Setters for Position
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    # Getters and Setters for Monthly Salary
    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self.__monthly_salary = monthly_salary

    # Private method to calculate bonus
    def __calculate_bonus(self, factor):
        return self.__monthly_salary * factor

    # Public method to get and print bonus
    def get_bonus(self, factor):
        bonus = self.__calculate_bonus(factor)
        print(f'{self.__name}, you got {bonus} as the annual bonus.')

    # Method to print all employee details
    def print_employee(self):
        print(f'Name: {self.__name}, ID: {self.__employee_id}, Department: {self.__department}, '
              f'Hire Date: {self.__hire_date}, Position: {self.__position}, Monthly Salary: {self.__monthly_salary}')

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    # Modified to use monthly_salary_factor from the role object
    def __calculate_bonus(self):
        return self.__monthly_salary * self.__role.monthly_salary_factor

    # Updated to include role name and description in the output
    def get_bonus(self):
        bonus = self.__calculate_bonus()
        print(f'{self.__name}, you got {bonus} as the annual bonus.')

    # Updated to include role name and description
    def print_employee(self):
        print(f'Name: {self.__name}, ID: {self.__employee_id}, Department: {self.__department}, '
              f'Hire Date: {self.__hire_date}, Position: {self.__position}, '
              f'Monthly Salary: {self.__monthly_salary}, Role: {self.__role.name}, '
              f'Role Description: {self.__role.description}')
