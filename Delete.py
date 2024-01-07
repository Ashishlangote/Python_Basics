from ORM import *

Base.metadata.create_all(engine)

local_session = session(bind=engine)

user_to_delete = local_session.query(User).filter(User.username == 'raju').first()
local_session.delete(user_to_delete)
local_session.commit()
