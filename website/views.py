# Create website route. Except Login, Logout and Sign Up page (This should be in 'auth.py').
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# views, url_prefix='/'
# If we want to access to the home page, URL: https://localhost/xxx
views = Blueprint('views', __name__)


@views.route('', methods=['GET', 'POST'])
@views.route('/', methods=['GET', 'POST'])
@login_required  # If user logged in, user may access to the home page.
def home():
    # If the user add a note
    if request.method == 'POST':
        # Get the note from frontend.
        note = request.form.get('note')

        # Check if the content is too short
        if len(note) <= 1:
            flash('Note is too short!', category='error')
        else:
            # Add new note to database
            new_note = Note(content=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()

            flash('Note added!', category='success')

    # Show Home page and transfer user to the frontend.
    return render_template('index.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def del_note():
    # Get the note that user want to delete.
    # Data is from index.js.
    note = json.loads(request.data)
    # Extract note's id
    note_id = note['noteId']
    # Use note's id to find the record
    found = Note.query.get(note_id)

    # If the record exist
    if found:
        if found.user_id == current_user.id:
            # Delete
            db.session.delete(found)
            db.session.commit()

    return Jsonify({})
