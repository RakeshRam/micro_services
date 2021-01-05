from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.sqlite3"
CORS(app)

try:
    from db import db, Character
except: # TODO fix circular imports
    from .db import db, Character
    
db.init_app(app)    

@app.route('/')
def index():
    return render_template('main.html', characters=Character.query.all())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')