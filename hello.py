from flask import Flask

app = Flask(__name__)

# Flask run levanta el servidor
# FLASK_APP es la variable de entorno que relaciona locations

# Los recursos en flask, se llaman rutas (endpoints), y para ello usaremos decoradores

# Recurso directorio raiz
@app.route('/')
def barra_directorio():
    return '¡Hola, mundo!'.upper()

@app.route('/bye')
def otro():
    return '¡Adios, mundo cruel!'


