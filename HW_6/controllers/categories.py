from models.category import Category
from models import db
from schemas.category import CategoryCreate

def get_all_categories() -> list[dict[str, int | str]]:
    categories = Category.query.all()
    categories_data = [
        {
            "id": category.id,
            "name": category.name
        }
        for category in categories
    ]

    return categories_data

def create_new_category(raw_data: dict[str, str]) -> Category:
    validated_obj = CategoryCreate.model_validate(raw_data)

    new_obj = Category(name=validated_obj.name)

    db.session.add(new_obj)
    db.session.commit()

    return new_obj

def get_category_by_id(id: int) -> Category:
    category = Category.query.get_or_404(id)
    return category


def update_category(obj, new_data):
    obj.name = new_data["name"]
    db.session.commit()

    return obj

def delete_category(obj):
    db.session.delete(obj)
    db.session.commit()

    return obj