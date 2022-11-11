from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from flask_cors import CORS


app = Flask(__name__)
spec = FlaskPydanticSpec('Mateus', title='Batata')
spec.register(app)
CORS(app)