from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from controllers.catigories import get_all_categories, create_new_category, get_category_by_id, update_category, \
    delete_category
from schemas.category import CategoryBase

categories_bp = Blueprint(name='categories', import_name=__name__)

@categories_bp.route('', methods=["GET", "POST"])
def get_categories():
    if request.method == "GET":
        categories = get_all_categories()

        return jsonify(categories)

    if request.method == "POST":
        data = request.json

        try:
            new_category = create_new_category(raw_data=data)
        except ValidationError as err:
            return jsonify(err.errors()), 400

        return jsonify(
            CategoryBase(id=new_category.id,
                         name=new_category.name
                         ).model_dump()
        ), 201


@categories_bp.route('<int:id>', methods=["PUT", "DELETE"])
def retrieve_category(id):
    if request.method == "PUT":
        category = get_category_by_id(id=id)

        if not category:
            return jsonify(
                {
                    "error": f"Значение по id - {id} не найдено."
                }
            ), 404

        data = request.json
        if not data or "name" not in data:
            return jsonify(
                {
                    "error": "No required field provided. ('name')"
                }
            ), 400

        updated_category = update_category(category, data)

        return jsonify(
            {
                "id": updated_category.id,
                "name": updated_category.name
            }
        ), 200

    if request.method == "DELETE":
        category = get_category_by_id(id=id)

        if not category:
            return jsonify(
                {
                    "error": f"Значение по id - {id} не найдено."
                }
            ), 404

        deleted_category = delete_category(category)

        return jsonify(
            {
                "id": deleted_category.id,
                "name": deleted_category.name
            }
        ), 200