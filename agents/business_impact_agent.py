import pandas as pd


class BusinessImpactAgent:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def assess(self):

        impacts = []

        for _, row in self.df.iterrows():

            impacts.append(
                {
                    "dashboard": row["dashboard"],
                    "records": row["affected_records"],
                    "severity": row["severity"]
                }
            )

        return impacts