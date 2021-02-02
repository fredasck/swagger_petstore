import os

import pytest
import requests
import json
import logging

from _pytest.config import Config


# @pytest.fixture(scope='function', autouse=True)
# def logger(request):
#     log_file = logging.FileHandler(os.path.join('/', 'log', 'test_case.log'), 'a')
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(level1name)s - %(message)s')
#     log_file.setFormatter(formatter)
#     Config.logger = logging.getLogger(request.function.__name__)
#     Config.logger.setLevel(logging.DEBUG)
#     for hdlr in Config.logger.handlers[:]:
#         Config.logger.removeHandler(hdlr)
#     Config.logger.addHandler(log_file)


class Pet:

    def __init__(self):
        self.path = 'https://petstore3.swagger.io/api/v3/pet/'
        self.response = None
        self.data = {}
        self.headers = {'accept': 'application/json'}

    def __getattr__(self, name):
        return self.data[name]

    def make_request(self, method, pet_data, headers=None):
        if headers:
            self.headers.update(headers)

        if method == 'post':
            self.response = requests.post(self.path, data=json.dumps(pet_data), headers=self.headers)
            self.data = self.response.json()
        elif method == 'put':
            self.response = requests.put(self.path, data=json.dumps(pet_data), headers=self.headers)
            self.data = self.response.json()
        elif method == 'get':
            self.response = requests.get('%s%d' % (self.path, pet_data['id']), headers=self.headers)
        elif method == 'delete':
            self.response = requests.delete('%s%d' % (self.path, pet_data['id']), headers=self.headers)

    @staticmethod
    def create(body):
        if not isinstance(body, dict):
            raise ValueError('Invalid data was used (create)')

        pet = Pet()
        pet.make_request('post', body, {'content-type': 'application/json'})
        return pet

    @staticmethod
    def update(body):
        if not isinstance(body, dict):
            raise ValueError('Invalid data was used (update)')

        pet = Pet()
        pet.make_request('put', body, {'content-type': 'application/json'})
        return pet

    @staticmethod
    def find(id_pet):
        if not isinstance(id_pet, int):
            raise ValueError('Invalid data was used (find)')

        pet = Pet()
        pet.make_request('get', {'id': id_pet})
        return pet

    @staticmethod
    def delete(id_pet):
        if not isinstance(id_pet, int):
            raise ValueError('Invalid data was used (delete)')

        pet = Pet()
        pet.make_request('delete', {'id': id_pet})
        return pet