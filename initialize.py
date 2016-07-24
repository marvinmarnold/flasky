from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from hello import hash_password

from database_setup import Base, Person

engine = create_engine('sqlite:///flasky.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSessionMaker = sessionmaker(bind=engine)
dbSession = DBSessionMaker()

### These are the commands you just saw live.

marvin = Person(
        name='Marvin Arnold',
        gender='male',
        nationality='American',
        hometown='New Orleans',
        email='marvin@meet.mit.edu',
        hashed_password=hash_password('marvin'))

lorenzo = Person(
        name='Lorenzo Brown',
        gender='male',
        nationality='American',
        hometown='Dallas',
        email='lorenzo@meet.mit.edu',
        hashed_password=hash_password('lorenzo'))

anna = Person(
        name='Anna Premo',
        gender='female',
        nationality='American',
        hometown='Pittsburg',
        email='anna@meet.mit.edu',
        hashed_password=hash_password('anna'))

lisa = Person(
        name='Lisa Kavanaugh',
        gender='female',
        nationality='German',
        hometown='Fairbanks',
        email='lisa@meet.mit.edu',
        hashed_password=hash_password('lisa'))

eric = Person(
        name='Eric Westberg',
        gender='male',
        nationality='American',
        hometown='Durango',
        email='eric@meet.mit.edu',
        hashed_password=hash_password('eric'))

# This deletes everything in your database.
dbSession.query(Person).delete()
dbSession.commit()

# This adds some rows to the database. Make sure you `commit` after `add`ing!
dbSession.add(marvin)
dbSession.add(lorenzo)
dbSession.add(anna)
dbSession.add(lisa)
dbSession.add(eric)
dbSession.commit()
