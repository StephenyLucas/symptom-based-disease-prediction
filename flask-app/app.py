from flask import Flask, request, jsonify,json
import pickle
import ast
import numpy as np 
import pandas as pd


app = Flask(__name__)

l1= [
    'itching', 'skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills',
    'joint_pain','stomach_pain','acidity','ulcers_on_tongue','vomiting','fatigue','weight_gain','anxiety', 
    'cold_hands_and_feets','mood_swings','weight_loss','restlessness','cough','high_fever', 
    'breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin',  
    'dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes',
    'back_pain','constipation','abdominal_pain','mild_fever',
    'yellowing_of_eyes','swelling_of_stomach','blurred_and_distorted_vision','throat_irritation',
    'redness_of_eyes','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'puffy_face_and_eyes','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'depression','irritability','muscle_pain',
    'abnormal_menstruation','dischromic _patches','increased_appetite',
    'lack_of_concentration','visual_disturbances','stomach_bleeding','pus_filled_pimples',
    'blackheads','skin_peeling','blister'
]

dict2 = {0: 'Fungal infection', 1: 'Allergy', 2: 'GERD', 3: 'Chronic cholestasis', 4: 'Drug Reaction', 5: 'Peptic ulcer diseae', 6: 'AIDS', 7: 'Diabetes ', 8: 'Gastroenteritis', 9: 'Bronchial Asthma', 10: 'Hypertension ', 11: 'Migraine', 12: 'Cervical spondylosis', 13: 'Paralysis (brain hemorrhage)', 14: 'Jaundice', 15: 'Malaria', 16: 'Chicken pox', 17: 'Dengue', 18: 'Typhoid', 19: 'hepatitis A', 20: 'Hepatitis B', 21: 'Hepatitis C', 22: 'Hepatitis D', 23: 'Hepatitis E', 24: 'Alcoholic hepatitis', 25: 'Tuberculosis', 26: 'Common Cold', 27: 'Pneumonia', 28: 'Dimorphic hemmorhoids(piles)', 29: 'Heart attack', 30: 'Varicose veins', 31: 'Hypothyroidism', 32: 'Hyperthyroidism', 33: 'Hypoglycemia', 34: 'Osteoarthristis', 35: 'Arthritis', 36: '(vertigo) Paroymsal  Positional Vertigo', 37: 'Acne', 38: 'Urinary tract infection', 39: 'Psoriasis', 40: 'Impetigo'}

predictions = {}

@app.route("/api/predict", methods=['GET','POST'])
def hello_world():
	print(request)
	content_type = request.headers.get('Content-Type')
	print(content_type)
	# if(content_type=="application/json"):
	print(dir(request))
	data = request.get_data()
	data = data.decode('utf-8')
	data = ast.literal_eval(data)
	# dataframe = pd.read_csv(r"C:\Users\Stepheny Lucas\Desktop\Code Editors\a sem 5\w3\flask-app\training.csv")
	X = pd.DataFrame(index=[0], columns=l1)
	X.fillna(0, inplace = True)
	if not data["Symptoms 1"]=='':
		X[data["Symptoms 1"]] = 1
	if not data["Symptoms 2"]=='':
		X[data["Symptoms 2"]] = 1
	if not data["Symptoms 3"]=='':
		X[data["Symptoms 3"]] = 1
	if not data["Symptoms 4"]=='':
		X[data["Symptoms 4"]] = 1
	if not data["Symptoms 5"]=='':
		X[data["Symptoms 5"]] = 1
	print(X)

	
	file = open(r"C:\Users\Stepheny Lucas\Desktop\Code Editors\a sem 5\w3\flask-app\gnb_tree.pkl", "rb")
	gnb = pickle.load(file)
	file.close()
	pred1 = gnb.predict(X)
	print(dict2[pred1[0]])
	predictions["GNB"] = dict2[pred1[0]]
	

	file = open(r"C:\Users\Stepheny Lucas\Desktop\Code Editors\a sem 5\w3\flask-app\decision_tree.pkl", "rb")
	decision_tree = pickle.load(file)
	file.close()
	pred2 = decision_tree.predict(X)
	print(dict2[pred2[0]])
	predictions["decision_tree"] = dict2[pred2[0]]
	
	file = open(r"C:\Users\Stepheny Lucas\Desktop\Code Editors\a sem 5\w3\flask-app\knn.pkl", "rb")
	knn = pickle.load(file)
	file.close()
	pred3 = knn.predict(X)
	print(dict2[pred3[0]])
	predictions["KNN"] = dict2[pred3[0]]
	
	file = open(r"C:\Users\Stepheny Lucas\Desktop\Code Editors\a sem 5\w3\flask-app\random_forest.pkl", "rb")
	random_forest = pickle.load(file)
	file.close()
	pred4 = random_forest.predict(X)
	print(dict2[pred4[0]])
	predictions["random_forest"] = dict2[pred4[0]]

	return predictions
	# return "<p>Hello, World!</p>"

@app.route("/api/predictions", methods=['GET'])
def people():
	global predictions
	return predictions
