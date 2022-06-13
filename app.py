import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Credit Card Lead Prediction')

@app.route('/predicao', methods=['POST'])
def predicao():
  Age = request.form['Age']
  Vintage = request.form['Vintage']
  Credit_Product = request.form['Credit_Product']

  array=[[str(Age), str(Vintage), str(Credit_Product)]]

  predicao = model.predict(array)

  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
