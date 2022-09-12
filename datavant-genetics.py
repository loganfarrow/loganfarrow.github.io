<<<<<<< HEAD
from django.shortcuts import render

import requests

def button(request):
    return render(request,'contact.html')

def output(request):
    return "testingnn"

def external(request):
    inp=request.POST.get('param')

=======
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  with open('genes.vcf', 'r') as file:
    text = file.read()
    if text.find('rs397508165') != -1:
      print("A Pathogenic Cystic Fibrosis variation has been detected in your DNA Profile. Allow us to connect you with a genetic counselor")

  return "A Pathogenic Cystic Fibrosis variation has been detected in your DNA Profile. Allow us to connect you with a genetic counselor"


if __name__ == '__main__':
  app.run(debug=True)
>>>>>>> 806376c7a27642e98d36faf6214c6b3b2251fff8
