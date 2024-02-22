from app.model.AnimalModel import AnimalModel
from app.views.animal.AnimalView import AnimalsView

def test_get_animal(test_app, mocker):
    # arrange
    # mock_animal_data = AnimalModel(name="kitty gallore", age=9, gender="male", species="mammals", special_requirements="medication")
    mock_animal_data = {
        "name" : "kitty",
        "age" : 8,
        "gender" : "female",
        "species" : "mammals",
        "special_requirements" : "medication"
    }
    mocker.patch.object(AnimalsView, "get", return_value=mock_animal_data)

    # act
    with test_app.test_client() as client:
        response = client.get("/animal/1")

    # assert
    assert response.status_code == 200

def test_update_animal(test_app, mocker):
    # arrange
    update_animal_data = {
        "name" : "cat",
        "age" : 7,
        "gender" : "female",
        "species" : "mammals",
        "special_requirements" : "medication"
    }
    mocker.patch.object(AnimalsView, 'put', return_value=update_animal_data)

    # act
    with test_app.test_client() as client:
        response = client.put("animal/1", json=update_animal_data)

    # assert
    assert response.status_code == 200

def test_deleted_animal(test_app, mocker):
    # arrange
    expected_response = "Animal is deleted"
    mocker.patch.object(AnimalsView, 'delete', return_value=expected_response)
    
    # act
    with test_app.test_client() as client:
        response = client.delete("/animal/123")
    
    # assert
    assert response.status_code == 200