from typing import Optional, Union, Dict, Any, Tuple
from flask import jsonify
from http import HTTPStatus
import datetime
import uuid

class CommonJsonResponse:
    """
    Standardized API Response Handler
    """
    
    @staticmethod
    def common_response(
                        status: str,
                        message: str = "",
                        data: Optional[Union[Dict, list, Any]] = None,
                        error: Optional[Dict] = None,
                        pagination: Optional[Dict] = None,
                        status_code: int = HTTPStatus.OK,
                        meta_data: Optional[Dict] = None
                    ):
        
        try:
            response = {
                "status": status.lower(),
                "message": message,
                "meta": {
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                    "request_id": str(uuid.uuid4()),
                    "status_code": status_code
                }
            }

            if data is not None:
                response["data"] = data

            if error is not None:
                response["error"] = error

            if pagination:
                response["meta"]["pagination"] = {
                    "current_page": pagination.get("current_page",0),
                    "limit": pagination.get("page_limit",0),
                    "total_records": pagination.get("total_records",0),
                    "total_pages": pagination.get("total_pages",0)
                }

            if meta_data:
                response["meta"].update(meta_data)

            return jsonify(response), status_code

        except Exception as e:
            error_response = {
                "status": "error",
                "message": "Internal server error while formatting response",
                "meta": {
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                    "request_id": str(uuid.uuid4()),
                    "error_details": str(e)
                }
            }
            return jsonify(error_response), HTTPStatus.INTERNAL_SERVER_ERROR
