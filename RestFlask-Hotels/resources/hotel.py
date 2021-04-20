from flask_restful import Resource

hoteis = [
    {
        'hotel_id': 'alpha',
        'name': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'beta',
        'name': 'Beta Hotel',
        'estrelas': 4.7,
        'diaria': 390.99,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'gama',
        'name': 'Gama Hotel',
        'estrelas': 4.5,
        'diaria': 320.30,
        'cidade': 'Santa Catarina'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}