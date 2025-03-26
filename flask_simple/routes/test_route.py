from flask import Blueprint, request, jsonify
from flask_pydantic import validate
from flask_simple.schemas.test_schema import test_schema
from flask_simple.service.test_service import TestServiceImpl

bp = Blueprint("test", __name__)


@bp.route("/test", methods=["POST"])
@validate()
def add_user(body: test_schema):
    user = TestServiceImpl()
    return user.test_func(body)
