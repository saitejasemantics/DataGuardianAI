# agents/dq_agent.py

import pandas as pd


class DataQualityAgent:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def investigate(self):

        issues = []

        for _, row in self.df.iterrows():

            if row["completeness_percent"] < 90:

                issues.append({
                    "table": row["table_name"],
                    "completeness": row["completeness_percent"],
                    "null_rate": row["null_rate"]
                })

        return issues