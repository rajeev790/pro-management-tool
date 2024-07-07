from app import app, db

if _name_ == '_main_':
    db.create_all()
    app.run(debug=True)