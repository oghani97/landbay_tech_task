import awsfile
import pandas as pd
import sqlite3


def main():
    df = pd.read_csv('/Users/og/Documents/landbay_tech_task/data/data_task_part_1.csv')

    con = sqlite3.connect("landbay.db")

    df.to_sql(
        'mortgage_data',
        con,
        if_exists='replace'
    )

    cursor = con.cursor()
    cursor.execute("""
    SELECT SUM(total_commission) AS total_commission
        FROM (
    SELECT BROKER_ID,
        SUM(
            CASE
                WHEN case_count <= 15 THEN LOAN_AMOUNT * 0.01
                WHEN case_count <= 30 THEN LOAN_AMOUNT * 0.03
            ELSE LOAN_AMOUNT * 0.05
        END
        ) AS total_commission
    FROM (
        SELECT BROKER_ID, LOAN_AMOUNT,
            ROW_NUMBER() OVER (PARTITION BY BROKER_ID ORDER BY APPLICATION_SUBMITTED_DATE) AS case_count
        FROM mortgage_data
        WHERE strftime('%Y', APPLICATION_SUBMITTED_DATE) = '2021' AND BROKER_ID = '00ca468e-3630-4fe6-b0fd-86f6d27e3b40'
        ) 
    GROUP BY BROKER_ID
);
""")
    print(cursor.fetchall())


if __name__ == "__main__":
    main()
