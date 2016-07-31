from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person, Comment, Tag, Photo

engine = create_engine('sqlite:///flasky.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSessionMaker = sessionmaker(bind=engine)
dbSession = DBSessionMaker()

#Eric adds a new photo
eric = dbSession.query(Person).filter_by(name="Eric Westberg").first()
new_photo = Photo(user_id = eric.id,
        url="http://i.huffpost.com/gen/1730217/images/o-SURFING-WORKOUT-facebook.jpg")
new_photo.tags.append(Tag(name="food"))

eric.photos.append(new_photo)


#Tag Eric's photo with a new tag
photoID = 1
photo = dbSession.query(Photo).filter_by(id=photoID).first()
new_tag = Tag(name="indonesia")
photo.tags.append(new_tag)
dbSession.add(new_tag)
dbSession.commit()


#Eric adds a new comment
newComment = Comment(photo_id=photoID, comment_string="I know!! Makes me miss the ocean!", commenter_id = eric.id)
photo.comments.append(newComment)
dbSession.add(newComment)
dbSession.commit()


#print post
print("***** POST ****")
print("Photo: "  + photo.url)
user = dbSession.query(Person).filter_by(id=photo.user_id).first()
print("User: "  + str(user.id))
print("Name: "  + user.name)
print("Comments:")

for comment in photo.comments:
    print(comment.comment_string)
