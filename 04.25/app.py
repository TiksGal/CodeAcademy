from main import engine, Project
from sqlalchemy.orm import sessionmaker
from session import session



while True:
    pasirinkimas = int(input("Pasirinkite veiksmą: \n1 - atvaizduoti projektus \n2 - sukurti projektą \n3 - pakeisti projektą \n4 - ištrinti projektą\n"))

    if pasirinkimas == 1:
        projektai = session.query(Project).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")

    if pasirinkimas == 2:
        name = input("Įveskite projekto pavadinimą")
        price = float(input("Įveskite projekto kainą"))
        projektas = Project(name, price)
        session.add(projektas)
        session.commit()

    if pasirinkimas == 3:
        projektai = session.query(Project).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")
        keiciamo_id = int(input("Pasirinkite norimo pakeisti projekto ID"))
        keiciamas_projektas = session.query(Project).get(keiciamo_id)
        pakeitimas = int(input("Ką norite pakeisti: 1 - pavadinimą, 2 - kainą"))
        if pakeitimas == 1:
            keiciamas_projektas.name = input("Įveskite projekto pavadinimą")
        if pakeitimas == 2:
            keiciamas_projektas.price = float(input("Įveskite projekto kainą"))
        session.commit()

    if pasirinkimas == 4:
        projektai = session.query(Project).all()
        print("-------------------")
        for projektas in projektai:
            print(projektas)
        print("-------------------")
        keiciamo_id = int(input("Pasirinkite norimo ištrinti projekto ID"))
        trinamas_projektas = session.query(Project).get(keiciamo_id)
        session.delete(trinamas_projektas)
        session.commit()