from flask import Flask
from app.connectors.connector import connection
from app.models.user_home import User
from sqlalchemy import select, text
from sqlalchemy.orm import sessionmaker
from app.controllers.user_home import user_routes
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.register_blueprint(user_routes)


@app.route('/')
def hello_universe():
    # SQL Way
    # Session = sessionmaker(connection)
    # with Session() as session:
    #     session.execute(text("INSERT INTO user (name, email, occupation) VALUES ('meirthmh', 'mei@gmail.com', 'Miss Billionare')"))
    #     session.commit()

    user_query = select(User)
    Session = sessionmaker(connection)
    with Session() as s:
        result = s.execute(user_query)
        for row in result.scalars():
            print(f'ID: {row.id}, Name: {row.name}')

    return "hello universe"

