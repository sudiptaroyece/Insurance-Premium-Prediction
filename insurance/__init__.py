from flask import Flask, url_for, redirect
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

from insurance.dataattributes.views import dataattr_blueprint

def create_app():
	with app.app_context():
		# Register Blueprints
		app.register_blueprint(dataattr_blueprint, url_prefix="/dataattributes")

		return app


@app.route('/')
def root():
	return redirect(url_for('dataattributes.predict_data'))

