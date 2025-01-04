from flask_restful import Resource, reqparse
from models import Category, Task, User, db

user_parser = reqparse.RequestParser()
user_parser.add_argument(
    "username", type=str, required=True, help="Username cannot be blank"
)

task_parser = reqparse.RequestParser()
task_parser.add_argument("title", type=str, required=True, help="Title cannot be blank")
task_parser.add_argument("description", type=str)
task_parser.add_argument(
    "user_id", type=int, required=True, help="User ID cannot be blank"
)
task_parser.add_argument(
    "category_id", type=int, required=True, help="Category ID cannot be blank"
)

category_parser = reqparse.RequestParser()
category_parser.add_argument(
    "name", type=str, required=True, help="Category name cannot be blank"
)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return {"id": user.id, "username": user.username}, 200
        return {"message": "User not found"}, 404

    def post(self):
        args = user_parser.parse_args()
        new_user = User(username=args["username"])
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "username": new_user.username}, 201


class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get(task_id)
        if task:
            return {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "user_id": task.user_id,
                "category_id": task.category_id,
            }, 200
        return {"message": "Task not found"}, 404

    def post(self):
        args = task_parser.parse_args()
        new_task = Task(
            title=args["title"],
            description=args["description"],
            user_id=args["user_id"],
            category_id=args["category_id"],
        )
        db.session.add(new_task)
        db.session.commit()
        return {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "user_id": new_task.user_id,
            "category_id": new_task.category_id,
        }, 201


class CategoryResource(Resource):
    def get(self, category_id):
        category = Category.query.get(category_id)
        if category:
            return {"id": category.id, "name": category.name}, 200
        return {"message": "Category not found"}, 404

    def post(self):
        args = category_parser.parse_args()
        new_category = Category(name=args["name"])
        db.session.add(new_category)
        db.session.commit()
        return {"id": new_category.id, "name": new_category.name}, 201
