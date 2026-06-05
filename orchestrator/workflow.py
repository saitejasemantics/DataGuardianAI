from agents.pipeline_agent import PipelineAgent
from agents.dq_agent import DataQualityAgent
from agents.schema_agent import SchemaAgent

pipeline_agent = PipelineAgent(
    "data/pipeline_logs.csv"
)

dq_agent = DataQualityAgent(
    "data/data_quality_metrics.csv"
)

schema_agent = SchemaAgent(
    "data/schema_changes.csv"
)

print("\n=== PIPELINE FINDINGS ===")
print(pipeline_agent.investigate())

print("\n=== DATA QUALITY FINDINGS ===")
print(dq_agent.investigate())

print("\n=== SCHEMA FINDINGS ===")
print(schema_agent.investigate())