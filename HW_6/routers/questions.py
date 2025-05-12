from flask import Blueprint, jsonify, request
from controllers.questions import get_all_questions, create_new_question, get_questions_by_id
from schemas.question import QuestionResponse

questions_bp = Blueprint("questions", __name__, url_prefix="/api/questions")

@questions_bp.route('/', methods=['GET'])
def list_questions():
    try:
        questions = get_all_questions()
        for q in questions:
            print(f"[DEBUG] Question: {q.text}, category: {q.category}")
        return jsonify([QuestionResponse.model_validate(q).model_dump() for q in questions])
    except Exception as e:
        print(f"Ошибка при получении вопросов: {str(e)}")
        return jsonify({"error": str(e)}), 500


@questions_bp.route('/', methods=['POST'])
def create_question():
    data = request.get_json()
    try:
        question = create_new_question(data)
        response_data = QuestionResponse.model_validate(question).model_dump()
        return jsonify(response_data), 201
    except Exception as e:
        print(f"Ошибка при создании вопроса: {str(e)}")
        return jsonify({"error": str(e)}), 400

@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = get_questions_by_id(question_id)
    if not question:
        return {"error": "Не найден"}, 404
    return jsonify(QuestionResponse.model_validate(question).model_dump())