import sqlite3
import json
from models import Category

def create_category(new_category):
    with sqlite3.connect("./rare.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            INSERT INTO Category
                ( id, follower_id, author_id, created_id)
            VALUES
                ( ?, ?, ?, ? )
            """, (new_category['id'], new_category['follower_id'], new_category['author_id'], new_category['created_id'], ))
        
        id = db_cursor.lastrowid
        
        new_category['id'] = id
    
    return new_category

def update_category(id, new_category):
    with sqlite3.connect("./rare.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            UPDATE Category
                SET
                    follower_id = ?,
                    author_id = ?,
                    created_id = ?
            WHERE id = ?
            """, (new_category['id'], new_category['follower_id'], new_category['author_id'], new_category['created_id'], ))

def delete_category(id):
    with sqlite3.connect("./rare.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            DELETE FROM Category
            WHERE id = ?
            """, (id, ))

def get_all_categorys():
    with sqlite3.connect("./rare.sqlite3") as conn:
        
        categorys = []
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            SELECT
                s.id,
                s.follower_id,
                s.author_id,
                s.created_id
            FROM Category s
                """)
        
        data = db_cursor.fetchall()
        
        for row in data:

            category = category(row['id'], row['follower_id'], row['author_id'], row['created_id'])
            categorys.append(category.__dict__)
        
        return categorys

def get_single_category(id):
    with sqlite3.connect("./rare.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            SELECT
                s.id,
                s.follower_id,
                s.author_id,
                s.created_id
            FROM Category s
            WHERE s.id = ?
            """, ( id, ))
        
        data = db_cursor.fetchone()
        
        category = category(row['id'], row['follower_id'], row['author_id'], row['created_id'])
        
        return category.__dict__
