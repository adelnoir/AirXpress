from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Banco de dados e tabelas
conn = sqlite3.connect("airxpress.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS voos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                origem TEXT NOT NULL,
                destino TEXT NOT NULL,
                data DATE NOT NULL,
                capacidade INTEGER NOT NULL
                    )
                ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
                    )
                ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                voo_id INTEGER NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (voo_id) REFERENCES voos(id)
                    )
                ''')
conn.commit()
conn.close()

@app.route('/voos', methods=['POST'])
def add_voo():
    origem = request.form['origem']
    destino = request.form['destino']
    data = request.form['data']
    capacidade = request.form['capacidade']

    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO voos (origem, destino, data, capacidade) VALUES (?, ?, ?, ?)",
                   (origem, destino, data, capacidade))
    conn.commit()
    conn.close()
    return redirect(url_for('get_voos'))

# Rota para listar voos
@app.route('/voos', methods=['GET'])
def get_voos():
    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM voos")
    voos = cursor.fetchall()
    conn.close()
    return render_template("voos.html", voos=voos)

#Rota para remover voo
@app.route('/voos/<int:id>', methods=['POST'])
def delete_voo(id):
    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()

    # Remover voo pelo ID
    cursor.execute("DELETE FROM voos WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    # Redirecionar para a lista de voos
    return redirect(url_for('get_voos'))

# Rota para adicionar voo
@app.route('/clientes', methods=['POST'])
def add_cliente():
    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()
    nome = request.form['nome']
    email = request.form['email']
    cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?)",
                   (nome, email
                    ))
    conn.commit()
    conn.close()
    return redirect(url_for('get_clientes'))

@app.route('/clientes', methods=['GET'])
def get_clientes():
    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return render_template("clientes.html", clientes=clientes)

@app.route('/clientes/<int:id>', methods=['POST'])
def delete_cliente(id):
    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()

    # Remover cliente pelo ID
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    # Redirecionar para a lista de clientes
    return redirect(url_for('get_clientes'))

@app.route('/reservas', methods=['POST'])
def add_reserva():
    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()
    cliente_id = request.form['cliente_id']
    voo_id = request.form['voo_id']
    cursor.execute("INSERT INTO reservas (cliente_id,voo_id) VALUES (?,?)",
                   (cliente_id,voo_id
                    ))
    conn.commit()
    conn.close()
    return redirect(url_for('get_reservas'))

@app.route('/reservas', methods=['GET'])
def get_reservas():
    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservas")
    reservas = cursor.fetchall()
    conn.close()
    return render_template("reservas.html", reservas=reservas)

@app.route('/reservas/<int:id>', methods=['POST'])
def delete_reserva(id):
    conn = sqlite3.connect("airxpress.db")
    cursor = conn.cursor()

    # Remover cliente pelo ID
    cursor.execute("DELETE FROM reservas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    # Redirecionar para a lista de clientes
    return redirect(url_for('get_reservas'))

# Página inicial
@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
