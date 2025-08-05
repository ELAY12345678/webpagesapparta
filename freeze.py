# freeze.py
from flask_frozen import Freezer
from app import app  # importa tu app Flask

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
