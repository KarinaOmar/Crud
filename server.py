from flask import Flask, render_template, request, redirect

from users import User #Importando la clase User para poder utilizar sus funciones

app = Flask(__name__)

@app.route('/')
def index():
    users= User.muestra_usuarios()
    return render_template('index.html', usuarios=users)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    #Recibimos el formulario a través de una variable llamada request.form
    #request.form = {"first_name":"Juana", "last_name":"De Arco", "email":"juana@cd.com"}
    User.guardar(request.form)
    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    formulario = {"id" : id} #diccionario con nombre de variable formulario
    User.borrar(formulario)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    formulario= {"id" : id}
    user = User.mostrar(formulario) #Instancia de usuario
    return render_template('edit.html', usuario = user)

@app.route('/update', methods=['POST'])
def update():
    #request.form= recibo diccionario con formulario de edit.html
    User.actualizar(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)