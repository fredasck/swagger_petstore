import requests
import logging


# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


def add_new_pet(pet_id, pet_name, category_id, category_name, photo_urls, tags_id, tags_name, status):
    request_data = {
        "id": pet_id,
        "name": pet_name,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "photoUrls": [
            photo_urls
        ],
        "tags": [
            {
                "id": tags_id,
                "name": tags_name
            }
        ],
        "status": status
    }
    return requests.post("https://petstore3.swagger.io/api/v3/pet",
                         headers={"accept": "application/xml", "Content-Type": "application/json"}, json=request_data)


def update_pet(pet_id, pet_name, category_id, category_name, photoUrls, tags_id, tags_name, status):
    request_data = {
        "id": pet_id,
        "name": pet_name,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "photoUrls": [
            photoUrls
        ],
        "tags": [
            {
                "id": tags_id,
                "name": tags_name
            }
        ],
        "status": status
    }
    return requests.put("https://petstore3.swagger.io/api/v3/pet",
                        headers={"accept": "application/xml", "Content-Type": "application/json"}, json=request_data)


def add_new_pet_2(pet_id, pet_name, category_id, category_name, photoUrls, tags_id, tags_name, status):
    request_data = {
        "id": pet_id,
        "name": pet_name,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "photoUrls": [
            photoUrls
        ],
        "tags": [
            {
                "id": tags_id,
                "name": tags_name
            }
        ],
        "status": status
    }

    print(request_data)
    return requests.post("https://petstore3.swagger.io/api/v3/pet",
                         headers={"accept": "application/json", "Content-Type": "application/json"}, json=request_data)


def get_pet_by_id(id):
    return requests.get(f'https://petstore3.swagger.io/api/v3/pet/{id}', headers={"accept": "application/xml"})


if __name__ == '__main__':
    pet = add_new_pet(10, 'doggie', 1, 'Dogs', 'string', 0, 'string', 'available')

    print(
        f"Create pet request status code is: {pet.status_code}.\n Headers: {pet.headers}.\n "
        f"Content: {pet.text}\n")
    update_pet = update_pet(11, 'doggse', 1, 'Dogs',
                            'https://www.interfax.ru/ftproot/textphotos/2020/11/24/foto700.jpg', 0, 'string',
                            'available')
    print(
        f"Update pet request status code is: {pet.status_code}.\n Headers: {pet.headers}.\n "
        f"Content: {pet.text}\n")
    pet_2 = add_new_pet_2(10, 'doggie', 1, 'Dogs', 'string', 0, 'string', 'available')
    print(
        f"Create pet_2  request status code is: {pet_2.status_code}.\n Headers: {pet_2.headers}.\n "
        f"Content: {pet_2.json()}\n")

    pet_by_id = get_pet_by_id(11)
    print(
        f"Pet by id status code is: {pet_by_id.status_code}. \n Headers: {pet_by_id.headers}.\n Content: {pet_by_id.text}\n")
