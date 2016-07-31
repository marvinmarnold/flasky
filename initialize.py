from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from hello import hash_password

from database_setup import Base, Person, Photo, Tag, Comment

engine = create_engine('sqlite:///flasky.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSessionMaker = sessionmaker(bind=engine)
dbSession = DBSessionMaker()

### These are the commands you just saw live.

marvin = Person(
        name='Marvin',
        gender='male',
        nationality='American',
        hometown='New Orleans',
        email='marvin@meet.mit.edu',
        hashed_password=hash_password('marvin'))

lorenzo = Person(
        name='Lorenzo',
        gender='male',
        nationality='American',
        hometown='Dallas',
        email='lorenzo@meet.mit.edu',
        hashed_password=hash_password('lorenzo'))

anna = Person(
        name='Anna',
        gender='female',
        nationality='American',
        hometown='Pittsburg',
        email='anna@meet.mit.edu',
        hashed_password=hash_password('anna'))

lisa = Person(
        name='Lisa',
        gender='female',
        nationality='German',
        hometown='Fairbanks',
        email='lisa@meet.mit.edu',
        hashed_password=hash_password('lisa'))

eric = Person(
        name='Eric',
        gender='male',
        nationality='American',
        hometown='Durango',
        email='eric@meet.mit.edu',
        hashed_password=hash_password('eric'))

# This deletes everything in your database.
dbSession.query(Person).delete()
dbSession.query(Photo).delete()
dbSession.query(Tag).delete()
dbSession.query(Comment).delete()
dbSession.commit()


# This adds some rows to the database. Make sure you `commit` after `add`ing!
dbSession.add(marvin)
dbSession.add(lorenzo)
dbSession.add(anna)
dbSession.add(lisa)
dbSession.add(eric)
dbSession.commit()


#This addds some tags to the database
sports =Tag(name="sports")
travel = Tag(name="travel")

dbSession.add(sports)
dbSession.add(travel)
dbSession.commit()



#This adds some photos to the database. Make sure you `commit` after `add`ing!
erics_photo = Photo(
        user_id = eric.id,
        url="http://i.huffpost.com/gen/1730217/images/o-SURFING-WORKOUT-facebook.jpg"
)

#lisa adds a photo
lisas_photo = Photo(
        user_id = lisa.id,
        url="http://d21vu35cjx7sd4.cloudfront.net/dims3/MMAH/crop/0x0%2B0%2B0/resize/645x380/quality/90/?url=http%3A%2F%2Fs3.amazonaws.com%2Fassets.prod.vetstreet.com%2Ff1%2F0ad6d0a10611e087a80050568d634f%2Ffile%2Fmastiff-2-645mk062411.jpg"
)

dbSession.add(erics_photo)
dbSession.add(lisas_photo)
dbSession.commit()

#This adds some photos to the database. Make sure you `commit` after `add`ing!
marvins_comment = Comment(
        photo_id = erics_photo.id,
        comment_string ="Dude!! That looks sick!",
        commenter_id = marvin.id
)

annas_comment = Comment(
        photo_id = lisas_photo.id,
        comment_string ="Awww! I want one!",
        commenter_id = anna.id
)
dbSession.add(marvins_comment)
dbSession.add(annas_comment)
dbSession.commit()


erics_photo.tags.append(sports)
erics_photo.tags.append(travel)
dbSession.add(erics_photo)
dbSession.commit()


