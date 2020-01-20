from flask_restful import Resource, Api
from config import tienda
from services.service import Service


class Root(Resource):
    

    def get(self):
        root = {'Wlecome' : 'Ollivanders'}
        return root
