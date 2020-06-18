from application import app, db 
from flask import render_template, redirect, url_for
from application.forms import positionForm, playerForm
from application.models import position, player 


@app.route('/')
@app.route('/home')
def home():
    playerData = player.query.all()
    positionData = position.query.all()
    return render_template(home.html, title='home', player=playerData, position=positionData)


@app.route('/about')
def about():
    return render_template(about.html, title='about')



@app.route(/'post', methods['GET','POST'])
def post():
    form = playerForm
    if form.validate_on_submit():
        playerData= player(
                first_name=form.first_name.data
                last_name=form.last_name.data
                club=form.club.data
                stat1_name=form.stat1_name.data
                stat2_name=form.stat2_name.data
                stat3_name=form.stat3_name.data


        )
        db.sessionadd(playerData)
        db.session.commit()
        return redirect(url_for('post')


    else:
        print(form.errors)

    return render_template('post.html', title='post', form=form)


    form = positionForm
    if form.validate_on_submit():
        positionData= position(
                    position=form.position.data
                    stat1_value=form.stat1_value.data
                    stat2_value=form.stat2_value.data
                    stat3_value=form.stat2_value.data

        )
        db.session.add(positionData)
        db.session.commit()
        return redirect(url_for('post')


    else:
        prnt(form.errors)
    return render_template('post.html', title='post', form=form)
                    
