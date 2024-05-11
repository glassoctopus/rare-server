import sqlite3
import json
from models import Subscription

def create_subscription(new_subscription):
    """For testing only, this api call is not part of front MVP or ERD"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            INSERT INTO Subscription
                ( id, follower_id, author_id, created_id)
            VALUES
                ( ?, ?, ? )
            """, (new_subscription['follower_id'], 
                  new_subscription['author_id'], 
                  new_subscription['created_id'], ))
        
        id = db_cursor.lastrowid
                
        new_subscription['id'] = id
    
    return new_subscription

def update_subscription(id, new_subscription):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            UPDATE Subscriptions
                SET
                    follower_id = ?,
                    author_id = ?,
                    created_id = ?
            WHERE id = ?
            """, (new_subscription['follower_id'], 
                  new_subscription['author_id'],  
                  new_subscription['created_id'], 
                  id, ))

def delete_subscription(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            DELETE FROM Subscription
            WHERE id = ?
            """, (id, ))

def get_all_subscriptions():
    with sqlite3.connect("./db.sqlite3") as conn:
        
        subscriptions = []
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            SELECT
                s.id,
                s.follower_id,
                s.author_id,
                s.created_id
            FROM Subscription s
                """)
        
        data = db_cursor.fetchall()
        
        for row in data:

            subscription = Subscription(row['id'], 
                                        row['follower_id'], 
                                        row['author_id'], 
                                        row['created_id'])
            subscriptions.append(subscription.__dict__)
        
        return subscriptions

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
        
        subscription = Subscription(data['id'], 
                                    data['follower_id'], 
                                    data['author_id'], 
                                    data['created_id'])
        
        return subscription.__dict__

def get_subscriptions_by_author(author_id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            SELECT
                s.id,
                s.follower_id,
                s.author_id,
                s.created_id,
                u.first_name
            FROM Subscription s
            WHERE s.author_id = ?
            JOIN Users u
                ON s.author_id = u.id                          
        """, ( author_id, ))
        
        