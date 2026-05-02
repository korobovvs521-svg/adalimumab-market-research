# visualize_pricing.py
import pandas as pd
import plotly.express as px


def create_spending_bar_chart(df):
    """
    Accepts the Medicare Pricing dataframe, formats the years,
    and returns a stacked bar chart illustrating the Citrate-Free transition.
    """
    plot_df = df.copy()

    # Ensure Data_Year is treated as a discrete category
    plot_df['Data_Year'] = plot_df['Data_Year'].astype(str)

    # Chart A: The Citrate-Free Cannibalization Strategy
    fig = px.bar(
        plot_df,
        x="Data_Year",
        y="Revenue_Billions_USD",
        color="Brand_Name",
        title="Medicare Spending: The Citrate-Free Transition",
        labels={
            "Revenue_Billions_USD": "Medicare Spending (Billions $)",
            "Data_Year": "Year",
            "Brand_Name": "Formulation"
        },
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    # Adjust legend anchor and add a bottom margin to prevent overlap
    fig.update_layout(
        barmode='stack',
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        margin=dict(b=120)
    )

    return fig


def create_cost_line_chart(df):
    """
    Accepts the Medicare Pricing dataframe, filters for primary delivery methods,
    and returns a line chart showing the unit cost trajectory.
    """
    plot_df = df.copy()
    plot_df['Data_Year'] = plot_df['Data_Year'].astype(str)

    # Filter to the primary delivery methods to keep the line chart clean
    main_brands = ['Humira Pen', 'Humira(Cf) Pen', 'Humira', 'Humira(Cf)']
    df_cost = plot_df[plot_df['Brand_Name'].isin(main_brands)]

    # Chart B: The Monopoly Price Hikes
    fig = px.line(
        df_cost,
        x="Data_Year",
        y="Avg_Cost_Per_Unit",
        color="Brand_Name",
        markers=True,
        title="Average Unit Cost Trajectory (Monopoly Premium)",
        labels={
            "Avg_Cost_Per_Unit": "Average Cost Per Unit ($)",
            "Data_Year": "Year",
            "Brand_Name": "Formulation"
        },
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    # Refine aesthetics
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5
        )
    )
    fig.update_traces(line=dict(width=3), marker=dict(size=8))

    return fig