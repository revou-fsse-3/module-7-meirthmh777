import pytest
from app.model.EmployeeModel import EmployeeModel
from app.views.employee.EmployeesView import AnimalsView
from app.schema.EmployeesSchemas import EmployeeSchemas

def test_get_employees(test_app, mocker):
    """get employees list success"""
    # Arrange
    mock_employees_data = [
        EmployeeModel(name="employee1", role="CEO", schedule="morning"),
        EmployeeModel(name="employee2", role="CEO", schedule="morning")
    ]
    mocker.patch.object(AnimalsView, "get", return_value=mock_employees_data)

    # Act
    with test_app.test_request_context():
        get_employees_list = AnimalsView().get()

    # Assert
    assert len(get_employees_list) == 2
    assert get_employees_list[0].name == "employee1"
    assert get_employees_list[1].name == "employee2"

def test_create_employees(test_app, mocker):
    """cretae employees list success"""
    # arrange
    mock_employees_data = {
        "name" : "Meirth MH",
        "role" : "CEO",
        "schedule" : "night"
    }
    mocker.patch.object(AnimalsView, "post", return_value=mock_employees_data)
    
    # act
    with test_app.test_request_context():
        create_new_employee = EmployeeSchemas().load(mock_employees_data)
        post_new_employee = AnimalsView().post(create_new_employee)

    # assert
    assert post_new_employee["name"] == "Meirth MH"
    assert post_new_employee["role"] == "CEO"
