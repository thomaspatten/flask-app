from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, Length
from application.models import  players, positions

class playersForm(FlaskForm):
    first_name = StringField('First Name',
         validators = [
            DataRequired(),
            Length(min=1, max=30)

            ]

    )

    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=1, max=30
            
            ]


    )


    club = StringField('Club',
        validators = [
            DataRequired(),
            Length(min=1, max=30)


                ]

    )


    stat1_name = StringField('Stat 1 Name',
        validators = [
            DataRequried(),
            Length(min=1, max =30)

                ]

    )


    stat2_name= StringField('Stat 2 Name',
        validators = [
            DataRequired(),
            length(min=1, max=30)

                ]

    )


    stat3_name =StringField('Stat 3 Name',
        validators = [
            DataRequied(),
            Length(min=1, max=30)

                ]

    )



    submit = SubmitField('Add Your Player, Club And Stat Names')



class positionForm(Flaskform):
    position = StringField('Position',
        validators = [
            DataRequried(),
            Length(min=1, max=10)

                ]

    )



    
    stat1_value = StringField('Stat 1 Value',
        validators = [
            DataRequired(),
            Length(min=1,max=10)

                ]

    )


    stat2_value = StringField('Stat 2 Value',
        validators = [
            DataRequried(),
            Length(min=1, max=10)

                ]

    )


    stat3_value = StringField('Stat 3 value',
        validators = [
            DataRequired(),
            Length(min=1, max=30)



    submit= SubmitField('Add The Position And the Stat Values To The Player')
