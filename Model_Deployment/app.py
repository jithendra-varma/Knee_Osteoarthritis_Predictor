#!/usr/bin/env python
import os
import sys

from flask import Flask, request, jsonify, send_file, render_template
from io import BytesIO
from PIL import Image, ImageOps
import base64
import urllib

import numpy as np
import scipy.misc
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os
import tensorflow as tf
import numpy as np
from tensorflow import keras
#from skimage import io



# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer




app = Flask(__name__)
 

# Load your trained model
 


@app.route("/")
@app.route("/first")
def first():
	return render_template('first_1.html')
    
@app.route("/login")
def login():
	return render_template('login_2.html')    
@app.route("/chart")
def chart():
	return render_template('chart_6.html')

@app.route("/performance")
def performance():
	return render_template('performance_5.html')


@app.route("/index",methods=['GET'])
def index():
	return render_template('upload_3.html')


@app.route("/upload", methods=['POST'])
def upload_file():
	print("Hello")
	try:
		img = Image.open(BytesIO(request.files['imagefile'].read())).convert('RGB')
		img = ImageOps.fit(img, (224, 224), Image.ANTIALIAS)
	except:
		error_msg = "Please choose an image file!"
		return render_template('upload_3.html', **locals())

	# Call Function to predict
	args = {'input' : img}
	out_pred, out_prob = predict(args)
	out_prob = out_prob * 100

	print(out_pred, out_prob)
	danger = "danger"
	if out_pred=="You Are Safe, But Do keep precaution":
		danger = "success"
	print(danger)
	img_io = BytesIO()
	img.save(img_io, 'PNG')

	png_output = base64.b64encode(img_io.getvalue())
	processed_file = urllib.parse.quote(png_output)

	return render_template('result_4.html',**locals())
def predict(args):
	img = np.array(args['input']) / 255.0
	img = np.expand_dims(img, axis = 0)

	model = 'knee.h5'
	# Load weights into the new model
	model = load_model(model)

	pred = model.predict(img)


	if np.argmax(pred, axis=1)[0] == 0:
		out_pred = ["Normal","No radiological findings of osteoarthritis",["-----","-----","-----","-----"],["-----","-----","-----"],["-----","-----","-----"]]
	elif np.argmax(pred, axis=1)[0] ==1:
		out_pred = ["Doubtful","Doubtful narrowing of joint space and possible osteophytic lipping.",
		["No damage revealed in X-Ray.","Somewhat damage to the Cartilage.","Slight narrowing in the space between the bones of the joint.","No development of bone spurs."],
		["No discomfort or pain.","Joint appears healthy.","Gait changes are unlikely."],
		["Eat healthy food consisting calcium and vitamins.","Acetaminophens (or) Over-the-counter (OTC) medications can often relieve the pain.","Need to do specific exercises to help build strength and mobility."]]
	elif np.argmax(pred, axis=1)[0] ==2:
		out_pred = ["Mild","Definite osteophytes and possible narrowing of joint space.",
		["Slight damage to the Cartilage.","Narrowing of the space in the joint and bone spurs.","Slight development of bone spurs.","No visible deformity at the ends of the bones."],
		["Stiffness and joint pain.","Area where the bones and tissues meet will start to harden.","Bone becomes thicker and denser."],
		["Taking pain relievers and attending physical therapy.","Wearing a knee brace designed to relieve pressure on the joint's surfaces.","Wearing shoe inserts to reduce stress on the knee."]]
	elif np.argmax(pred, axis=1)[0] ==3:
		out_pred = ["Moderate","Moderate multiple osteophytes, definite narrowing of joint space, small pseudo cystic areas with sclerotic walls and possible deformity of bone contour",
		["Some damage to Cartilage and other tissue.","A clear narrowing of the joint space.","Some development of bone spurs.","A possible deformity at the ends of the bones."],
		["Pain and discomfort during daily activities.","Early signs of joint inflammation.","Swelling and fluid build-up round the joint (Water on the knee)."],
		["Taking OTC pain relievers, such as acetaminophen.","Taking prescription pain relievers, such as oxycodone and codeine.","Receiving corticosteroid injections."]]
	elif np.argmax(pred, axis=1)[0] ==4:
		out_pred = ["Severe","Large osteophytes, marked narrowing of joint space,"
		" severe sclerosis and definite deformity of bone contour",
		["A severe narrowing of the joint space.","A significant development of bone spurs.","Clear damage to the cartilage.","A definite deformity at the ends of the bones."],
		["Stiffness in the joint and constant inflammation.","Less fluid and more friction in the joint.","Significant pain and discomfort even during simple movements."],
		["The cartilage is diminished or completely worn away.","Use pain relief medication. A cane, walker, or brace can help to stay mobile.","Knee replacement or realignment surgery."]]
	return out_pred, float(np.max(pred))
 
 

if __name__ == '__main__':
    app.run(debug=True)