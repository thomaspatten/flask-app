from application import db
from application.models import position, player
db.drop_all()
db.create_all()
