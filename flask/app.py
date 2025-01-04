from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import Category, Task, User, db
from resources import CategoryResource, TaskResource, UserResource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)

api.add_resource(UserResource, "/users", "/users/<int:user_id>")
api.add_resource(TaskResource, "/tasks", "/tasks/<int:task_id>")
api.add_resource(CategoryResource, "/categories", "/categories/<int:category_id>")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
