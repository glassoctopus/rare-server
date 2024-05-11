import sqlite3
import json
from models import Tags

def create_tag(new_tag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            INSERT INTO Tags
                ( id, label)
            VALUES
                ( ?, ?, ?, ? )
            """, (new_tag['id'], new_tag['label'],))
        
        id = db_cursor.lastrowid
        
        new_tag['id'] = id
    
    return new_tag

def delete_tag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            DELETE FROM Tags
            WHERE id = ?
            """, (id, ))

def get_all_tags():
    with sqlite3.connect("./db.sqlite3") as conn:
        
        Tags = []
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            SELECT
                t.id,
                t.label
            FROM Tags t
                """)
        
        data = db_cursor.fetchall()
        
        for row in data:

            tag = Tags(row['id'], row['follower_id'], row['author_id'], row['created_id'])
            tags.append(tag.__dict__)
        
        return tags

def get_single_subscription(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            SELECT
                s.id,
                s.follower_id,
                s.author_id,
                s.created_id
            FROM Subscription s
            WHERE s.id = ?
            """, ( id, ))
        
        data = db_cursor.fetchone()
        
        subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_id'])
        
        return subscription.__dict__

    