from app import app
from flask_sqlalchemy import SQLAlchemy

#connecting to database
# <db>+<driver>://<user>:<password>@<host>[:<port>]/<dbname>
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Pinkwine123@localhost:3306/notes"
db = SQLAlchemy(app)
