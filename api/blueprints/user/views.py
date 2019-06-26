from flask import Blueprint
from flask_restful import Api
from api.blueprints.user.resources.user_resource import UserResource

# registers a new user blueprint
user = Blueprint('user', __name__,
                 url_prefix='/user', template_folder='templates')

user_api = Api(user)


# register all resources associated with the user blueprint
# do not forget the appended
user_api.add_resource(UserResource, '/api')
