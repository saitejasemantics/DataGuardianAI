from agents.pipeline_agent import PipelineAgent

agent = PipelineAgent(
    "data/pipeline_logs.csv"
)

results = agent.investigate()

print(results)