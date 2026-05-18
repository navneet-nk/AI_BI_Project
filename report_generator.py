from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import letter

import matplotlib.pyplot as plt

def generate_pdf_report(
    filtered_data,
    insights,
    forecast_values,
    fig
):

    pdf_file = "analytics_report.pdf"

    chart_image = "chart.png"

    # SAVE CHART IMAGE
    fig.savefig(chart_image)

    # CREATE PDF
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # TITLE
    title = Paragraph(
        "AI Business Analytics Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    # DATASET INFO
    rows = filtered_data.shape[0]

    cols = filtered_data.shape[1]

    dataset_info = Paragraph(
        f"""
        Dataset Rows: {rows}<br/>
        Dataset Columns: {cols}
        """,
        styles['BodyText']
    )

    elements.append(dataset_info)

    elements.append(
        Spacer(1, 20)
    )

    # CHART SECTION
    chart_title = Paragraph(
        "Analytics Chart",
        styles['Heading2']
    )

    elements.append(chart_title)

    chart = Image(
        chart_image,
        width=400,
        height=250
    )

    elements.append(chart)

    elements.append(
        Spacer(1, 20)
    )

    # AI INSIGHTS
    insights_title = Paragraph(
        "AI Insights",
        styles['Heading2']
    )

    elements.append(insights_title)

    for insight in insights:

        p = Paragraph(
            f"• {insight}",
            styles['BodyText']
        )

        elements.append(p)

    elements.append(
        Spacer(1, 20)
    )

    # FORECASTING
    forecast_title = Paragraph(
        "Forecast Predictions",
        styles['Heading2']
    )

    elements.append(forecast_title)

    forecast_text = Paragraph(
        str(forecast_values),
        styles['BodyText']
    )

    elements.append(forecast_text)

    # BUILD PDF
    doc.build(elements)

    return pdf_file