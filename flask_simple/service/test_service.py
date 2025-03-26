
from flask import jsonify
from flask_simple.db_service.db import db
from flask_simple.db_service.db_common_service import DBService
from flask_simple.commonutil.commonutil_service import CommonJsonResponse
from flask_bcrypt import Bcrypt
import logging



from flask_bcrypt import Bcrypt

bcrypt = Bcrypt() 

class TestServiceImpl:
    def test_func(self, data):  
        logging.info(f"Request:{data}")
        return CommonJsonResponse.common_response(
            status="success",
            message="User registered successfully",
            data = {"name":data.name,"email":data.email},
            status_code=200
        )
        