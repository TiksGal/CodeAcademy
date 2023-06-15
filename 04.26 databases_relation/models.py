from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///saskaitos.db')
Base = declarative_base()


class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    asmens_kodas = Column("Asmens kodas", Integer, unique=True)
    el_pastas = Column("El. pašto adresas", String)

    def __repr__(self):
        return f"{self.id}: {self.vardas} {self.pavarde}, {self.asmens_kodas}, {self.el_pastas}"

class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    adresas = Column("Adresas", String)
    banko_kodas = Column("Banko kodas", Integer)
    swift_kodas = Column("SWIFT kodas", String)

    def __repr__(self):
        return f"{self.id}: {self.pavadinimas}, {self.adresas}, {self.banko_kodas}, {self.swift_kodas}"

class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key=True)
    numeris = Column("Sąskaitos numeris", Integer)
    balansas = Column("Pinigų balansas", Float)
    asmuo_id = Column(Integer, ForeignKey('asmuo.id'))
    asmuo = relationship("Asmuo")
    bankas_id = Column(Integer, ForeignKey('bankas.id'))
    bankas = relationship("Bankas")

    def __repr__(self):
        return f"{self.id}: {self.numeris}, {self.balansas}, {self.asmuo}, {self.bankas}"


Base.metadata.create_all(engine)