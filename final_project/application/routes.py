from application import app, db 
from flask import render_template, redirect, url_for
from application.forms import positionForm, playerForm, UpdatepositionForm
from application.models import position, player 


@app.route('/')
@app.route('/home')
def home():
    playerData = player.query.all()

    return render_template('home.html', title='home', player=playerData)


@app.route('/about')
def about():
    return render_template('about.html', title='about')



@app.route('/post', methods=['GET','POST'])
def post():
    playerData= player.query.all()
    form = playerForm()
    if form.validate_on_submit():
        playerData= player(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                club=form.club.data,
                stat1_name=form.stat1_name.data,
                stat2_name=form.stat2_name.data,
                stat3_name=form.stat3_name.data


        )
        db.session.add(playerData)
        db.session.commit()
        return redirect(url_for('post'))

    else:
        print(form.errors)

    return render_template('post.html', title='post', form=form)

@app.route('/update_position/<int:id>', methods=['GET','POST'])
def update_position(id):
    form = UpdatepositionForm()
    position=position.query.filter_by(id = id).first()
    if form.validate_on_submit:
        pos=form.pos.data,
        stat1_value=form.stat1_value.data,
        stat2_value=form.stat2_value.data,
        stat3_value=form.stat3_value.data

        db.session.commit()
        return redirect(url_for('update_position'))
    else:
        print (form.errors)
    return render_template('updateposition.html', title='update', form = form, id=id)
@app.route('/position',methods=['GET','POST'])
def position():
    
    
    form = positionForm()
    if form.validate_on_submit():
        positionData= position(
                    pos=form.pos.data,
                    stat1_value=form.stat1_value.data,
                    stat2_value=form.stat2_value.data,
                    stat3_value=form.stat3_value.data

        )
        db.session.add(positionData)
        db.session.commit()
        return redirect(url_for('position'))


    else:
        print(form.errors)
    return render_template('position.html', title='position', form=form)
