from ORM import *

Base.metadata.create_all(engine)

users = [
    {
        'username': 'ashish',
        'email': 'ashish@gmail.com'
    },
    {
        'username': 'raju',
        'email': 'raju@gmail.com'
    }
]

local_session = session(bind=engine)

for user in users:
    new_user = User(username=user['username'], email=user['email'])

    local_session.add(new_user)
    local_session.commit()

    print(f"Added {user['username']}")
