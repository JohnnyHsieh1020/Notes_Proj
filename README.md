# Flask_CRUD_2

### Feature:

- login
- logout
- sign up
- create note
- delete note

## Resources Used

**Python Version :** 3.8.2  
**IDE :** VSCode  
**Packages :**

- flask : Flask, render_template, url_for, redirect, request, flash, Blueprint, jsonify
- flask_login : login_user, login_required, logout_user, current_user, LoginManager, UserMixin
- werkzeug.security : generate_password_hash, check_password_hash
- sqlalchemy.sql : func
- flask_sqlalchemy : SQLAlchemy
- os : path
- json

**Reference documents or videos :**

1. https://youtu.be/dam0GPOAvVI

## Install packages

- Install Flask

```
pip3 install flask
```

- Install SQLAlchemy

```
pip3 install flask-sqlalchemy
```

- Install flask-login

```
pip3 install flask-login
```

## DataBase

1. Use SQLAlchemy to create a sqlite database.
2. Create User table, with 5 columns.
   - id(P-key)
   - first_name
   - email
   - password
   - notes
3. Create Note table, with 4 columns.
   - id(P-key)
   - content
   - date
   - user_id(F-key, ref to User-id)
