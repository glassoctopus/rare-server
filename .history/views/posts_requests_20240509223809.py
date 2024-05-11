import sqlite3
from models import Posts

POSTS = [
  {
    "id": 1, 
    "user_id": 1, 
    "category_id": 1, 
    "title": "Ipsum Lorem",
    "publication_date": "January 2024",
    "image_url": "", 
    "content": "Latin Stuff", 
    "approved": 1
    }
]

def get_all_posts():
  
    with sqlite3.connect("./db.sqlite3") as conn:
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
        print(dataset)
        
        for row in dataset:
            print(row)
            post = Posts(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
            print(post.__dict__)
            posts.append(post.__dict__)

    return posts

def get_single_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
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
   
def create_post(new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id, title, publication_date, image_url, content, approved )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?);
        """, ( new_post['user_id'],
              new_post['category_id'], new_post['title'],
              new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_post['id'] = id


    return new_post
