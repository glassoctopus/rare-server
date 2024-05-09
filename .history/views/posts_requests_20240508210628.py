import sqlite3
import json
from models import Posts

def get_all_posts():
    try:
        with sqlite3.connect("./rare.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                p.id,
                p.user_id,
                p.category_id,
                p.title,
                p.publication_date,
                p.image_url,
                p.content,
                p.approved
            FROM Posts p
            """)

            posts = []

            dataset = db_cursor.fetchall()
            print("Number of rows fetched:", len(dataset)) 
            
            for row in dataset:
                post = Posts(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'],
                             row['image_url'], row['content'], row['approved'])
                posts.append(post.__dict__)

        return posts
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return []  




def get_single_post(id):
    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.id = ?
        """, ( id, ))

        
        data = db_cursor.fetchone()

        
        post = Posts(data['id'], data['user_id'], data['category_id'], data['title'], data['publication_date'],
                          data['image_url'], data['content'], data['approved'])

        return post.__dict__
