from utils import create_dbs
import os

if __name__ == "__main__":
    create_dbs('postgres', 'postgres', os.environ["PGPASSWORD"], 'localhost', '5432', os.environ["SOURCEDIR"])