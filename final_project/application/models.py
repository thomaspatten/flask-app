from application import db 
from datetime import datetime 



class positions(db.model):
    id= db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(100),nullable=False)
    stat1_value=db.Column(db.Integer,nullable=False)
    stat2_value=db.Column(db.Integer,nullable=False)
    stat3_value=db.Column(db.Integer,nullable=False)
    
    player_id= db.Column(db.Integer,db.ForeignKey('players.id'),nullable=False)



def __repr__(self):
    return''.join([
        'Player id: ', self.player_id, '\r\n'
        'position:',self.position, '\r\n'
        'stat value:',self.stat1_value'\r\n',self.stat2_value'\r\n',self.stat3_value'\r\n'





class players(db.model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(s50),nullable=False)
    club=db.Column(db.String(50),nullable=False)
    stat1_name=db.Column(db.String(50),nullable=False)
    stat2_name=db.Column(db.String(50),nullable=False)
    stat3_name=db.column(db.String(50),nullable=False)

