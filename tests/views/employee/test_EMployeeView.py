from app.model.EmployeeModel import EmployeeModel
from app.views.employee.EmployeeView import AnimalsView

def test_get_employee(test_app, mocker):
    # arrange
    mock_employee_data = {
        "name" : "Meirth MH",
        "role" : "CEO",
        "schedule" : "night"
    }
    mocker.patch.object(AnimalsView, "get", return_value=mock_employee_data)

    # act
    with test_app.test_client() as client:
        response = client.get("/employee/1")

    # assert
    assert response.status_code == 200

def test_update_employee(test_app, mocker):
    # arrange
    update_employee_data = {
        "name" : "Meirth MH",
        "role" : "CEO",
        "schedule" : "morning"
    }
    mocker.patch.object(AnimalsView, 'put', return_value=update_employee_data)

    # act
    with test_app.test_client() as client:
        response = client.put("employee/1", json=update_employee_data)

    # assert
    assert response.status_code == 200

def test_deleted_employee(test_app, mocker):
    # arrange
    expected_response = "employee doesn't exist"
    mocker.patch.object(AnimalsView, 'delete', return_value=expected_response)
    
    # act
    with test_app.test_client() as client:
        response = client.delete("/employee/123")
    
    # assert
    assert response.status_code == 200