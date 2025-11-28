from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.String(32), nullable=False)
    cpf = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    telefone = db.Column(db.String(32), nullable=False)
    matricula = db.Column(db.String(32), nullable=False)
    usuario = db.Column(db.String(64), nullable=False)
    nome = db.Column(db.String(128), nullable=False)
    cargo = db.Column(db.String(64), nullable=True)
    unidade = db.Column(db.String(64), nullable=True)
    motivo = db.Column(db.Text, nullable=True)
    concordo = db.Column(db.Boolean, default=False)
    ativo = db.Column(db.Boolean, default=False)
    senha = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.id} {self.usuario}>'


# Modelo para Lote

class Lote(db.Model):
    __tablename__ = 'lotes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    empresa = db.Column(db.String(128), nullable=True)
    numero_contrato = db.Column(db.String(32), nullable=True)
    numero = db.Column(db.String(32), nullable=True)
    data_inicio = db.Column(db.String(32), nullable=True)
    data_fim = db.Column(db.String(32), nullable=True)
    valor_contratual = db.Column(db.Float, nullable=True)
    unidades = db.Column(db.Text, nullable=True)  # Salvar como JSON/texto
    precos = db.Column(db.Text, nullable=True)    # Salvar como JSON/texto
    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.String(32), nullable=True)
    data_criacao = db.Column(db.String(32), nullable=True)
    data_contrato = db.Column(db.String(32), nullable=True)
    status = db.Column(db.String(32), nullable=True)
    descricao = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Lote {self.id} {self.nome}>'
