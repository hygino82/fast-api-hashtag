from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    Float,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base

from sqlalchemy_utils import ChoiceType

# Cria a conexão com o banco de dados SQLite
db = create_engine("sqlite:///banco.db", echo=True)

# Cria a classe base para os modelos do SQLAlchemy
Base = declarative_base()

# Criar as classes/tabelas do banco de dados


# Usuário
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True, nullable=False)
    admin = Column("admin", Boolean, default=False, nullable=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


# Pedido
class Pedido(Base):
    __tablename__ = "pedidos"

    STATUS_PEDIDOS = [
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO"),
        ("FINALIZADO", "FINALIZADO"),
    ]

    id = Column("id", Integer, nullable=False, primary_key=True, autoincrement=True)
    status = Column(
        "status", String, default="PENDENTE", nullable=False
    )

    usuario = Column("usuario", ForeignKey("usuarios.id"), nullable=False)
    preco = Column("preco", Float, nullable=False)

    # itens = Column("itens", String, nullable=False)  # Armazena os itens do pedido como uma string
    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco


# Itens Pedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    id = Column("id", Integer, nullable=False, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String, nullable=False)
    tamanho = Column("tamanho", String, nullable=False)
    preco_unitario = Column("preco_unitario", Float, nullable=False)
    pedido = Column("pedido", Integer, ForeignKey("pedidos.id"), nullable=False)

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido


# Executa a criação dos metadados no banco de dados
Base.metadata.create_all(db)
