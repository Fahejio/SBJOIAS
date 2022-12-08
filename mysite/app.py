from flask import Flask,render_template

app = Flask(__name__)

###Rotas
@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/home.html')
def HomeB():
    return render_template('home.html')

@app.route('/Perfil(dp).html')
def Perfil():
    return render_template("Perfil(dp).html")

@app.route('/dadospessoais.html')
def dadospessoais():
    return render_template("dadospessoais.html")

@app.route('/Pedidos.html')
def Pedidos():
    return render_template("Pedidos.html")

@app.route('/senhaperfil.html')
def senhaperfil():
    return render_template("senhaperfil.html")

@app.route('/Endereço.html')
def Endereco():
    return render_template("./Endereço.html")

@app.route('/sacola.html')
def sacola():
    return render_template("sacola.html")

@app.route('/meus_favoritos.html')
def meus_favoritos():
    return render_template("meus_favoritos.html")

@app.route('/compra.html')
def compra():
    return render_template("compra.html")

@app.route('/finalizar_compra.html')
def finalizar_compra():
    return render_template("finalizar_compra.html")