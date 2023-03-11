
import psycopg2, glob

def get_table_name(path: str) -> str:
    '''
    Function takes directory path as argument 
    and returns a table name as file name stripping off extension
    '''
    return path.split('/')[7].split('.')[0]

def create_dbs(database: str, user: str, password: str, host: str, port: str, source_dir: str):
    '''
    Function takes postgress database connection parameters
    and source directory and creates tables one per file.
    '''
    print('Starting creation of tables...')
    
    paths = (glob.glob(source_dir))
    
    print(f'Getting paths: {paths}')
    
    print('Establishing connection to database...')
    
    try:
        conn=psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)

    cursor = conn.cursor()

    # Generating tables while looping through files in source folder
    for path in paths:
        table = get_table_name(path)
        print(f'Generating table {table}...')
        try:
            if table == 'site':
                sql = f'''
                    DROP TABLE IF EXISTS {table};
                    CREATE TABLE {table} (  
                        year INT,
                        month INT,
                        day INT,
                        site_id INT
                    );

                    COPY {table} (
                        year,
                        month,
                        day,
                        site_id)
                    FROM '{path}'
                    WITH DELIMITER ';'
                    CSV HEADER;
                    '''
                # Execute query
                cursor.execute(sql, path)
                
                # Commit changes
                conn.commit()
                                
                print(f"Done with {table}.csv!")
            else:
                sql = f'''
                    DROP TABLE IF EXISTS temp_{table};
                    CREATE TEMP TABLE temp_{table} (  
                        year INT,
                        month INT,
                        day INT,
                        cell_identity VARCHAR(32),
                        frequency_band INT,
                        site_id INT
                    );
                    
                    COPY temp_{table} (
                        year,
                        month,
                        day,
                        cell_identity,
                        frequency_band,
                        site_id)
                    FROM '{path}'
                    WITH DELIMITER ';'
                    CSV HEADER;
                    
                    ALTER TABLE temp_{table}
                    ADD technology VARCHAR(32) ;
                    
                    UPDATE temp_{table}
                    SET technology = '{table}';
                    
                    DROP TABLE IF EXISTS {table};
                    CREATE TABLE {table} AS
                    SELECT * FROM temp_{table};
                    '''

                # Execute query
                cursor.execute(sql, path)
                print(f"Done with {table}.csv!")

                # Commit changes
                conn.commit()
                
        except Exception:
            print(f'SQL injection of {table} failed.')
            exit (1)
            
    # Closing the connection
    print('Creation of tables complete, closing connection, exiting...')
    conn.close()

        


