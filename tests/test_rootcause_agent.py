from agents.pipeline_agent import PipelineAgent
from agents.dq_agent import DataQualityAgent
from agents.schema_agent import SchemaAgent
from agents.rootcause_agent import RootCauseAgent

pipeline = PipelineAgent(
    "data/pipeline_logs.csv"
)

dq = DataQualityAgent(
    "data/data_quality_metrics.csv"
)

schema = SchemaAgent(
    "data/schema_changes.csv"
)

root = RootCauseAgent()

results = root.analyze(
    pipeline.investigate(),
    dq.investigate(),
    schema.investigate()
)

print(results)