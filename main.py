import seaborn as sns

# Load the built-in 'iris' dataset from seaborn into a DataFrame
iris_df = sns.load_dataset('iris')

# Display the first few rows of the DataFrame
print(f"shape of df is {iris_df.shape}")
print(iris_df.head())