import json
import psycopg2

# Database connection parameters
DB_NAME = "leetcode"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "postgres_db"
DB_PORT = "5432"

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# Create table schema
create_table_query = """
CREATE TABLE IF NOT EXISTS leetcode_problems (
    id SERIAL PRIMARY KEY,
    slug TEXT,
    title TEXT,
    difficulty TEXT,
    content TEXT,
    python TEXT
);
"""
cur.execute(create_table_query)
conn.commit()

# Read and transform data
with open('leetcode-train.jsonl', 'r') as file:
    for line in file:
        data = json.loads(line)
        id = data.get('id')
        slug = data.get('slug')
        title = data.get('title')
        difficulty = data.get('difficulty')
        content = data.get('content')
        python = data.get('python')

        # Insert data into the table
        insert_query = """
        INSERT INTO leetcode_problems (id, slug, title, difficulty, content, python)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """
        cur.execute(insert_query, (id, slug, title, difficulty, content, python))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
