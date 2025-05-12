from sqlalchemy.orm import Mapped, mapped_column
from extensions import db
from models.question import Question

class Answer(db.Model):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    question_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('questions.id'),
    )
    is_agree: Mapped[bool] = mapped_column(
        db.Boolean,
    )

    question: Mapped['Question'] = db.relationship('Question', back_populates='answers')

    def __repr__(self):
        return f'Answer(id={self.id}, question_id={self.question_id}, is_agree={self.is_agree})'