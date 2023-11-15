from flask import Blueprint, jsonify, redirect, url_for


api = Blueprint("API", __name__, url_prefix='/api')


@api.get('/')
def redirect_status():
    return redirect(url_for('index'))