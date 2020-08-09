from flask import render_template, request, url_for, redirect, Blueprint, flash
import pickle as pkl
from sklearn.preprocessing import PolynomialFeatures


dataattr_blueprint=Blueprint(
	"dataattributes",
	__name__,
	template_folder="templates"
)

model  = pkl.load(open('PolyRegression_InsuranceKaggle_model.pkl','rb'))
poly=PolynomialFeatures(degree=3)
	# from flask import request
@dataattr_blueprint.route('/predict_data', methods=['GET','POST'])
def predict_data():
	
	if request.method == 'GET':
		return render_template('collect_parameter.html')

	elif request.method == 'POST':
		age = int(request.form['age'])
		sex = int(request.form['sex'])
		children = int(request.form['children'])
		region = int(request.form['region'])
		bmi = float(request.form['bmi'])
		smoker = int(request.form['smoker'])
		print([age,sex,children,bmi,smoker,region])
		
		x=poly.fit_transform([[age,sex,children,bmi,smoker,region]])
		prediction = model.predict(x)
		result=round(prediction[0],0)
		flash("Your Predicted Insurance Ammount will be: {0}".format(result))
	return render_template('collect_parameter.html')

