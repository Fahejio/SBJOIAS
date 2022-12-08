from flask import Flask, request, render_template

###Rotas
@app.route('/Perfil(DP)')
def galeria():
    return render_template("Perfil(DP).html")