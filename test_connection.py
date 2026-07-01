from utils.databricks import execute_query

df = execute_query("""

SELECT *

FROM gitobservatory.gold.repository_comparison

LIMIT 5

""")

print(df)