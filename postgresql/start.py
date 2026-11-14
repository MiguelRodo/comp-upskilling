import psycopg

with psycopg.connect(
  host="db",
  dbname="clinical_training",
  user="student",
  password="training_password"
) as conn:
  with conn.cursor() as cur:
    cur.execute("SELECT current_database(), current_user;")
    print(cur.fetchone())
