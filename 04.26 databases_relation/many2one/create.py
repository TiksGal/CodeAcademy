from many2one.models import Vaikas, Tevas
from many2one.session import session

vaikas = Vaikas(
    vardas="vaikas", pavarde="Tevaika", mokymo_istaiga="Ciurlionio gimnazija" 
)
tevas = Tevas(
    vardas="Tevas", pavarde="Tevaika", vaikas=vaikas
)
session.add(tevas)
session.commit()