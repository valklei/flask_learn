from extensions import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    answers = db.relationship('Answer', back_populates='question')
    category = db.relationship('Category', back_populates='questions')

    def __repr__(self):
        return f'<Question {self.text}>'