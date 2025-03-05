from flask import Flask, request, render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulari():
    if request.method == 'POST':
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("retorno_hero.html")
        tipus = request.form['tipus']
        nom = request.form['nom']
        atac = request.form['atac']
        defensa = request.form['defensa']
        moviment = request.form['moviment']
        cos = request.form['cos']
        ment = request.form['ment']
        habilitats = request.form['habilitats']
        info = {"tipus":tipus, "nom":nom, "atac":atac, "defensa":defensa, "moviment":moviment, "cos":cos, "ment":ment, "habilitats":habilitats}

        #  Aqui retorna la pagina html amb el resultat
        textFinal = template.render(info)
        return textFinal
    else:# Aqui et dona la pagina html amb el formulari
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("formulari1.html")
        return template.render()

if __name__ == '__main__':
    app.run(debug=True)
