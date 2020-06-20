from application import db 




class position(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    pos = db.Column(db.String(100),nullable=False)
    stat1_value=db.Column(db.Integer,nullable=False)
    stat2_value=db.Column(db.Integer,nullable=False)
    stat3_value=db.Column(db.Integer,nullable=False)
    
    player_id= db.Column(db.Integer,db.ForeignKey('player.id'),nullable=False)



def __repr__(self):
    return''.join([
        'Player id: ', self.player_id, '\r\n'
        'position:',self.pos, '\r\n'
        'stat value:',self.stat1_value,'\r\n',self.stat2_value,'\r\n',self.stat3_value,'\r\n'

        ])



class player(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    club=db.Column(db.String(50),nullable=False)
    stat1_name=db.Column(db.String(50),nullable=False)
    stat2_name=db.Column(db.String(50),nullable=False)
    stat3_name=db.Column(db.String(50),nullable=False)
    position=db.relationship('position', backref=db.backref('player'), lazy=True)
def __repr__(self):
    return'',join([
        'Name: ',self.first_name,'\r\n',self.last_name,'\r\n'
        'Club: ' ,self.club,'\r\n'
        'Stat Name:',self.stat1_name,'\r\n',self.stat2_name,'\r\n',self.stat3_name,'\r\n'
        ])
