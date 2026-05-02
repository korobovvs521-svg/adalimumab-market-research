# visualize_trials.py
import pandas as pd
import plotly.express as px


def create_gantt_chart(df):
    """
    Accepts the Adalimumab Chart Data (Excel), formats the dates,
    and returns a Plotly Gantt (timeline) chart.
    """
    plot_df = df.copy()

    # Ensure dates are in datetime format for Plotly
    plot_df['Start Date'] = pd.to_datetime(plot_df['Start Date'])
    plot_df['Completion Date'] = pd.to_datetime(plot_df['Completion Date'])

    fig = px.timeline(
        plot_df,
        x_start="Start Date",
        x_end="Completion Date",
        y="Sponsor",
        color="Interchangeable",
        hover_name="Product Name",
        title="Real Data: Adalimumab Late-Stage Pipeline & FDA Status",
        color_discrete_map={True: '#2ca02c', False: '#1f77b4'}
    )

    # Sort the y-axis so sponsors are ordered cleanly
    fig.update_yaxes(categoryorder="total ascending", title="Trial Sponsor")

    return fig


def create_efficiency_scatter(df):
    """
    Accepts the Adalimumab Chart Data (Excel),
    and returns a Plotly scatter plot comparing duration and enrollment.
    """
    plot_df = df.copy()

    fig = px.scatter(
        plot_df,
        x="Trial_Duration_Months",
        y="Enrollment",
        color="Interchangeable",
        hover_name="Sponsor",
        hover_data={"Product Name": True, "Interchangeable": False, "Trial_Duration_Months": True, "Enrollment": True},
        title="Trial Efficiency: Duration vs Enrollment",
        labels={"Trial_Duration_Months": "Trial Duration (Months)", "Enrollment": "Total Patient Enrollment"},
        color_discrete_map={True: '#2ca02c', False: '#1f77b4'}
    )

    # Enhance the marker aesthetics
    fig.update_traces(marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')))

    return fig