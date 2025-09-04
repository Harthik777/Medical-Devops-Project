from pyspark.sql import SparkSession

def main():
    # --- Configuration ---
    postgres_db = "medicaldata"
    postgres_table = "image_metadata"
    postgres_user = "myuser"
    postgres_pwd = "mypassword"
    # Make sure this filename matches the JAR you downloaded
    jdbc_driver_jar = "postgresql-42.7.3.jar" 
    # -------------------

    # Create a SparkSession with a more forceful timezone setting
    spark = SparkSession.builder \
        .appName("PostgreSQL Connection") \
        .config("spark.driver.extraClassPath", jdbc_driver_jar) \
        .config("spark.driver.extraJavaOptions", "-Duser.timezone=Asia/Kolkata") \
        .getOrCreate()
        
    print("SparkSession created successfully.")

    try:
        # Read data from PostgreSQL table
        print(f"Reading data from PostgreSQL table '{postgres_table}'...")
        df = spark.read \
            .format("jdbc") \
            .option("url", f"jdbc:postgresql://localhost:5432/{postgres_db}") \
            .option("dbtable", postgres_table) \
            .option("user", postgres_user) \
            .option("password", postgres_pwd) \
            .option("driver", "org.postgresql.Driver") \
            .load()

        print("✅ Data loaded successfully into a Spark DataFrame.")
        
        # Verify the data by counting the rows
        row_count = df.count()
        print(f"The table contains {row_count} rows.")

        # Show the first 5 rows of your data
        print("Showing the first 5 rows:")
        df.show(5)

    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        # Stop the SparkSession
        spark.stop()
        print("SparkSession stopped.")

if __name__ == "__main__":
    main()