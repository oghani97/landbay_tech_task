import awsfile
import pandas as pd
import sqlite3


def main():
    df = pd.read_csv('/Users/og/Documents/landbay_tech_task/data/data_task_part_1.csv')
    print(df.head(10))
    print(df.columns.tolist())
    print(df['CASE_NUMBER'].nunique())


    con = sqlite3.connect("landbay.db")

    df.to_sql(
        'mortgage_data',
        con,
        if_exists='replace'
    )

    cursor = con.cursor()
    cursor.execute("""
    SELECT COUNT(DISTINCT BROKER_ID) as "Unique Broker ID"
    FROM mortgage_data
    """)
    print(cursor.fetchall())


if __name__ == "__main__":
    main()