import pandas as pd

class Employee:
    def __init__(self, name, id_, dept, passw, email, supervisor, permission):
        self.name = name
        self.id = id_
        self.dept = dept
        self.passw = passw
        self.email = email
        self.supervisor = supervisor
        self.permission = permission

    def get_employee(self):
        employee_dict = {'name': self.name,
                         'id': self.id,
                         'dept': self.dept,
                         'passw': self.passw,
                         'email': self.email,
                         'supervisor': self.supervisor,
                         'permission': self.permission}
        return employee_dict
