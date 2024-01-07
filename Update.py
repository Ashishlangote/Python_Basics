from ORM import *

Base.metadata.create_all(engine)

local_session = session(bind=engine)

user_to_update = local_session.query(User).filter(User.username == 'ashish').first()

user_to_update.username = "pappu"
user_to_update.email = "pappu@gmail.com"
local_session.commit()
