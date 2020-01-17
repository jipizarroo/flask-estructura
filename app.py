import os
from flask import Flask, render_template, jsonify, request
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db
from family import Family

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db')   #RUTA DE BASE DE DATOS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
CORS(app)

fam = Family("Pizarro")

@app.route('/')
def home(): 
    return render_template('index.html', name="home")

@app.route('/family', methods=['GET', 'POST'])
@app.route('/family/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def members(id = None):
    if request.method == 'GET':
        if id is not None:
            member = fam.get_member(id)
            if member:
                return jsonify(member), 200
            else:
                return jsonify({"msg": "Not Found"}), 404
        else:
        #members = Member.query.all()
            members = fam.get_all_members()
        # members = list(map(lambda member: member.serialize(), members)) #serialize convierte el objeto python a un array para poder trabajar en json.
        return jsonify(members), 200
    if request.method == 'POST':
        if not request.json.get('name'):
            return jsonify({"name": "is required"}), 422
        if not request.json.get('age'):
            return jsonify({"age": "is required"}), 422
        
        fam._name = request.json.get('name')
        fam._age = request.json.get('age')

        member = fam.add_member(fam)
        return jsonify(member), 200
    if request.method == 'PUT':
        if not request.json.get('name'):
                return jsonify({"name":"Is required"}),422
        if not request.json.get('age'):
                return jsonify({"age":"Is required"}),422
        
        newUpdate = {
            "name":request.json.get("name"),
            "age":request.json.get("age")
        }
        member = fam.update_member(id,newUpdate)
        return jsonify(member), 200
if __name__ == "__main__":
    manager.run()
