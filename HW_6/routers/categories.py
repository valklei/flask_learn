from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from controllers.categories import get_all_categories, create_new_category, get_category_by_id, update_category, \
    delete_category
from schemas.category import CategoryBase, CategoryResponse

categories_bp = Blueprint('categories', __name__, url_prefix='/api/categories')


@categories_bp.route('/', methods=["GET", "POST"])
def manage_categories():
    if request.method == "GET":
        categories = get_all_categories()
        return jsonify([CategoryResponse.model_validate(cat).model_dump() for cat in categories])

    if request.method == "POST":
        data = request.json
        if "name" not in data:
            return jsonify({"error": "Отсутствует обязательное поле 'name'"}), 400

        try:
            new_category = create_new_category(raw_data=data)
        except ValidationError as err:
            return jsonify(err.errors()), 400

        return jsonify(CategoryResponse.model_validate(new_category).model_dump()), 201


@categories_bp.route('/<int:id>', methods=["GET", "PUT", "DELETE"])
def category_operations(id):
    category = get_category_by_id(id)
    if not category:
        return jsonify({"error": f"Категория с id {id} не найдена."}), 404

    if request.method == "GET":
        return jsonify(CategoryResponse.model_validate(category).model_dump())

    if request.method == "PUT":
        data = request.json
        if not data or "name" not in data:
            return jsonify({"error": "Отсутствует обязательное поле 'name'"}), 400

        updated_category = update_category(category, data)
        return jsonify(CategoryResponse.model_validate(updated_category).model_dump()), 200

    if request.method == "DELETE":
        delete_category(category)
        return jsonify({
            "message": f"Категория с id {id} и названием '{category.name}' успешно удалена."
        }), 204