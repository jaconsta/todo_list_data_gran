from app import db

from app.users.models import User


class Todo(db.Document):
    """
    A ToDo entry.
    """
    # Entry owner
    user = db.ReferenceField(User)

    description = db.StringField(required=True)

    status_choices = ('PENDING', 'COMPLETE')
    status = db.StringField(choices=status_choices, default=status_choices[0])

    created_at = db.DateTimeField()
    updated_at = db.DateTimeField()

    def set_user(self, user_id):
        self.user = user_id
