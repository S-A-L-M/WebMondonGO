from Config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_Main = Blueprint("routes_Main", __name__)

@routes_Main.route('/IndexMain', methods=['GET'])
def IndexMain():

    return render_template('/Main/Main.html')