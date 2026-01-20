from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    education_form = Column(String, nullable=False)
