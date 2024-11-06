from flask import Blueprint, render_template, redirect, url_for, jsonify
import subprocess
import os
from app.scripts.publicpositions import get_public_positions
# import nbformat
# from nbclient import NotebookClient

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/loadPositions')
def loadPositions():
    return render_template('publicPositions.html')

@bp.route('/fetch-public-positions', methods=['POST'])
def fetch_public_positions():
    data = get_public_positions()
    return jsonify(data)
    # return render_template('publicPositions.html', data=data)


# @bp.route('/runPositions', method=['POST'])
# def public_positions():
#     nb_path = 'notebooks/publicPositions.ipynb'
#     with open(nb_path) as f:
#         nb = nbformat.read(f, as_version=4)
#     client = NotebookClient(nb)
#     client.execute()

#     output = {}
#     for cell in 

# return render_template('publicPositions.html', results = nb['cell_numbers'])

# from flask import Blueprint, render_template, request, redirect, url_for, flash


# main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return render_template('index.html')

# @main.route('/app/templates/index.html')
# def index():
#     return render_template('index.html')

# @main.route('run-notebook', method=['POST'])
