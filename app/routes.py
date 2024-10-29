from flask import Blueprint, render_template, redirect, url_for
import subprocess
import os
import nbformat
from nbclient import NotebookClient

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/public-positions', method=['POST'])
def public_positions():
    nb_path = 'notebooks/publicPositions.ipynb'
    with open(nb_path) as f:
        nb = nbformat.read(f, as_version=4)
    client = NotebookClient(nb)
    client.execute()

    return render_template('publicpositions.html', results = nb['cell_numbers'])

# from flask import Blueprint, render_template, request, redirect, url_for, flash


# main = Blueprint('main', __name__)

# @main.route('/')
# def index():
#     return render_template('index.html')

# @main.route('/app/templates/index.html')
# def index():
#     return render_template('index.html')

# @main.route('run-notebook', method=['POST'])
