from flask import Blueprint, render_template, redirect, url_for, jsonify
from flask_login import login_required
import subprocess
import os
from app.scripts.publicpositions import get_public_positions
# from app.scripts.capital_accounts_automated import capital_accounts_automated
# import nbformat
# from nbclient import NotebookClient

bp = Blueprint('main', __name__)

# UPLOAD_FOLDER = 'app/uploads'

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/loadPositions')
@login_required
def loadPositions():
    return render_template('publicPositions.html')

@bp.route('/fetch-public-positions', methods=['POST'])
def fetch_public_positions():
    data = get_public_positions()
    return jsonify(data)

@bp.route('/automations')
@login_required
def automations():
    return render_template('automations.html')