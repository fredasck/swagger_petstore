import allure
import pytest
from pet_store_api.pet_store_api_parametrize import get_pet_by_id, add_new_pet_2


# from alchemize import JsonListModel, Attr, JsonTransmuter


# class PetAddRequest(JsonListModel):
#     __mapping__ = {
#         'id': Attr('pet_id', int),
#         'name': Attr('pet_name', str),
#         'category_id': Attr('category_id', int),
#         'category_name': Attr('category_name', str),
#         'photoUrls': Attr('photo_urls', str),
#         'tags_id': Attr('tags_id', int),
#         'tags_name': Attr('tags_name', str),
#         'status': Attr('status', str)
#
#     }
#
#     def __init__(self, pet_id=None, pet_name=None, category_id=None, category_name=None, photo_urls=None, tags_id=None,
#                  tags_name=None, status=None, **attrs):
#         super().__init__(**attrs)
#         self.status = status
#         self.tags_name = tags_name
#         self.tags_id = tags_id
#         self.photo_urls = photo_urls
#         self.category_name = category_name
#         self.category_id = category_id
#         self.pet_name = pet_name
#         self.pet_id = pet_id
#
#
# class PetAddResponse(JsonListModel):
#     __mapping__ = {
#         'id': Attr('pet_id', int),
#         'name': Attr('pet_name', str),
#         'category_id': Attr('category_id', int),
#         'category_name': Attr('category_name', str),
#         'photoUrls': Attr('photo_urls', str),
#         'tags_id': Attr('tags_id', int),
#         'tags_name': Attr('tags_name', str),
#         'status': Attr('status', str)
#     }
#
#     def __init__(self, pet_id=None, pet_name=None, category_id=None, category_name=None, photo_urls=None, tags_id=None,
#                  tags_name=None, status=None, **attrs):
#         super().__init__(**attrs)
#         self.status = status
#         self.tags_name = tags_name
#         self.tags_id = tags_id
#         self.photo_urls = photo_urls
#         self.category_name = category_name
#         self.category_id = category_id
#         self.pet_name = pet_name
#         self.pet_id = pet_id

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("test_input, expected_result",
                         [(0, 200), (1, 200), (2, 200), (3, 200), (4, 200), (5, 200), (6, 200), (7, 200), (8, 200),
                          (9, 200),
                          (10, 200), (11, 200), (12, 200), (13, 200), (14, 200), (15, 200), (16, 200), (17, 200),
                          (18, 200), (19, 200), (20, 200), (21, 200), (22, 200), (23, 200), (24, 200),
                          (25, 200), (26, 200), (27, 200), (28, 200), (29, 200), (30, 200)])
def test_get_pet_id_status_code_is_200(test_input, expected_result):
    assert get_pet_by_id(
        test_input).status_code == expected_result, f"Status code isn\'t ok {get_pet_by_id(test_input).status_code}"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_input, expected_result",
                         [(1002, 404), (1005, 404), (1007, 404), (1008, 404), (1009, 404), (1010, 404), (1011, 404),
                          (1013, 404), (1015, 404), (1016, 404), (1017, 404), (1019, 404), (1020, 404), (2022, 404),
                          (2023, 404), (2024, 404), (2025, 404), (2026, 404),
                          (2027, 404), (2028, 404), (2029, 404), (2030, 404), (2031, 404), (2032, 404)])
def test_get_pet_id_status_code_is_404(test_input, expected_result):
    assert get_pet_by_id(
        test_input).status_code == expected_result, f"Status code isn\'t ok {get_pet_by_id(test_input).status_code}"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_input, expected_result",
                         [('test', 400), ('тест', 405), ('Ё', 400), ('~', 400), ('₴', 400), ('\'', 400),
                          ('$', 400), ('&', 400), ('^', 400), ('*', 400), ('(', 400),
                          (')', 400), ('-', 400), ('_', 400), ('=', 400), ('+', 400), ('[', 400), (']', 400),
                          ('{', 400), ('}', 400), (':', 400), ('<', 400), ('>', 400), (',', 400),
                          ('|', 400), ('†', 400), ('®', 400), ('¿', 400), ('✅', 400), ('😝', 400)])
def test_get_pet_id_status_code_is_400(test_input, expected_result):
    assert get_pet_by_id(
        test_input).status_code == expected_result, f"Status code isn\'t ok {get_pet_by_id(test_input).status_code}"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_input, expected_result",
                         [(' ', 405), ('', 405), (';', 405), ('?', 405), ('.', 405), ])
def test_get_pet_id_status_code_is_405(test_input, expected_result):
    assert get_pet_by_id(
        test_input).status_code == expected_result, f"Status code isn\'t ok {get_pet_by_id(test_input).status_code}"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_input, expected_result",
                         [((9222968140496970050, "doggie", 0, 'my_dog',
                            "https://thepetridish.my/wp-content/uploads/2020/03/doggo.jpg", 0, "dog_fun",
                            "available"),
                           ({'id': 9222968140496970050, 'category': {'id': 0, 'name': 'my_dog'},
                             'name': 'doggie',
                             'photoUrls': ['https://thepetridish.my/wp-content/uploads/2020/03/doggo.jpg'],
                             'tags': [{'id': 0, 'name': 'dog_fun'}], 'status': 'available'})),

                          ((9222968140496970050, "doggie", 0, 'string', "string", 0, "string", "available"),
                           ({'id': 9222968140496970050, 'category': {'id': 0, 'name': 'string'},
                             'name': 'doggie',
                             'photoUrls': ['string'],
                             'tags': [{'id': 0, 'name': 'string'}], 'status': 'available'}))])
def test_add_pet_data_is_added(test_input, expected_result):
    assert add_new_pet_2(
        *test_input).json() == expected_result, f"Error in data. For now {add_new_pet_2(*test_input).json()}, but " \
                                                f"should be{expected_result} "
    assert add_new_pet_2(
        *test_input).status_code == 200, f"Status code isn\'t ok {add_new_pet_2(*test_input).status_code}"


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("test_input, expected_result",
                         [(('-', '2', '3', '4', '5', '6', '7', '8'), 405),
                          (('', '', '', '', '', '', '', ''), 405),
                          (('text', '2', '3', '4', '5', '6', '7', '8'), 405),

                          ])
def test_add_pet_data_is_not_added(test_input, expected_result):
    assert add_new_pet_2(*test_input).status_code == expected_result, \
        f"Error is {add_new_pet_2(*test_input).json()}. " \
        f"For now {add_new_pet_2(*test_input).status_code}, " \
        f"but should be {expected_result} "
