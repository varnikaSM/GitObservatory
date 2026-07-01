from utils.repository_service import get_repository_comparison

df = get_repository_comparison()

print(df.columns.tolist())

print(df.head())