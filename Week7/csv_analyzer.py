import pandas as pd

file_path = input("Enter the path to the CSV file: ")
df = pd.read_csv(file_path)

class CSVAnalyzer:
    def __init__(self, df):
        self.df = df

    def analyze(self):
        print(" A basic analysis of all the columns in the CSV file: ")
        for column in self.df.columns:
            print(f"Column: {column}")
            print(f"Data Type: {self.df[column].dtype}")
            print(f"Number of Unique Values: {self.df[column].nunique()}")
            print(f"Number of Missing Values: {self.df[column].isnull().sum()}")
            print("-" * 40)
    
    def insight(self):
        for column in self.df.columns:
            if self.df[column].dtype in ["int64", "float64"]:
                print(f"\nInsights for the column: {column}")
                print(self.df[column].describe())
                print(f"The number of missing values is: {self.df[column].isnull().sum()}")
                print(f"Number of duplicate values: {self.df[column].duplicated().sum()}")
            elif self.df[column].dtype in ["object", "string"]:
                print(f"\nInsights for the column: {column}")
                print(self.df[column].describe())
                missing_count = (
                    self.df[column].isnull() |
                    self.df[column].astype(str).str.strip().eq("")
                    ).sum()
                print(f"The number of missing values is: {missing_count}")
                print(f"Number of duplicate values: {self.df[column].duplicated().sum()}")
            else:
                print(f"Insights for the column: {column}")
                print(self.df[column].describe())

insight_type = input("How do you want to analyze the csv data (analyze / insight)?: ")
analyzer = CSVAnalyzer(df)

if insight_type == "analyze":
    analyzer.analyze()
elif insight_type == "insight":
    analyzer.insight()
else:
    print("Invalid input. Please enter 'analyze' or 'insight'.")
