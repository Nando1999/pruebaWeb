# Importar las librerias

# from email.mime import application
from flask import Flask, abort, render_template


# Instanciar la aplicaicon
app = Flask(__name__)

#ruta principal
#Llamar a index.html en la ruta principal
@app.route('/')
def idex():
    return render_template('idex3.html')


# main del programa
if __name__ == '__main__':
    # debug = True, para reiniciar automatica el servidor
    app.run(debug=True)
