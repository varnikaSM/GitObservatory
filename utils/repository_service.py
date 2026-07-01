from utils.databricks import execute_query

def get_repository_comparison():

    query = """
    SELECT *
    FROM gitobservatory.gold.repository_comparison
    """

    return execute_query(query)