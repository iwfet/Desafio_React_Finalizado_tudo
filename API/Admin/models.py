from API import db

class INSS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faixa_inicial = db.Column(db.Numeric(10,2), nullable=False)
    faixa_final = db.Column(db.Numeric(10,2), nullable=False)
    aliquota = db.Column(db.Integer, default=0)
    deduçao = db.Column(db.Numeric(10,2), nullable=False)
    
    def __repr__(self):
        return '%r' % self.id

class IRFF(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faixa_inicial = db.Column(db.Numeric(10,2), nullable=False)
    faixa_final = db.Column(db.Numeric(10,2), nullable=False)
    aliquota = db.Column(db.Integer, default=0)
    deduçao = db.Column(db.Numeric(10,2), nullable=False)
    
    def __repr__(self):
        return '%r' % self.id
    
db.create_all()