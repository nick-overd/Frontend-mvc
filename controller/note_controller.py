from controller import app, AlchemyEncoder
from flask import request, render_template, redirect, url_for
from model import db
from model.note import Note
import json

@app.route("/", methods=["GET"])
def home_page():
    return render_template("home.html", title="Home")

@app.route("/about", methods=["GET"])
def about_page():
    return render_template("about.html", title="About")

@app.route("/note", methods=["GET"])
def get_notes():
    notes = db.session.query(Note).all()
    return render_template("notes.html", title="Notes", notes=notes)

@app.route("/note/<note_id>", methods=["GET"])
def view__single_note(note_id):
    note = db.session.query(Note).filter(Note.id == note_id).first()
    return render_template("note.html", title=note.text, note = note)

@app.route("/note", methods=["POST"])
def add_note():
    note_data = request.form
    note = Note(**note_data)
    db.session.add(note)
    db.session.commit()
    return redirect( url_for ( "get_notes" ) )

@app.route("/note/edit/<note_id>", methods=["GET"])
def edit_note(note_id):
    note = db.session.query(Note).filter(Note.id == note_id).first()
    return render_template("edit.html", title="Edit Note", note=note)

@app.route("/note/update", methods=["POST"])
def update_note():
    note_data = request.form
    note = db.session.query(Note).filter(Note.id == note_data["id"]).first()
    note.text = note_data["text"]
    db.session.commit()
    return redirect( url_for ( "get_notes" ) )

@app.route("/note/remove/<note_id>", methods=["POST"])
def delete_note(note_id):
    note = db.session.query(Note).filter(Note.id == note_id).first()
    db.session.delete(note)
    db.session.commit()
    return redirect( url_for ( "get_notes" ) )
