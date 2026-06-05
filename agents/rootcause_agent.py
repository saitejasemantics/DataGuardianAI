class RootCauseAgent:

    def analyze(
        self,
        pipeline_findings,
        dq_findings,
        schema_findings
    ):

        root_causes = []

        # Rule 1: Schema Drift

        schema_changes = len(schema_findings) > 0

        pipeline_schema_errors = any(
            "schema" in str(item["error"]).lower()
            or "column" in str(item["error"]).lower()
            for item in pipeline_findings
        )

        if schema_changes and pipeline_schema_errors:

            root_causes.append(
                {
                    "root_cause": "Schema Drift",
                    "confidence": "HIGH"
                }
            )

        # Rule 2: Data Quality Issue

        if len(dq_findings) > 0:

            root_causes.append(
                {
                    "root_cause": "Data Quality Degradation",
                    "confidence": "MEDIUM"
                }
            )

        return root_causes