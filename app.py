from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #Agregar una nueva página a su aplicación web creando una nueva ruta
def index():
    return render_template('PageNode.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
