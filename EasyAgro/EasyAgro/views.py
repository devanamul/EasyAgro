from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import project, crops
from django.core.files.storage import default_storage
from django.conf import settings 
import numpy as np
import cv2
import tensorflow as tf
import tensorflow_hub as hub
import os
from io import BytesIO
# from models import classify

def home(request):
	return render(request, "EasyAgro/home.html")

def signin(request):
	if request.method == 'GET':
		return render(request, "EasyAgro/login.html")
	elif request.method == 'POST' and 'login' in request.POST:
		u = request.POST.get('username')
		p = request.POST.get('pass')
		user = authenticate(username=u, password=p)
		if user is None:
			return render(request, "EasyAgro/login.html")
		else:
			login(request, user)
			return redirect('Dashboard')
	elif request.method == 'POST' and 'SignUp' in request.POST:
		username = request.POST.get('username')
		email = request.POST.get('email')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		password = request.POST.get('password')
		
		
		try:
			create_user = User.objects.create_user(
				username=username,
				email=email,
				first_name=first_name,
				last_name=last_name,
				password=password
				)
		except ValueError as e:
			error_message = str(e)
			return render(request, "EasyAgro/login.html", {'error_message': error_message})
		
		create_user.save()
		messages.success(request, 'Successfully registered!')
		return redirect('SignIn')




def dashboard(request):
	u = request.user
	projects = project.objects.filter(author=u)
	return render(request, "EasyAgro/dashboard.html", {'projects': projects})

def projectForm(request):
	if request.method == 'GET':
		return render(request, "EasyAgro/projectForm.html")
	elif request.method == 'POST':
		projectName = request.POST['projectName']
		landSize = request.POST['landSize']
		cropType = request.POST['CropType']
		u = request.user

		print(cropType)

		crop = crops.objects.get(name = cropType)

		newProject = project(author = u, crop = crop, name = projectName, area = landSize, status = 'Running')
		newProject.save()
		return redirect('ProjectForm')

def Project(request):
	return render(request, "EasyAgro/project.html")

def diseaseIdentification(request):
	if request.method == 'GET':
		return render(request, "EasyAgro/disease.html")

	elif request.method == 'POST':
		os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
		model_path = os.path.join(os.path.dirname(__file__), 'models', 'my_model.h5')
		model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer':hub.KerasLayer})

		uploaded_image = request.FILES['img']
		image_bytes = uploaded_image.read()

		image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
		print(image.shape)
		image = cv2.resize(image, (224, 224))
		image = np.array(image) / 255.0
		image = np.expand_dims(image, axis=0)

		prediction = model.predict(image)

		predicted_label = np.argmax(prediction)

		labels = {}
		labels[0] = "Early Blight"
		labels[1] = "Healthy"
		labels[2] = "Late Blight"

		result = labels[predicted_label]

		return render(request, "EasyAgro/disease.html", {'result': result})


