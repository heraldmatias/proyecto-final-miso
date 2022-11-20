from sqlalchemy import Column, Integer, String

from .database import Base


class CasoMedico(Base):
    __tablename__ = "caso_medico"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    tipo_lesion = Column(String, index=True)
    forma_lesion = Column(String, index=True)
    especialidad = Column(String, index=True)
    paciente_id = Column(Integer, index=True)

# TODO Agregar tabla de imagenes
