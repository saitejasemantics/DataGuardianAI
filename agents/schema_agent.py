import pandas as pd


class SchemaAgent:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def investigate(self):

        findings = []

        for _, row in self.df.iterrows():

            findings.append(
                {
                    "table": row["table_name"],
                    "column": row["column_name"],
                    "change": row["change_type"]
                }
            )

        return findings