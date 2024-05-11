import sqlite3
import json
from models import Subscription

def create_subscription(new_subscription):
    with sqlite3.connect("./rare.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            INSERT INTO Subscription
                ( id, follower_id, author_id, created_id)
            VALUES
                ( ?, ?, ?, ? )
            """, (new_subscription['id'], new_subscription['follower_id'], new_subscription['author_id'], new_subscription['created_id'], ))
        
        id = db_cursor.lastrowid
        
        new_subscription['id'] = id
    
    return new_subscription

def delete_subscription(id):
    with sqlite3.connect("./rare.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            DELETE FROM Subscription
            WHERE id = ?
            """, (id, ))

def get_all_subscriptions():
    with sqlite3.connect("./rare.sqlite3") as conn:
        
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

            subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_id'])
            subscriptions.append(subscription.__dict__)
        
        return subscriptions

def get_single_subscription(id):
    with sqlite3.connect("./rare.sqlite3") as conn:
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

    