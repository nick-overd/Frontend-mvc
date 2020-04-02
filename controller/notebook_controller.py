from flask import request
from controller import app, AlchemyEncoder
from model import db
from model.notebook import Notebook
import json

@app.route("/notebook", methods=["POST"])
def add_notebook():
    notebook_Data = request.json
    print(notebook_Data) 
    notebook = Notebook(**notebook_Data)
    db.session.add(notebook)
    db.session.commit()
    return "added"

@app.route("/notebook/<id>", methods=["GET"])
def get_by_notebook_id(id):
    notebook = db.session.query(Notebook).filter(Notebook.id == id).first()
    return json.dumps(notebook, cls=AlchemyEncoder)

@app.route("/notebook", methods=["GET"])
def get_all_notebook():
    notebooks = db.session.query(Notebook).all()
    print(notebooks)
    return json.dumps(notebooks, cls=AlchemyEncoder)


@app.route("/notebook", methods=["PATCH", "PUT"])
def update_notebook():
    notebook_Data = request.json
    notebook = db.session.query(Notebook).filter(Notebook.id==notebook_Data["id"]).first()
    notebook.text = notebook_Data["text"]
    db.session.commit()
    return json.dumps(notebook, cls=AlchemyEncoder)

setattr
@app.route("/notebook/<id>", methods=["DELETE"])
def delete_notebook(id):
    notebook = db.session.query(Notebook).filter(Notebook.id==id).first()
    db.session.delete(notebook)
    db.session.commit()
    return "deleted"


# #query
# @app.route("/note", methods=["PATCH", "PUT"])
# def update():
#     print(request.args)
#     return request.args

    
# #path and body
# @app.route("/notes/<id>", methods=["DELETE"])
# def delete(id):
#     print(int(id))
#     print(request.json)
#     return request.json
 