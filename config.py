from db import db

# Tabela de Usuários do Site (Mestres e Jogadores)
class UsuarioRpg(db.Model):
    __tablename__ = 'usuarios_rpg'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(300), nullable=False)
    is_mestre = db.Column(db.Boolean, default=False)  # Para saber se é Mestre ou Jogador

# Tabela de Fichas dos Personagens
class Personagem(db.Model):
    __tablename__ = 'personagens'
    __bind_key__ = 'personagem_rpg_bind'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    classe = db.Column(db.String(50), nullable=False)
    nivel = db.Column(db.Integer, default=1)
    dono_user = db.Column(db.String(100), nullable=False) # Vinculado ao login do usuário

# Tabela da História / Resumo da One-Shot
class HistoriaOneShot(db.Model):
    __tablename__ = 'historia_oneshot'
    __bind_key__ = 'historia_rpg_bind'
    
    id = db.Column(db.Integer, primary_key=True)
    resumo = db.Column(db.Text, nullable=False)
    sessao_titulo = db.Column(db.String(150), nullable=False)