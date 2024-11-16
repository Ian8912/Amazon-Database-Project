import pg8000

def connect():
    return pg8000.connect(
        database = "Amazon_Analysis",
        user = "postgres",
        password = "2IddddI2$$",
        host = "localhost",
        port = 5432
    )

if __name__ == "__main__":
    conn = connect()
    print("Database connection successful")
    conn.close()