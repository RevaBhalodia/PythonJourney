class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        self.connection = {"status": "open"}
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection.")
        self.connection["status"] = "closed"
        return False  # Don't suppress exceptions

with DatabaseConnection("students_db") as conn:
    print(f"Connection status: {conn['status']}")