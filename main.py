from app import app
from app import db
from questionnaire.view import users

app.register_blueprint(users, url_prefix='/')
if __name__ == '__main__':
    app.run()
