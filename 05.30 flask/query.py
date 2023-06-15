from app import Message, db, app

with app.app_context():
    db.create_all()  # creates the tables in the DB

    # create some test records:
    jonas = Message('Jonas', 'jonas@mail.com', 'Some very serious feedback.')
    antanas = Message('Antanas', 'antanas@mail.lt', 'Antanas opinion is very important.')
    juozas = Message('Juozas', 'juozukas@friends.lt', 'I am very angry because it is bad.')
    bronius = Message('Bronius', 'bronka@yahoo.com', 'I am happy, I like it.')

    # Add these characters to our DB
    db.session.add_all([jonas, antanas, juozas, bronius])

    # .commit saves the changes
    db.session.commit()

    print(jonas.id)
    print(antanas.id)
    print(bronius.id)
    print(juozas.id)


# 1
# 2
# 4
# 3