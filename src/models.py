from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    apellido = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    favoritos_personajes = db.relationship('PersonajesFavoritos', backref='Usuarios', lazy=True)
    favoritos_personajes = db.relationship('PlanetasFavoritos', backref='Usuarios', lazy=True)

    def __repr__(self):
        return "<Usuario %r >" % self.nombre
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }

class Personajes(db.Model):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    raza = db.Column(db.String(250))
    altura = db.Column(db.String(250))
    peso = db.Column(db.String(250), nullable=False)
    favoritos_personajes = db.relationship('PersonajesFavoritos', backref='Personaje', lazy=True)

    def __repr__(self):
        return "<Personajes %r >" % self.nombre
    
    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "raza": self.raza,
            "altura": self.altura,
            "peso": self.peso
        }

class PersonajesFavoritos(db.Model):
    __tablename__ = 'personajes_favoritos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    personaje_id = db.Column(db.Integer,db.ForeignKey("personajes.id"))

    def __repr__(self):
        return "<PersonajesFavoritos %r >" % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id
        }
    

class Planetas(db.Model):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    poblacion = db.Column(db.String(250))
    diametro = db.Column(db.String(250))
    temperatura = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planetas %r>' % self.nombre

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "diametro": self.diametro,
            "temperartura": self.temperatura
            # do not serialize the password, its a security breach
        }

class PlanetasFavoritos(db.Model):
    __tablename__ = 'planetas_favoritos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    planeta_id = db.Column(db.Integer,db.ForeignKey("planeta.id"))

    def __repr__(self):
        return "<PlanetasFavoritos %r >" % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.planeta_id
        }