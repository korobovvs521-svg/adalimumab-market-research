# visualize_financials.py
import pandas as pd
import plotly.express as px


def create_spend_pie_chart(df):
    """
    Accepts the Financial Intelligence dataframe, groups data by payment category,
    and returns a Plotly donut chart representing total spend.
    """
    # Create a copy to prevent Streamlit cache mutation
    plot_df = df.copy()

    # Aggregate data by payment category
    spend_by_cat = plot_df.groupby('Nature_of_Payment_or_Transfer_of_Value')[
        'Total_Amount_of_Payment_USDollars'].sum().reset_index()

    # Create the donut chart
    fig = px.pie(
        spend_by_cat,
        values='Total_Amount_of_Payment_USDollars',
        names='Nature_of_Payment_or_Transfer_of_Value',
        hole=0.4,
        title="Total Spend by Payment Category"
    )
    fig.update_layout(showlegend=False)

    return fig


def create_physician_bar_chart(df):
    """
    Accepts the Financial Intelligence dataframe, aggregates payments by physician,
    and returns a horizontal Plotly bar chart of the top 10 compensated physicians.
    """
    plot_df = df.copy()

    # Aggregate data by physician name
    top_paid = plot_df.groupby(['Covered_Recipient_First_Name', 'Covered_Recipient_Last_Name'])[
        'Total_Amount_of_Payment_USDollars'].sum().reset_index()
    top_paid['Physician'] = top_paid['Covered_Recipient_First_Name'] + " " + top_paid['Covered_Recipient_Last_Name']

    # Extract top 10 and sort for horizontal bar layout
    top_paid = top_paid.nlargest(10, 'Total_Amount_of_Payment_USDollars').sort_values(
        by='Total_Amount_of_Payment_USDollars', ascending=True)

    # Create the horizontal bar chart
    fig = px.bar(
        top_paid,
        x='Total_Amount_of_Payment_USDollars',
        y='Physician',
        orientation='h',
        title="Top 10 Compensated Physicians",
        color_discrete_sequence=['#2CA02C']
    )

    return fig