from flask import Blueprint, request
from ..services import hello_service as service
from ..schemas.hello_schema import hello_schema, hello_list_schema

bp = Blueprint('hello', __name__, url_prefix='/hello')


@bp.route('/')
def get_hello_list():
    return hello_list_schema.jsonify(service.get_hello_list())


@bp.route('/<name>')
def save_hello(name):
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers['X-Forwarded-For']
    else:
        ip = request.remote_addr
    return hello_schema.jsonify(service.save_hello(name, ip)), 201
