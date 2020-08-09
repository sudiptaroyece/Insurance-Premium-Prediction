from flask import Flask, url_for, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

from insurance.dataattributes.views import dataattr_blueprint

def create_app():
	with app.app_context():
		# Register Blueprints
		app.register_blueprint(dataattr_blueprint, url_prefix="/dataattributes")

		return app


@app.route('/')
def root():
	return redirect(url_for('dataattributes.predict_data'))

