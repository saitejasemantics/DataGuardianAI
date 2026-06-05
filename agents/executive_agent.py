class ExecutiveAgent:

    def summarize(
        self,
        root_causes,
        impacts,
        recommendations
    ):

        summary = {
            "incident_count": len(root_causes),
            "business_impacts": len(impacts),
            "recommendations": len(recommendations)
        }

        return summary