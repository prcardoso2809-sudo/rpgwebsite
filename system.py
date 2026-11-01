from flask import Flask, redirect, request, url_for, render_template, session, flash
from db import db
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_BINDS'] = {
    'personagem_rpg_bind': 'sqlite:///personagem.db',
    'historia_rpg_bind': 'sqlite:///historia.db'
}
app.secret_key = '01001000 01100101 01111001 00101100 00100000 01110111 01101000 01100001 01110100 00100000 01100001 01110010 01100101 00100000 01111001 01101111 01110101 00100000 01100100 01101111 01101001 01101110 01100111 00100000 01101000 01100101 01110010 01100101 00111111 00100000 01101100 01101111 01101100'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)