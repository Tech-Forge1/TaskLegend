#--------------------Importações começam aqui----------------------------------
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from sqlalchemy.orm import mapped_column, Mapped
from email_validator import validate_email, EmailNotValidError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_manager, LoginManager, UserMixin
#-------------------Importações terminam aqui-----------------------------------


#-------------------Configurações começam aqui----------------------------------
app = Flask()
app.config['WTF_CSRF_ENABLED'] = True
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
#-----------------Configirações terminam aqui---------------------------------


#-----------------Banco de dados começa aqui----------------------------------
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    senha: Mapped[str] = mapped_column(nullable=False)

    @property
    def password(self):
        raise AttributeError("Palavra-passe não é acessível diretamente.")

    @password.setter
    def password(self, text_pass):
        self.password_hash = generate_password_hash(text_pass)

    def check_pass(self, tryed_pass):
        return check_password_hash(self.password_hash, tryed_pass)

    def __repr__(self):
        return f'User(name={self.name}, email={self.email})'

#-----------------Banco de dados termina aqui----------------------------------


#-----------------Endpoints começam aqui---------------------------------------
@app.route('/register', methods=['POST'])
def criar_conta():
    data = request.json
    nome = data.get('name')
    mail = data.get('mail')
    senha1 = data.get('senha1')
    senha2 = data.get('senha2')

    if not nome or not mail:
        return jsonify({"error": "Campos obrigatorios"})

    if senha1 != senha2:
        return jsonify({"error": "Palavra-passe diferentes"})

    try:
        valid_email = validate_email(mail).email
    except EmailNotValidError as e:
        return jsonify({"error": "Email invalido: " + str(e)}), 400

    user = Users(nome=nome, email=mail, senha=senha1)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso", "user": {
        "id": user.id, "name": user.nome, "email": user.email, "senha": user.senha}}), 201

@app.rout('/login', methods=['POST'])
def login_page():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    user = Users.query.filter_by(email=email).first()
    if user and user.check_pass(senha):
        login_user(user, remember=True, duration=timedelta(days=7))

    return jsonify({"message": "Login realizado com sucesso!"}), 200

@app.route('/logout', methods=['GET'])
def logout(id):
    user = Users.query.get_or_404(id)
    logout(user)

    return jsonify({"message": "Logout feito com sucesso"})
#-------------------Endpoints terminam aqui------------------------


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True, host='0.0.0.0', port=2323)
