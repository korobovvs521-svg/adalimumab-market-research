# visualize_pipeline.py
import pandas as pd
import plotly.express as px

def create_pipeline_chart(df):
    """
    Accepts the Pipeline Intelligence dataframe, processes it,
    and returns the 'Trial Volume by Sponsor & Phase' chart.
    """
    # 1. Data preparation
    phase_counts = df.dropna(subset=['Sponsor', 'Phases']).groupby(['Sponsor', 'Phases']).size().reset_index(
        name='Trial Count')

    top_sponsors = phase_counts.groupby('Sponsor')['Trial Count'].sum().nlargest(6).index
    phase_counts = phase_counts[phase_counts['Sponsor'].isin(top_sponsors)]

    # 2. Chart creation
    fig = px.bar(
        phase_counts,
        x='Sponsor',
        y='Trial Count',
        color='Phases',
        title="Trial Volume by Sponsor & Phase"
    )
    
    return fig
