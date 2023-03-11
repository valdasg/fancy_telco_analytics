# Simple analytics pipeline for Fancy Telco Co.

### Decsription

Repository consists of two parts:
- Python scripts solving sample problems located at [tasks](./tasks/) directory.
- Ingestion script and SQL analytics scripts

### Inngestion
PostgreSQL database on localhost is used in as database of choice.
Raw data is stored at [raw](./tasks/) directory.
Directory contains cell and site data as csv files. Two types of data is stored:
- cell data
- site data
It is assumed that data is allways overwritten upon landing and there are only two sources of files as per above.
Script uses functions in [utils](./utils.py) file to load the data to postgress at the same time adding source as
a separate column.
Sript is executed running [mail](./utils.py) file.

# Recreate exectution
Create a directory at location of your choice and clone the repo:
```
git clone <repo-url>
```
Script uses psycopg2 external library, install it before running it by typing following in terminal.

While in directory create virtual environment
```
python3 -m venn .venv
```
and install psycopg2
```
pip install psycopg2-binary --force-reinstall --no-cache-dir
```
Enter your credentials of your PostgreSQL instance while executing [main](./utils.py) file.

Run [SQL script](./sql_scripts.sql) of your choice to analize dada.
