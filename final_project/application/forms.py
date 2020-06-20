from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, Length
from application.models import  player, position

class playerForm(FlaskForm):
    first_name = StringField('First Name',
         validators = [
            DataRequired(),
            Length(min=1, max=30)

            ]

    )

    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=1, max=30)
            
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
            DataRequired(),
            Length(min=1, max =30)

                ]

    )


    stat2_name= StringField('Stat 2 Name',
        validators = [
            DataRequired(),
            Length(min=1, max=30)

                ]

    )


    stat3_name =StringField('Stat 3 Name',
        validators = [
            DataRequired(),
            Length(min=1, max=30)

                ]

    )



    submit = SubmitField('Add Your Player, Club And Stat Names')



class positionForm(FlaskForm):
    pos = StringField('Position',
        validators = [
            DataRequired(),
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
            DataRequired(),
            Length(min=1, max=10)

                ]

    )


    stat3_value = StringField('Stat 3 value',
        validators = [
            DataRequired(),
            Length(min=1, max=30)

                ]
    )

    submit= SubmitField('Add The Position And the Stat Values To The Player')



class UpdatepositionForm(FlaskForm):
    pos = StringField('Position',
        validators = [
            DataRequired(),
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
            DataRequired(),
            Length(min=1, max=10)

                ]

    )


    stat3_value = StringField('Stat 3 value',
        validators = [
            DataRequired(),
            Length(min=1, max=30)

                ]
    )

    submit= SubmitField('Add The Position And the Stat Values To The Player')
