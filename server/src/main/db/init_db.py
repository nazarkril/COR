from server.src.main.var import HOST_NAME, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD, DATABASE_NAME
from flask import Flask, request
import psycopg2

# Create a Flask app
app = Flask(__name__)

# Connect to the database using psycopg2 library and the database credentials
conn = psycopg2.connect(
    host=HOST_NAME,
    port=POSTGRES_PORT,
    database=DATABASE_NAME,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)


def create():
    # Get the username and email from the request body
    username = request.form.get('username')
    email = request.form.get('email')

    # Insert the data into the database
    cur = conn.cursor()
    id = len(get_users_for_db())
    cur.execute(f"INSERT INTO users VALUES ({id}, '{username}', '{email}')")
    conn.commit()

    return 'User created successfully!'


def get_users_for_db():
    cur = conn.cursor()
    cur.execute(f"SELECT username FROM users;")
    result = cur.fetchall()
    conn.commit()
    return result


if __name__ == '__main__':
    app.run()
