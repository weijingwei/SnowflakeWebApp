from snowflake import connector



def sfconnect():
    cnx = connector.connect(
        account='xda06983',
        user='weijingwei',
        password='Biptwjw@205491',
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC'
    )
    return cnx
