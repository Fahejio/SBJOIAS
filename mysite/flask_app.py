
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://SBjoias:Squad6PI@SBjoias.mysql.pythonanywhere-services.com/SBjoias$default'
db = SQLAlchemy(app)
engine = sqlalchemy.create_engine('mysql://SBjoias:Squad6PI@SBjoias.mysql.pythonanywhere-services.com/SBjoias$default')
Session = sessionmaker(bind=engine)
session = Session()


class Produto(db.Model):
    CodigoProd = db.Column(db.Integer,primary_key=True)
    Descricao = db.Column(db.String(200))
    Nome = db.Column(db.String(150),nullable=False)
    Avaliacao = db.Column(db.String(100))
    Tipo = db.Column(db.String(30),nullable=False)
    Valor =db.Column(db.Float,nullable=False)
    Quantidade =db.Column(db.Integer)

    def to_json(self):
        return{"codigoProd":self.CodigoProd,"Descrição":self.Descricao,"Nome":self.Nome,
        "Avaliacao":self.Avaliacao,"Tipo":self.Tipo,"Valor":self.Valor,"Quantidade":self.Quantidade}

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

