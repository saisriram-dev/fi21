import json
import pandas as pd

path = input("Enter the path to the CSV file: ")
df = pd.read_csv(path)

out_path = input("Enter the path to save the JSON report: ")


class CSVAnalyzer:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        report = {}

        for column in self.df.columns:
            column_report = {
                "data_type": str(self.df[column].dtype),
                "unique_values": int(self.df[column].nunique()),
                "duplicate_values": int(self.df[column].duplicated().sum()),
            }

            # Missing values
            if self.df[column].dtype in ["object", "string"]:
                missing_count = (
                    self.df[column].isnull()
                    | self.df[column].astype(str).str.strip().eq("")
                ).sum()
            else:
                missing_count = self.df[column].isnull().sum()

            column_report["missing_values"] = int(missing_count)

            # Numeric stats
            if pd.api.types.is_numeric_dtype(self.df[column]):
                desc = self.df[column].describe()

                column_report["summary"] = {
                    "count": float(desc["count"]),
                    "mean": float(desc["mean"]),
                    "std": float(desc["std"]),
                    "min": float(desc["min"]),
                    "25%": float(desc["25%"]),
                    "50%": float(desc["50%"]),
                    "75%": float(desc["75%"]),
                    "max": float(desc["max"]),
                }

            # String stats
            elif self.df[column].dtype in ["object", "string"]:
                desc = self.df[column].describe()

                column_report["summary"] = {
                    "count": int(desc["count"]),
                    "top": str(desc["top"]) if "top" in desc else None,
                    "freq": int(desc["freq"]) if "freq" in desc else None,
                }

            report[column] = column_report

        with open(out_path, "w") as file:
            json.dump(report, file, indent=4)


analyzer = CSVAnalyzer(df)
analyzer.generate_report()

print(f"JSON report saved successfully to: {out_path}")
