from flask import Flask, render_template, jsonify, abort
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.sqlite3"
CORS(app)

try:
    from db import db, Character, User
    from producer import publish
except: # TODO fix circular imports !!!
    from .db import db, Character, User
    from .producer import publish
    
db.init_app(app)    

@app.route('/')
def index():
    return render_template('main.html', characters=Character.query.all())

@app.route('/character/<int:uid>/<int:id>/vote', methods=['POST'])
def like(uid, id):
    try:
        user = User.query.get(uid)
        user.character_id = id
        db.session.commit()
        publish('character_vote', id)
    except Exception as e:
        print(str(e))
        abort(400, 'You already voted for this character.')

    return jsonify({
        'message': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')