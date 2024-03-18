class Role:
    def __init__(self, name, description, monthly_salary_factor):
        self.__name = name
        self.__description = description
        self.__monthly_salary_factor = monthly_salary_factor

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def monthly_salary_factor(self):
        return self.__monthly_salary_factor


    @monthly_salary_factor.setter
    def monthly_salary_factor(self, monthly_salary_factor):
        self.__monthly_salary_factor = monthly_salary_factor
