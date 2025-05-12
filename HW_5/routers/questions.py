from flask import Blueprint, request, jsonify, Response
from pydantic import ValidationError

from controllers.questions import get_all_questions, create_new_question, get_questions_by_id, update_question
from schemas.question import QuestionResponse

questions_bp = Blueprint(name="questions", import_name=__name__)

@questions_bp.route('', methods=["GET", "POST"])
def questions_list() -> None | tuple[Response, int] | Response:
    if request.method == "GET":
        questions = get_all_questions()

        return jsonify(questions)

    if request.method == "POST":
        data = request.json

        try:
            new_question = create_new_question(raw_data=data)
        except ValidationError as err:
            return jsonify(err.errors()), 400

        return jsonify(
            QuestionResponse(id=new_question.id,
                             text=new_question.text,
                             category_id=new_question.category_id
                             ).model_dump()
        ), 201


@questions_bp.route('/<int:id>', methods=["GET", "PUT", "DELETE"])
def retrieve_question(id: int):
    if request.method == "GET":
        question = get_questions_by_id(id=id)
        if not question:
            return jsonify(
                {
                    "error": f"Значение по id - {id} не найдено."
                }
            ), 404
        return jsonify(
            QuestionResponse(id=question.id,
                             text=question.text,
                             category_id=question.category_id
                             ).model_dump()
        ), 200

    if request.method == "PUT":
        question = get_questions_by_id(id=id)
        if not question:
            return jsonify(
                {
                    "error": f"Значение по id - {id} не найдено."
                }
            ), 404

        data = request.json
        if not data or "text" not in data:
            return jsonify(
                {
                    "error": "No required field provided. ('text')"
                }
            ), 400

        updated_question = update_question(question, data)

        return jsonify(
            QuestionResponse(id=updated_question.id,
                             text=updated_question.text,
                             category_id=updated_question.category_id
                             ).model_dump()
        ), 200

    if request.method == "DELETE":
        return f"QUESTION DELETE BY ID - {id}"