from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Me trae del formulario el nombre num1
        num1 = float(request.form.get('num1'))
        print("ESTE ES MI NUMERO -----> ",num1)
        num2 = float(request.form.get('num2'))
        print ("ESTE ES MI NUMERO -----> ",num2)
        select= (request.form.get ('operation'))
        print ("OPERADOR ES -----> ",select)
        if select== "add" :
            result= num1 + num2
        elif select== "subtract" :
            result= num1 - num2
        elif select== "multiply" :
            result= num1 * num2
        elif select== "divide":
            result= num1 / num2
        print (result)
    return render_template('index.html', result=result)



if __name__ == '__main__':
    app.run(debug=True)
