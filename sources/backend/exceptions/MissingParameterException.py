from flask import make_response, jsonify
from werkzeug.exceptions import HTTPException


class MissingParameterException(HTTPException):
    """
    Exception personnalisée exprimant le manque d'un paramètre.
    :param description: Information concernant le paramètre manquant.
    """
    def __init__(self, description):
        self.code = 400
        self.description = description
        self.response = make_response(jsonify({"code": 'MISSING_PARAMETER', "desc": description}), self.code)
