from ORM import *

Base.metadata.create_all(engine)

Base.metadata.create_all(engine)

local_session = session(bind=engine)

# users = local_session.query(User).all()[:3]
#
# for user in users:
#     print(user.email)

result = local_session.query(User).filter(User.username == 'ashish').first()
print(result)
