# services/users/project/__init__.py

import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instanitate the db
db = SQLAlchemy()