from agents.recommendation_agent import RecommendationAgent

root_causes = [
    {
        "root_cause": "Schema Drift",
        "confidence": "HIGH"
    },
    {
        "root_cause": "Data Quality Degradation",
        "confidence": "MEDIUM"
    }
]

agent = RecommendationAgent()

recommendations = agent.recommend(root_causes)

print(recommendations)