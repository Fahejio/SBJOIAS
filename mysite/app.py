from flask import Flask, request, render_template

app = Flask(__name__)
###Rotas
@app.route('/Perfil(dp)')
def Perfil():
    return render_template("Perfil(dp).html")