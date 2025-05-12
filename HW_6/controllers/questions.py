from controllers.categories import get_category_by_id
from models.question import Question
from models import db
from schemas.question import QuestionCreate

def get_all_questions():
    return Question.query.options(db.joinedload(Question.category)).all()

def create_new_question(raw_data: dict[str, str]) -> Question:
    validated_obj = QuestionCreate.model_validate(raw_data)
    get_category_by_id(validated_obj.category_id)
    new_obj = Question(text=validated_obj.text, category_id=validated_obj.category_id)
    db.session.add(new_obj)
    db.session.commit()
    db.session.refresh(new_obj)
    return new_obj

def get_questions_by_id(question_id: int) -> Question:
    return Question.query.options(db.joinedload(Question.category)).get(question_id)


def update_question(obj, new_data):
    obj.text = new_data["text"]
    db.session.commit()

    return obj