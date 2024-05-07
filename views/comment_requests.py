import sqlite3
import json
from models import Comment

COMMENTS = [
    {
        
    }
]

def get_all_comments():
    """Function to get all comments"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.author_id,
            c.post_id,
            c.content,
            c.password
        FROM comment a
        """)

        # Initialize an empty list to hold all location representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an comment instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # comment class above.
            comment = Comment(row['id'], row['author_id'], row['post_id'], row['content'])

            comments.append(comment.__dict__)

    return comments