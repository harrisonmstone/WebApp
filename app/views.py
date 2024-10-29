
# from flask import Blueprint, render_template, request, redirect, url_for, flash
# import nbformat
# from nbclient import NotebookClient

# main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return render_template('index.html')

# @main.route('/app/templates/index.html')
# def index():
#     return render_template('index.html')

# @main.route('run-notebook', method=['POST'])


from flask import Blueprint, render_template, redirect, url_for
import subprocess
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')