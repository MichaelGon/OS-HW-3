from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'mydb'),
        user=os.getenv('DB_USER', 'user'),
        password=os.getenv('DB_PASSWORD', 'password')
    )
    return conn

@app.route('/users', methods=['GET', 'POST'])
def users():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.json['name']
        cursor.execute('INSERT INTO users (name) VALUES (%s)', (name,))
        conn.commit()
        return jsonify({'status': 'User added'}), 201

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(users)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100));')
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001)
