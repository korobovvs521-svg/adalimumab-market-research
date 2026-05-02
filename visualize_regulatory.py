# visualize_regulatory.py
import pandas as pd
import plotly.express as px


def create_regulatory_chart(df):
    """
    Accepts the Regulatory Timeline dataframe, formats the dates,
    and returns a scatter plot of FDA market entrants.
    """
    # Create a copy to avoid mutating the cached Streamlit dataframe
    plot_df = df.copy()

    # 1. Data Preparation
    plot_df['Approval_Date'] = pd.to_datetime(plot_df['Approval_Date'])

    # 2. Chart Creation
    fig = px.scatter(
        plot_df,
        x='Approval_Date',
        y='Brand_Name',
        color='Is_Interchangeable',
        color_discrete_map={"Yes": "#D4AF37", "No": "#7F8C8D"},
        title="Adalimumab Market Entrants (2002 - Present)"
    )

    # 3. Refine aesthetics
    fig.update_traces(marker=dict(size=15, line=dict(width=2, color='DarkSlateGrey')))

    return fig