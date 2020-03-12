from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from model.apps import EmployedSchema, Employed
import config

app = Flask(__name__)
CORS(app)


@app.route('/employed')
def employed():
    employed_schema = EmployedSchema()
    employed = Employed.query.all()
    output_json = employed_schema.dump(employed).data
    return {
        'data': output_json
    }


app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI

db = SQLAlchemy(app)
db.reflect()
ma = Marshmallow(app)

if __name__ == '__main__':
    app.run()
