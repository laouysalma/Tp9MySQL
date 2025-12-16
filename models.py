from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("mysql+pymysql://root:root:1234@localhost/universite")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Etudiant(Base):
    __tablename__ = "ETUDIANT"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    inscriptions = relationship("Inscription", back_populates="etudiant")

# à compléter avec Professeur, Cours, Enseignement, Inscription, Examen

# Créer les tables
Base.metadata.create_all(engine)
