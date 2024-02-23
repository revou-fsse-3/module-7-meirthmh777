from app.model.EmployeeModel import EmployeeModel


# I want to make sure if the AnimalModel code behaves as expected
def test_create_new_arrival_employee():
    new_employee = EmployeeModel(name="margaret", role="zoo keeper", schedule="morning")
    assert new_employee.name == "margaret"
    assert new_employee.role == "zoo keeper"
    assert new_employee.schedule == "morning"

def test_update_employee():
    employee = EmployeeModel(name="Max", role="amphibians keeper", schedule="afternoon")
    employee.update(name="Max", role="mammals keeper", schedule="morning")
    assert employee.role == "mammals keeper"
    assert employee.schedule == "morning"

def test_employee_role_invalid():
    try:
        employee = EmployeeModel(name="Max", role=None, schedule="afternoon")
        assert False
    except:
        assert True

def test_employee_name_null():
    employee = EmployeeModel(name="Max", role="amphibians keeper", schedule="afternoon")
    employee.update(name="Max", role=None, schedule="afternoon")
    assert employee.role == None

    