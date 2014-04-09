from hashlib import sha256

from flask.ext.restful import Resource, Api, reqparse
from labauth import app

from labauth.models import Human, Machine

api = Api(app)

class UserResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('machine_token', type=str, required=True)
        parser.add_argument('user_token', type=str, required=True)
        
        args = parser.parse_args()
        
        # authenticate machine
        machine_obj = Machine.query.filter(
            Machine.token_hash == sha256(args.machine_token).hexdigest()
        ).first()
        if machine_obj is None:
            return {
                'error_msg': 'Machine not authenticated'
            }, 401
        
        # authenticate user
        user_obj = Human.query.filter(
            Human.token_hash == sha256(args.user_token).hexdigest()
        ).first()
        if user_obj is None:
            return {
                'error_msg': 'No user with specified Token.'
            }, 404
        
        return {
            'username': user_obj.username,
            'email': user_obj.email
        }

api.add_resource(UserResource, '/')
