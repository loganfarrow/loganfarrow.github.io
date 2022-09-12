from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('contact.html')

@app.route('/my-link/')
def my_link():
  with open('genes.vcf', 'r') as file:
    text = file.read()
    if text.find('rs397508165') != -1:
      print("A Pathogenic Cystic Fibrosis variation has been detected in your DNA Profile. Allow us to connect you with a genetic counselor")

  return "A Pathogenic Cystic Fibrosis variation has been detected in your DNA Profile. Allow us to connect you with a genetic counselor"


if __name__ == '__main__':
  app.run(debug=True)

