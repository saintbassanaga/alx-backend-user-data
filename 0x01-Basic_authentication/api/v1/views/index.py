#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort ,Response

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> Response:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> Response:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stat = {'users': User.count()}
    return jsonify(stat)

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> Response:
    """ GET api/v1/unauthorized
    """
    abort(401)

