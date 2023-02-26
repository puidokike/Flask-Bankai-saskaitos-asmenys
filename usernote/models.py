from usernote import db


class Saskaita(db.Model):
    __tablename__ = "saskaita"
    id = db.Column(db.Integer, primary_key=True)
    numeris = db.Column(db.String(100))
    balansas = db.Column(db.Integer)
    asmuo_id = db.Column(db.Integer, db.ForeignKey('asmuo.id'))
    bankas_id = db.Column(db.Integer, db.ForeignKey('bankas.id'))
    asmuo = db.relationship("Asmuo")
    bankas = db.relationship("Bankas")

    def __init__(self, numeris, balansas, asmuo_id, bankas_id):
        self.numeris = numeris
        self.balansas = balansas
        self.asmuo_id = asmuo_id
        self.bankas_id = bankas_id

    def __repr__(self):
        return f"{self.id}. Numeris: {self.numeris}. Balansas: {self.balansas}$. Asmens ID: {self.asmuo_id}"


class Asmuo(db.Model):
    __tablename__ = "asmuo"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(100))
    pavarde = db.Column(db.String(100))
    ak = db.Column(db.Integer)
    tel = db.Column(db.String(12))

    def __init__(self, vardas, pavarde, ak, tel):
        self.vardas = vardas
        self.pavarde = pavarde
        self.ak = ak
        self.tel = tel

    def __repr__(self):
        return f"{self.id}. {self.vardas} {self.pavarde}, a.k.: {self.ak}. Tel.nr.: {self.tel}"


class Bankas(db.Model):
    __tablename__ = "bankas"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String(100))
    adresas = db.Column(db.String(100))
    banko_kodas = db.Column(db.String(50))
    swift = db.Column(db.String(10))

    def __init__(self, pavadinimas, adresas, banko_kodas, swift):
        self.pavadinimas = pavadinimas
        self.adresas = adresas
        self.banko_kodas = banko_kodas
        self.swift = swift

    def __repr__(self):
        return f"{self.id}. {self.pavadinimas}, {self.adresas}. Banko kodas: {self.banko_kodas}, SWIFT: {self.swift}"


