from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyBndwG3xeoZ_xiecS1AHlXNQCHWdXU4eXE",
    'authDomain': "epicturkey-6abfa.firebaseapp.com",
    'databaseURL': "https://epicturkey-6abfa.firebaseio.com",
    'projectId': "epicturkey-6abfa",
    'storageBucket': "epicturkey-6abfa.appspot.com",
    'messagingSenderId': "543046502770",
    'appId': "1:543046502770:web:3d69be495e5315804db5eb",
    'measurementId': "G-VB5FT6KYR6"
  }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


