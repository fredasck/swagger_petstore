import allure
import pytest

from pet_store_api.pet_store import Pet


@allure.severity(allure.severity_level.CRITICAL)
def test_create_valid_data():
    pet_data = {"id": 3000, "category": {"id": 0, "name": "Shih-TZU"}, "name": "Boss",
                "photoUrls": ["https://static01.nyt.com/images/2020/03/07/multimedia/07xp-marnie/07xp-marnie"
                              "-superJumbo.jpg?quality=90&auto=webp"],
                "tags": [{"id": 0, "name": "my_new_dog"}], "status": "available"}
    pet = Pet.create(pet_data)

    assert pet.response.status_code == 200, f"Status code isn\'t ok {pet.response.status_code}"
    assert pet.id == 3000, f"Incorrect id was assigned. For now {pet.id}"
    assert pet.category[
               'id'] == 0, f"The category name wasn\'t created. For now category_name is {pet.category['id']}"
    assert pet.category[
               'name'] == 'Shih-TZU', f"The category name wasn\'t created. For now category_name is {pet.category['name']}"

    assert pet.name == 'Boss', f"The pet name wasn\'t created. For now name is {pet.name}"
    assert pet.photoUrls[0] == "https://static01.nyt.com/images/2020/03/07/multimedia/07xp-marnie/07xp-marnie" \
                               "-superJumbo.jpg?quality=90&auto=webp", f"Incorrect url was " \
                                                                       f"added. For now" \
                                                                       f" {pet.photoUrls} "

    assert pet.tags[0]['id'] == 0, f"Incorrect tag_id was added. For now {pet.tags[0]['id']}"
    assert pet.tags[0]['name'] == 'my_new_dog', f"Incorrect tag_name was added. For now {pet.tags[1]['name']}"
    assert pet.status == 'available', f"The status wasn\'t created. For now status is {pet.status}"


@allure.severity(allure.severity_level.CRITICAL)
def test_update_valid_data():
    pet_data = {"id": 3000, "category": {"id": 0, "name": "Pug"}, "name": "Max", "photoUrls": [
        "https://images2.minutemediacdn.com/image/upload/c_crop,h_1191,w_2120,x_0,y_57/f_auto,q_auto,w_1100/v1554740850/shape/mentalfloss/64051-istock-685469924.jpg"],
                "tags": [{"id": 1, "name": "pugs_fun"}], "status": "pending"}
    pet = Pet.update(pet_data)
    assert pet.response.status_code == 200, f"Status code isn\'t ok {pet.response.status_code}"
    assert pet.id == 3000, f"Incorrect id was updated. For now {pet.id}"
    assert pet.category[
               'id'] == 0, f"The category name wasn\'t updated. For now category_name is {pet.category['id']}"
    assert pet.category[
               'name'] == 'Pug', f"The category name wasn\'t updated. For now category_name is {pet.category['name']}"
    assert pet.name == 'Max', f"The pet name wasn\'t updated. For now name is {pet.name}"
    assert pet.photoUrls[
               0] == "https://images2.minutemediacdn.com/image/upload/c_crop,h_1191,w_2120,x_0,y_57/f_auto,q_auto,w_1100/v1554740850/shape/mentalfloss/64051-istock-685469924.jpg", f"Incorrect url was " \
                                                                                                                                                                                    f"added. For now" \
                                                                                                                                                                                    f" {pet.photoUrls} "

    assert pet.tags[0]['id'] == 1, f"Incorrect tag_id was updated. For now {pet.tags[0]['id']}"
    assert pet.tags[0]['name'] == 'pugs_fun', f"Incorrect tag_name was updated. For now {pet.tags[1]['name']}"
    assert pet.status == 'pending', f"The status wasn\'t updated. For now status is {pet.status}"


@allure.severity(allure.severity_level.NORMAL)
def test_find_valid_data():
    pet = Pet.find(3000)
    assert pet.response.status_code == 200, f"Status code isn\'t ok {pet.response.status_code}"
    # Pet.delete(3000)


@allure.severity(allure.severity_level.CRITICAL)
def test_delete_valid_data():
    pet_data = {"id": 3000}
    Pet.create(pet_data)
    pet = Pet.delete(3000)
    assert pet.response.status_code == 200, f"Status code isn\'t ok {pet.response.status_code}"


@allure.severity(allure.severity_level.NORMAL)
def test_create_invalid_data():
    pet_data = {"id": "ASA8980DSF"}
    pet = Pet.create(pet_data)
    assert pet.response.status_code == 400, f"Status code isn\'t ok {pet.response.status_code}"

    with pytest.raises(ValueError) as e:
        pet_data2 = 34
        Pet.create(pet_data2)
        assert str(e.value) == 'Invalid data was used (create)'

    with pytest.raises(ValueError):
        assert Pet.update(None) == 'Invalid data was used (create)'


@allure.severity(allure.severity_level.NORMAL)
def test_update_invalid_data():
    pet_data = {"id": "21A"}
    pet = Pet.update(pet_data)
    assert pet.response.status_code == 400

    with pytest.raises(ValueError):
        pet_data2 = "4"
        assert Pet.update(pet_data2) == 'Invalid data was used (update)'

    with pytest.raises(ValueError):
        assert Pet.update(None) == 'Invalid data was used (update)'


@allure.severity(allure.severity_level.MINOR)
def test_find():
    with pytest.raises(ValueError):
        assert Pet.find('SF') == 'Invalid data was used (find)'
    with pytest.raises(ValueError):
        assert Pet.find(345.4) == 'Invalid data was used (find)'


@allure.severity(allure.severity_level.NORMAL)
def test_delete():
    with pytest.raises(ValueError):
        assert Pet.delete('a') == 'Invalid data was used (delete)'
    with pytest.raises(ValueError):
        assert Pet.delete(5.56) == 'Invalid data was used (delete)'


# @pytest.mark.parametrize("id_pet, expected_result",
#                          [(100, 200), (200, 200), (300, 200), (400, 200), (500, 200), (600, 200), (700, 200),
#                           (800, 200), (900, 200) ])
# def test_find_valid_data(id_pet, expected_result):
#
#     assert Pet.find(
#         id_pet).response.status_code == expected_result, f"Status code isn\'t ok {Pet.find(id_pet).status_code} "
