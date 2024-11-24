from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta para el índice
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtiene los datos enviados desde el formulario
        name = request.form.get('name')
        age = int(request.form.get('age'))
        quantity = int(request.form.get('quantity'))

        # Define el precio por tarro y calcula descuentos
        price_per_can = 9000
        total = price_per_can * quantity

        if age > 30:
            discount = 0.25 * total
        elif 18 <= age <= 30:
            discount = 0.15 * total
        else:
            discount = 0

        final_total = total - discount

        # Renderiza la plantilla con los resultados
        return render_template('ejercicio1.html', name=name, total=total, discount=discount, final_total=final_total)

    # Muestra el formulario inicialmente
    return render_template('ejercicio1.html')

# Ruta para el ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    message = ""  # Variable para mostrar el mensaje al usuario
    if request.method == "POST":
        username = request.form.get("username")  # Obtiene el nombre del usuario
        password = request.form.get("password")  # Obtiene la contraseña

        # Validación de usuarios predefinidos
        if username == "juan" and password == "admin":
            message = "Bienvenido Administrador juan"
        elif username == "pepe" and password == "user":
            message = "Bienvenido Usuario pepe"
        else:
            message = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
