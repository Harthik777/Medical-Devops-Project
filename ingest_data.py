import pandas as pd
from sqlalchemy import create_engine
import os

# --- Configuration ---
csv_file = 'medical_images_metadata.csv'
table_name = 'image_metadata'

# Database connection details from your docker-compose.yml
user = 'myuser'
password = 'mypassword'
host = 'localhost'
port = '5432'
db = 'medicaldata'
# -------------------

print(f"➡️ Starting ingestion process for '{csv_file}'...")

if not os.path.exists(csv_file):
    print(f"❌ Error: The file '{csv_file}' was not found.")
else:
    try:
        connection_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
        engine = create_engine(connection_url)

        df = pd.read_csv(csv_file)
        print(f"✅ Read {len(df)} rows from CSV. Writing to PostgreSQL table '{table_name}'...")

        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"🎉 Success! Ingestion complete. All {len(df)} records are in the '{table_name}' table.")

    except Exception as e:
        print(f"❌ An error occurred during ingestion: {e}")