import pytest
from app.model.AnimalModel import AnimalModel
from app.views.animal.AnimalsView import AnimalsView
from app.schema.AnimalsSchemas import AnimalSchemas

def test_get_animals(test_app, mocker):
    """get animals list success"""
    # Arrange
    mock_animals_data = [
        AnimalModel(name="kitty gallore", age=9, gender="male", species="mammals", special_requirements="medication"),
        AnimalModel(name="doggy", age=9, gender="male", species="mammals", special_requirements="medication")
    ]
    mocker.patch.object(AnimalsView, "get", return_value=mock_animals_data)

    # Act
    with test_app.test_request_context():
        get_animals_list = AnimalsView().get()

    # Assert
    assert len(get_animals_list) == 2
    assert get_animals_list[0].name == "kitty gallore"
    assert get_animals_list[1].name == "doggy"

def test_create_animals(test_app, mocker):
    """cretae animals list success"""
    # arrange
    mock_animals_data = {
        "name" : "kitty",
        "age" : 8,
        "gender" : "female",
        "species" : "mammals",
        "special_requirements" : "medication"
    }
    mocker.patch.object(AnimalsView, "post", return_value=mock_animals_data)
    
    # act
    with test_app.test_request_context():
        create_new_animal = AnimalSchemas().load(mock_animals_data)
        post_new_animal = AnimalsView().post(create_new_animal)

    # assert
    # expected_response = {
    #     "name" : "kitty",
    #     "age" : 8,
    #     "gender" : "female",
    #     "species" : "mammals",
    #     "special_requirements" : "medication"
    # }
    assert post_new_animal["name"] == "kitty"
    assert post_new_animal["age"] == 8
