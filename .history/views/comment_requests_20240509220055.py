import sqlite3
from models import Comment



def get_all_comments():
    """Function to get all comments"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.author_id,
            c.post_id,
            c.content
        FROM Comments c
        """)

        # Initialize an empty list to hold all comments
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:
            # Create a Comment instance from the current row
            comment = Comment(row['id'], row['author_id'], row['post_id'], row['content'])
            comments.append(comment.__dict__)

    return comments


def update_comment(id, new_comment):
    """Updates comment"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                author_id = ?,
                post_id = ?,
                content = ?,
        WHERE id = ?
        """, (new_comment['author_id'], new_comment['post_id'],
              new_comment['content'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    # return value of this function
    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
    
def delete_comment(id):
    """Function to delete a comment"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))

def create_comment(new_comment):
    """Creates a new comment"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            (id,author_id, post_id, content)
        VALUES
            (?,?, ?, ?);
        """, (new_comment['id'],new_comment['author_id'], new_comment['post_id'], new_comment['content']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the comment dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id

    return new_comment

def get_single_comment(id):
    """Variable to hold a single comment if it exists"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.author_id,
            c.post_id,
            c.content
        FROM Comments c
        WHERE c.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a comment instance from the current row
        comment = Comment(data['id'], data['author_id'], data['post_id'], data['content'])

        return comment.__dict__
