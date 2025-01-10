import os
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import pandas as pd
import logging

#dosyaların varlığını kontrol edelim
log_dir = 'var/log/orhanApi'
lib_dir = 'var/lib/orhanApi'

log_file = os.path.join(log_dir, 'debug.log')
lib_file = os.path.join(lib_dir, 'kullanicilar.csv')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
if not os.path.exists(lib_dir):
    os.makedirs(lib_dir)

if not os.path.exists(lib_file):
    pd.DataFrame(columns=['name', 'age', 'city']).to_csv(lib_file, index=False)


logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode='w')

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return {"message": "Merhabalar!"}, 200
class Users(Resource):
    def __init__(self):
        self.data = pd.read_csv(lib_file)
        
    def get(self):
        self.data = self.data.to_dict('records')
        return {'data': self.data}, 200
    
    def post(self):
        data_arg = reqparse.RequestParser()
        data_arg.add_argument("name", type=str)
        data_arg.add_argument("age", type=int)
        data_arg.add_argument("city", type=str)

        args = data_arg.parse_args()

        self.data = pd.concat([self.data, pd.DataFrame([args])], ignore_index=True)
        self.data.to_csv(lib_file, index=False)
        
        return {'message': 'Kayıt eklendi.'}, 200

    def delete(self):
        name = request.args.get('name')

        if name in self.data['name'].values:
            self.data = self.data[self.data['name'] != name]
            self.data.to_csv(lib_file, index=False)
            return {'message': 'Kayıt silindi.'}, 200
        else:
            return {'message': 'Kayıt bulunamadı.'}, 404

class Cities(Resource):
    def get(self):
        data = pd.read_csv(lib_file, usecols=[2])
        data = data.to_dict('records')
        return {'data': data}, 200

class Name(Resource):
    def get(self, name):
        data = pd.read_csv(lib_file)
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name:
                return {'data': entry}, 207
        return {'message': 'Bu isimde bir kayıt bulunamadı!'}, 405

class AddNumbers(Resource):
    def get(self):
        numbers = request.args.getlist('num', type=int)
        result = sum(numbers)
        return {'result': result}, 200

class MultiplyNumbers(Resource):
    def get(self):
        try:
            num1 = float(request.args.get('num1'))
            num2 = float(request.args.get('num2'))
        except (TypeError, ValueError):
            return {'error': 'Lütfen geçerli numaralar girin.'}, 400

        result = num1 * num2
        return {'result': result}, 200


api.add_resource(Home, '/')
api.add_resource(Users, '/users')
api.add_resource(Cities, '/cities')
api.add_resource(Name, '/<string:name>')
api.add_resource(AddNumbers, '/add_numbers')
api.add_resource(MultiplyNumbers, '/multiply_numbers')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5044)
