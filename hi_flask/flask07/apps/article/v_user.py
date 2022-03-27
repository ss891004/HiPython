

from flask import Blueprint, render_template,request,redirect,url_for
from .models import User

user_bp = Blueprint('bp_user', __name__,template_folder='../templates')

@user_bp.route("/get_user")
def get_user():
    return "ok~~~"
