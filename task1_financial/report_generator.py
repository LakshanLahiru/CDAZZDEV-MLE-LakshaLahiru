# AI-ASSISTED: Gemini, Prompt: 'Create standalone modular report generator module for equity research brief', Date: 2026-10-07

"""
report_generator.py
===================
Handles export and rendering of the executive equity research brief
into styled HTML/PDF format with embedded charts and regulatory disclaimers.
"""

import base64
import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger("EquityPipeline")

# ==============================================================================
# MANDATORY REGULATORY DISCLAIMER CONSTANT
# ==============================================================================
FINANCIAL_RISK_DISCLAIMER = """
<strong>MANDATORY REGULATORY & FINANCIAL RISK DISCLAIMER:</strong><br>
This equity research document is generated automatically by an experimental Machine Learning
and LLM-driven research pipeline for technical assessment purposes only. It does not constitute
financial, investment, legal, or tax advice, nor is it a solicitation to buy or sell securities.
Past performance and quantitative indicators are not predictive of future returns. Equity markets
are subject to significant volatility and capital loss. Always conduct independent due diligence
or consult a licensed financial advisor before making investment decisions.
"""


def generate_html_equity_report(
    summary: dict,
    latest_indicators: pd.Series,
    sentiment,
    recommendation,
    chart_image_path: str = "technical_chart.png",
    output_html_path: str = "reports/research_brief.html"
) -> str:
    """
    Renders a publication-grade single-page executive equity brief in HTML.
    Encodes technical charts to base64 for self-contained portability.
    """
    Path("reports").mkdir(parents=True, exist_ok=True)
    
    # 1. Encode chart to Base64
    chart_b64 = ""
    if Path(chart_image_path).exists():
        with open(chart_image_path, "rb") as img_file:
            chart_b64 = base64.b64encode(img_file.read()).decode("utf-8")
            
    # 2. Top 3 headlines rows
    top_3_news = sentiment.headline_results[:3]
    news_rows_html = ""
    for item in top_3_news:
        badge_color = (
            "#16a34a" if item.sentiment == "positive"
            else ("#dc2626" if item.sentiment == "negative" else "#6b7280")
        )
        news_rows_html += f"""
        <tr>
            <td style="padding: 10px 12px; font-weight: 500; color: #1e293b;">{item.headline}</td>
            <td style="padding: 10px 12px; text-align: center;">
                <span style="background: {badge_color}1a; color: {badge_color}; padding: 3px 10px; border-radius: 999px; font-size: 11px; font-weight: 700; text-transform: uppercase;">
                    {item.sentiment}
                </span>
            </td>
            <td style="padding: 10px 12px; text-align: center; font-size: 13px; font-weight: 600; color: #334155;">{item.confidence * 100:.0f}%</td>
            <td style="padding: 10px 12px; font-size: 12px; color: #64748b;">{item.brief_reason}</td>
        </tr>
        """
        
    rec_color = (
        "#16a34a" if recommendation.recommendation == "BUY"
        else ("#dc2626" if recommendation.recommendation == "SELL" else "#d97706")
    )
    
    drivers_html = "".join([f"<li style='margin-bottom: 4px;'>{d}</li>" for d in recommendation.primary_drivers])
    risks_html = "".join([f"<li style='margin-bottom: 4px;'>{r}</li>" for r in recommendation.key_risks])

    # 3. Assemble Full Styled HTML
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{summary['ticker']} Equity Research Brief</title>
<style>
    body {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background: #f8fafc;
        color: #0f172a;
        margin: 0;
        padding: 24px;
        line-height: 1.5;
    }}
    .container {{
        max-width: 1080px;
        margin: 0 auto;
        background: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.08);
        padding: 32px;
        border: 1px solid #e2e8f0;
    }}
    .header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #0f172a;
        padding-bottom: 16px;
        margin-bottom: 24px;
    }}
    .badge-signal {{
        background: {rec_color};
        color: white;
        padding: 8px 24px;
        border-radius: 8px;
        font-size: 20px;
        font-weight: 800;
        letter-spacing: 1px;
    }}
    .grid-4 {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-bottom: 24px;
    }}
    .card {{
        background: #f1f5f9;
        padding: 16px;
        border-radius: 8px;
        border-left: 4px solid #2563eb;
    }}
    .card-label {{ font-size: 11px; text-transform: uppercase; color: #64748b; font-weight: 700; }}
    .card-val {{ font-size: 22px; font-weight: 800; color: #0f172a; margin-top: 4px; }}
    .section-title {{
        font-size: 16px;
        font-weight: 800;
        text-transform: uppercase;
        color: #1e293b;
        letter-spacing: 0.5px;
        margin: 24px 0 12px 0;
        border-bottom: 1px solid #cbd5e1;
        padding-bottom: 6px;
    }}
    .rec-box {{
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-left: 6px solid {rec_color};
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 24px;
    }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 13px; }}
    th {{ background: #f8fafc; padding: 10px 12px; text-align: left; font-weight: 700; color: #475569; border-bottom: 1px solid #cbd5e1; }}
    tr:nth-child(even) {{ background: #f8fafc; }}
    .chart-container {{ text-align: center; margin: 24px 0; }}
    .chart-container img {{ max-width: 100%; border-radius: 8px; border: 1px solid #e2e8f0; }}
    .disclaimer {{
        background: #fffbeb;
        border: 1px solid #fef3c7;
        padding: 16px;
        border-radius: 8px;
        font-size: 11px;
        color: #92400e;
        line-height: 1.6;
        margin-top: 32px;
    }}
</style>
</head>
<body>
<div class="container">
    <div class="header">
        <div>
            <h1 style="margin: 0; font-size: 28px; font-weight: 900; color: #0f172a;">{summary['ticker']} EQUITY RESEARCH BRIEF</h1>
            <p style="margin: 4px 0 0 0; color: #64748b; font-size: 13px;">Automated Financial Intelligence Pipeline • As of {summary['as_of_date']}</p>
        </div>
        <div style="text-align: right;">
            <div class="badge-signal">{recommendation.recommendation}</div>
            <div style="font-size: 12px; color: #64748b; margin-top: 4px; font-weight: 600;">Confidence: {recommendation.confidence * 100:.0f}%</div>
        </div>
    </div>

    <!-- 1. COMPANY SNAPSHOT -->
    <div class="grid-4">
        <div class="card">
            <div class="card-label">Current Close Price</div>
            <div class="card-val">${summary['current_price']:.2f}</div>
        </div>
        <div class="card">
            <div class="card-label">52-Week Range</div>
            <div class="card-val" style="font-size: 18px;">${summary['52_week_low']:.1f} - ${summary['52_week_high']:.1f}</div>
        </div>
        <div class="card">
            <div class="card-label">P/E Ratio</div>
            <div class="card-val">{summary['pe_ratio'] if summary['pe_ratio'] is not None else 'N/A'}</div>
        </div>
        <div class="card">
            <div class="card-label">YTD Return</div>
            <div class="card-val" style="color: {'#16a34a' if summary['ytd_return_pct'] >= 0 else '#dc2626'};">{summary['ytd_return_pct']:+.2f}%</div>
        </div>
    </div>

    <!-- 2. LLM RECOMMENDATION -->
    <div class="rec-box">
        <h3 style="margin-top: 0; color: #0f172a; font-size: 18px;">Investment Thesis & Reasoning</h3>
        <p style="font-size: 15px; color: #334155; line-height: 1.7; font-weight: 500;">
            "{recommendation.justification}"
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 16px;">
            <div>
                <strong style="color: #16a34a; font-size: 13px; text-transform: uppercase;">Primary Drivers:</strong>
                <ul style="margin: 6px 0 0 16px; padding: 0; font-size: 13px; color: #334155;">
                    {drivers_html}
                </ul>
            </div>
            <div>
                <strong style="color: #dc2626; font-size: 13px; text-transform: uppercase;">Identified Key Risks:</strong>
                <ul style="margin: 6px 0 0 16px; padding: 0; font-size: 13px; color: #334155;">
                    {risks_html}
                </ul>
            </div>
        </div>
    </div>

    <!-- 3. TECHNICAL OUTLOOK -->
    <div class="section-title">Technical Outlook & Indicator Matrix</div>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 20px; font-size: 13px;">
        <div style="background: #f8fafc; padding: 12px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong>Moving Averages:</strong><br>
            • 50 SMA: ${latest_indicators['SMA_50']:.2f}<br>
            • 200 SMA: ${latest_indicators['SMA_200']:.2f}<br>
            • Regime: {'Golden Cross' if latest_indicators['SMA_50'] > latest_indicators['SMA_200'] else 'Death Cross'}
        </div>
        <div style="background: #f8fafc; padding: 12px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong>Momentum Oscillators:</strong><br>
            • RSI (14 Wilder): {latest_indicators['RSI_14']:.2f}<br>
            • MACD Hist: {latest_indicators['MACD_Hist']:.3f}<br>
            • Momentum Signal: {summary['momentum_signal']} ({summary['momentum_score']})
        </div>
        <div style="background: #f8fafc; padding: 12px; border-radius: 6px; border: 1px solid #e2e8f0;">
            <strong>Bollinger Bands (20, 2σ):</strong><br>
            • Lower: ${latest_indicators['BB_Lower']:.2f}<br>
            • Upper: ${latest_indicators['BB_Upper']:.2f}<br>
            • %B Relative: {latest_indicators['BB_Percent_B']:.2f}
        </div>
    </div>

    <!-- 4. EMBEDDED TECHNICAL CHART -->
    <div class="chart-container">
        <img src="data:image/png;base64,{chart_b64}" alt="Technical Dashboard for {summary['ticker']}">
    </div>

    <!-- 5. NEWS SENTIMENT SUMMARY -->
    <div class="section-title">Recent Market News Sentiment (Top 3 Headlines)</div>
    <p style="font-size: 12px; color: #64748b; margin-top: -6px;">
        Overall News Bias: <strong>{sentiment.overall_sentiment}</strong> (Net Sentiment Score: {sentiment.net_sentiment_score:+.3f})
    </p>
    <table>
        <thead>
            <tr>
                <th style="width: 45%;">Headline</th>
                <th style="width: 12%; text-align: center;">Sentiment</th>
                <th style="width: 10%; text-align: center;">Confidence</th>
                <th style="width: 33%;">Analytical Reason</th>
            </tr>
        </thead>
        <tbody>
            {news_rows_html}
        </tbody>
    </table>

    <!-- 6. MANDATORY REGULATORY RISK DISCLAIMER -->
    <div class="disclaimer">
        {FINANCIAL_RISK_DISCLAIMER}
    </div>
</div>
</body>
</html>
"""
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    logger.info(f"Report successfully rendered and saved to '{output_html_path}'.")
    return output_html_path
