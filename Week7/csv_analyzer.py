import sys
import pandas as pd

def main():
    file_path = sys.argv[1]

    df = pd.read_csv(file_path)

    print("CSV loaded successfully")
    print(df.head())

if __name__ == "__main__":
    main()