import sys
from pathlib import Path
import pandas as pd

# Fix import issue when running Streamlit
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import streamlit as st

from agents.pipeline_agent import PipelineAgent
from agents.dq_agent import DataQualityAgent
from agents.schema_agent import SchemaAgent
from agents.rootcause_agent import RootCauseAgent

from agents.business_impact_agent import BusinessImpactAgent
from agents.recommendation_agent import RecommendationAgent
from agents.executive_agent import ExecutiveAgent

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="DataGuardian AI",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🛡️ DataGuardian AI")

    st.info(
        """
        Multi-Agent Data Quality &
        Root Cause Intelligence Platform
        """
    )

    st.markdown("---")

    st.write("### Challenge Track")

    st.write("✅ Reasoning Agents")
    st.write("✅ Enterprise Agents")

    st.markdown("---")

    st.write("Version: 1.0")

# --------------------------------------------------
# Load Agents
# --------------------------------------------------

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

business_agent = BusinessImpactAgent(
    "data/business_impact.csv"
)

recommendation_agent = RecommendationAgent()

executive_agent = ExecutiveAgent()

# --------------------------------------------------
# Execute Investigation
# --------------------------------------------------

pipeline_results = pipeline_agent.investigate()

dq_results = dq_agent.investigate()

schema_results = schema_agent.investigate()

root_results = root_agent.analyze(
    pipeline_results,
    dq_results,
    schema_results
)

business_results = business_agent.assess()

recommendations = recommendation_agent.recommend(
    root_results
)

executive_summary = executive_agent.summarize(
    root_results,
    business_results,
    recommendations
)

# --------------------------------------------------
# Main Header
# --------------------------------------------------

st.title("🛡️ DataGuardian AI")

st.markdown(
    """
    ### Multi-Agent Data Quality & Root Cause Intelligence Platform

    Autonomous AI agents that detect data issues,
    investigate failures, identify root causes,
    assess business impact, and recommend corrective actions.
    """
)

st.divider()

# --------------------------------------------------
# KPI Metrics
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Failed Pipelines",
        value=len(pipeline_results)
    )

with col2:
    st.metric(
        label="DQ Issues",
        value=len(dq_results)
    )

with col3:
    st.metric(
        label="Root Causes",
        value=len(root_results)
    )

st.divider()

# --------------------------------------------------
# Findings Section
# --------------------------------------------------

left_col, right_col = st.columns(2)

with left_col:

    st.subheader("🔍 Pipeline Findings")

    st.dataframe(
        pd.DataFrame(pipeline_results),
        use_container_width=True
    )

    st.subheader("📊 Data Quality Findings")

    st.dataframe(
        pd.DataFrame(dq_results),
        use_container_width=True
    )

with right_col:

    st.subheader("🧩 Schema Findings")

    st.dataframe(
        pd.DataFrame(schema_results),
        use_container_width=True
    )

    st.subheader("🚨 Root Cause Analysis")

    for item in root_results:

        if item["confidence"] == "HIGH":

            st.error(
                f"{item['root_cause']} "
                f"(Confidence: {item['confidence']})"
            )

        else:

            st.warning(
                f"{item['root_cause']} "
                f"(Confidence: {item['confidence']})"
            )

# --------------------------------------------------
# Business Impact
# --------------------------------------------------

st.divider()

st.subheader("📈 Business Impact Analysis")

st.dataframe(
    pd.DataFrame(business_results),
    use_container_width=True
)

# --------------------------------------------------
# Recommendations
# --------------------------------------------------

st.divider()

st.subheader("💡 AI Recommendations")

for rec in recommendations:
    st.success(rec)

# --------------------------------------------------
# Executive Metrics
# --------------------------------------------------

st.divider()

st.subheader("📊 Executive Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Incidents",
        executive_summary["incident_count"]
    )

with col2:
    st.metric(
        "Business Impacts",
        executive_summary["business_impacts"]
    )

with col3:
    st.metric(
        "Recommendations",
        executive_summary["recommendations"]
    )

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

st.divider()

st.subheader("📋 Executive Summary")

st.success(
    """
    DataGuardian AI identified multiple operational
    issues impacting enterprise data reliability.

    Primary Findings:
    • Schema Drift detected in source systems
    • Data Quality degradation observed
    • Pipeline execution failures identified

    Business Impact:
    • Revenue Dashboard affected
    • Customer Dashboard impacted
    • 47,000+ records potentially affected

    Recommended Actions:
    • Implement schema validation checks
    • Add automated data quality monitoring
    • Configure proactive pipeline alerting

    Business Value:
    • Faster root cause analysis
    • Reduced incident resolution time
    • Improved data trust and reliability
    """
)

# --------------------------------------------------
# Agent Workflow
# --------------------------------------------------

st.divider()

st.subheader("🤖 Multi-Agent Workflow")

st.info(
    """
    Pipeline Agent → Data Quality Agent → Schema Agent
    → Root Cause Agent → Business Impact Agent
    → Recommendation Agent → Executive Summary Agent
    """
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Built for Microsoft Agent League Hackathon | DataGuardian AI v1.0"
)