from app import app
from utils.db import db

with app.app_context():
    db.createAll()

if __name__ == '__main__':
    app.run(debug=True)
