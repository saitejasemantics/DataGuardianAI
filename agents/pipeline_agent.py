# agents/pipeline_agent.py

import pandas as pd


class PipelineAgent:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def investigate(self):

        failed_pipelines = self.df[
            self.df["status"] == "FAILED"
        ]

        results = []

        for _, row in failed_pipelines.iterrows():
            results.append({
                "pipeline": row["pipeline_name"],
                "error": row["error_message"]
            })

        return results