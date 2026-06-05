class RecommendationAgent:

    def recommend(self, root_causes):

        recommendations = []

        for cause in root_causes:

            if cause["root_cause"] == "Schema Drift":

                recommendations.append(
                    "Implement schema validation before pipeline execution."
                )

            elif cause["root_cause"] == "Data Quality Degradation":

                recommendations.append(
                    "Add automated data quality checks and alerting."
                )

        return recommendations