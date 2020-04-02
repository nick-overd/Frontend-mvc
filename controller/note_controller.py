from flask import request, render_template
from controller import app, AlchemyEncoder
from model import db
from model.note import Note
import json

@app.route("/", methods=["GET"])
def home_page():
    return render_template("home.html", title = "Home")

@app.route("/about", methods=["GET"])
def about_page():
    return render_template("about.html", title = "About")


@app.route("/note", methods=["POST"])
def added():
    noteData = request.json
    print(noteData) 
    # hard coding the database
    # note = Note(id = 2, text = "first")
    note = Note(**noteData)
    db.session.add(note)
    db.session.commit()
    return "added"

@app.route("/note/<note_id>", methods=["GET"])
def get_by_id(note_id):
    note = db.session.query(Note).filter(Note.id == note_id).first()
    return render_template("note.html", title = "Note", note = note)

# @app.route("/note/<notebook_id>", methods=["GET"])
# def get_by_id(notebook_id):
#     note = db.session.query(Note).filter(Note.notbook_id == notebook_id).all()
#     return json.dumps(note, cls=AlchemyEncoder)


@app.route("/note", methods=["GET"])
def get_all():
    notes = db.session.query(Note).all()
    return render_template("notes.html", title="My Notes", notes=notes)

@app.route("/note", methods=["PATCH", "PUT"])
def update():
    note_Data = request.json
    note = db.session.query(Note).filter(Note.id==note_Data["id"]).first()
    note.text = note_Data["text"]
    db.session.commit()
    return json.dumps(note, cls=AlchemyEncoder)


@app.route("/note/remove/<id>", methods=["POST"])
def delete(id):
    note = db.session.query(Note).filter(Note.id==id).first()
    db.session.delete(note)
    db.session.commit()
    return "deleted"
 

@app.route("/notes")
def take_notes():
    return "note note note note note"


