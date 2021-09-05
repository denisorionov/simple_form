from flask import Blueprint, request
from flask import render_template

from app import db
from questionnaire.models import UserProfiles, User

users = Blueprint('questionnaire', __name__, template_folder='templates')


@users.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            user = User(name=request.form['userName'],
                        middle_name=request.form['userSurname'],
                        bornDate=request.form['dateBorn'],
                        gender=request.form['gender'])
            db.session.add(user)
            db.session.flush()

            citizen = request.form.get('citizen')
            if not citizen:
                citizen = "unchecked"

            user_profiles = UserProfiles(user_id=user.user_id,
                                         education=request.form['education'],
                                         comment=request.form['comment'],
                                         citizenship=citizen)
            db.session.add(user_profiles)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)

    return render_template("questionnaire/picture.html")

