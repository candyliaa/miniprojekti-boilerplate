from db_helper import reset_db, setup_db
from setup import app

def setup_database():
    with app.app_context():
      setup_db()
      print("setup db")

setup_database()