import sqlite3
from models import Post_tags



def get_all_posttags():
    """Function to get all comments"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.tag_id,
            p.post_id,
        FROM PostTags p
        """)

        # Initialize an empty list to hold all comments
        post_tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:
            # Create a Comment instance from the current row
            post_tag = Post_tags(row['id'], row['tag_id'], row['post_id'])
            post_tags.append(post_tag.__dict__)

    return post_tags


def update_posttag(id, new_posttag):
    """Updates comment"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE PostTags
            SET
                tag_id = ?,
                post_id = ?,
        WHERE id = ?
        """, (new_posttag['tag_id'], new_posttag['post_id'], id, ))

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
    
def delete_posttag(id):
    """Function to delete a comment"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE id = ?
        """, (id, ))

def create_posttag(new_posttag):
    """Creates a new comment"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostTags
            (id,tag_id, post_id, content)
        VALUES
            (?,?, ?, ?);
        """, (new_posttag['id'],new_posttag['tag_id'], new_posttag['post_id']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the comment dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_posttag['id'] = id

    return new_posttag

def get_single_posttags(id):
    """Variable to hold a single comment if it exists"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.tag_id,
            p.post_id,
        FROM PostTags p
        WHERE p.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a comment instance from the current row
        post_tag = Post_tags(data['id'], data['tag_id'], data['post_id'])

        return post_tag.__dict__
