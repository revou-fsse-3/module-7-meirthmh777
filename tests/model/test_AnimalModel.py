from app.model.AnimalModel import AnimalModel


# I want to make sure if the AnimalModel code behaves as expected
def test_create_new_arrival_animal():
    new_animal = AnimalModel(name="margaret", age=2, gender="female", species="amphibians", special_requirements="none")
    assert new_animal.name == "margaret"
    assert new_animal.age == 2
    assert new_animal.gender == "female"
    assert new_animal.species == "amphibians"
    assert new_animal.special_requirements == "none"

def test_update_animal():
    animal = AnimalModel(name="Max", age=5, gender="Male", species="mammals", special_requirements="None")
    animal.update(name="Max", age=6, gender="Male", species="mammals", special_requirements="needs special diet")
    assert animal.age == 6
    assert animal.special_requirements == "needs special diet"

def test_update_age_invalid():
    try:
        animal = AnimalModel(name="Max", age="9", gender="Male", species="mammals", special_requirements="None")
        assert False
    except:
        assert True

def test_animal_name_null():
    animal = AnimalModel(name="Max", age=5, gender="Male", species="mammals", special_requirements="None")
    animal.update(name=None, age=6, gender="Male", species="mammals", special_requirements="needs special diet")
    assert animal.name == None

