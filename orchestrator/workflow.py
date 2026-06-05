from agents.pipeline_agent import PipelineAgent
from agents.dq_agent import DataQualityAgent
from agents.schema_agent import SchemaAgent
from agents.rootcause_agent import RootCauseAgent

pipeline_agent = PipelineAgent(
    "data/pipeline_logs.csv"
)

dq_agent = DataQualityAgent(
    "data/data_quality_metrics.csv"
)

schema_agent = SchemaAgent(
    "data/schema_changes.csv"
)

root_agent = RootCauseAgent()

pipeline_findings = (
    pipeline_agent.investigate()
)

dq_findings = (
    dq_agent.investigate()
)

schema_findings = (
    schema_agent.investigate()
)

root_causes = root_agent.analyze(
    pipeline_findings,
    dq_findings,
    schema_findings
)

print("\n=== ROOT CAUSE ANALYSIS ===")

for cause in root_causes:

    print(
        f"{cause['root_cause']} "
        f"(Confidence: {cause['confidence']})"
    )