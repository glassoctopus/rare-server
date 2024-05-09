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
            
            
            for row in dataset:
                print(row)
                post = Posts(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
                print(post.__dict__)
                posts.append(post.__dict__)

    return posts
   
