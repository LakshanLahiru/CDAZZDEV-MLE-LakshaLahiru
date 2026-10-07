# Task 1: LLM-Powered Equity Research Pipeline

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LakshanLahiru/CDAZZDEV-MLE-LakshaLahiru/blob/main/task1_financial/equity_research_pipeline.ipynb)

> **Role Assessment:** Senior Machine Learning Engineer Technical Assessment  
> **Candidate:** Lakshan Lahiru (`CDAZZDEV-MLE-LakshaLahiru`)  
> **Domain:** Financial AI (100 Points + 5 Bonus Marks)

---

## Overview

This module implements an automated, production-grade financial research assistant that ingests market data, computes quantitative technical indicators from first principles without external math libraries, applies LLM reasoning over combinations of indicators, and outputs a validated equity research thesis and executive report.

---

## Key Deliverables & Architecture

```
task1_financial/
├── equity_research_pipeline.ipynb  # Fully executed notebook with visible outputs
├── prompts.py                      # Decoupled prompt templates for sentiment & trade signal
├── report_generator.py             # Modular HTML generator with embedded charts
├── technical_chart.png             # 4-Panel publication-quality financial chart
├── reports/
│   └── research_brief.html         # Self-contained styled HTML executive brief
├── requirements.txt                # Locked dependencies
└── .env.example                    # Template for Groq API key
```

---

## Core Technical Features

### 1. Task 1A: Financial Data Pipeline (60 Points)
* **Dynamic Ingestion (No Hardcoded Dates):** Fetches $\ge 2$ years of daily OHLCV bars via `yfinance` with an automated 120-day historical buffer to ensure rolling indicators (e.g., 200-day SMA) have valid data across the full window.
* **First-Principles Indicators (Strictly NO TA-Lib):**
  * **50-Day & 200-Day SMA:** Arithmetic rolling means with Golden/Death cross detection.
  * **RSI (Period 14):** Welles Wilder exponential smoothing ($\alpha = 1/14$) handling zero-loss boundaries.
  * **MACD (12, 26, 9):** Fast EMA (12), Slow EMA (26), Signal EMA (9), and divergence histogram.
  * **Bollinger Bands (20-day, $2\sigma$):** Upper, middle, and lower volatility bands with $\%B$ ratio.
* **Fault-Tolerant News Retrieval:** Ingests $\ge 10$ recent news items via `yfinance` with automatic fallback to Yahoo Finance RSS XML feed.
* **Summary Dictionary & Momentum Signal:** Produces clean dictionary with 52-week range, P/E ratio, YTD return, and a composite algorithmic momentum score ($-5$ to $+5$).

### 2. Task 1B: LLM Reasoning & Validation (40 Points)
* **Pydantic v2 Schema Enforcement:** Validates all LLM outputs (`HeadlineSentiment` and `InvestmentRecommendation`) under JSON mode with retry loops.
* **Decoupled Prompt Engineering:** All system personas and prompt templates are isolated in `prompts.py`.
* **Multi-Indicator Reasoning:** LLM synthesizes interactions across multiple technical indicators (rather than echoing raw numbers) to formulate a reasoned Buy/Hold/Sell signal with a 3–5 sentence justification.
* **Inference Engine:** Powered by Groq Cloud API (`openai/gpt-oss-120b`).

### 3. Bonus Deliverable: Executive Brief (+5 Points)
* Standalone single-page research brief rendered in styled HTML with responsive cards, badges, and the mandatory financial risk disclaimer.
* Technical dashboard embedded directly using inline Base64 data encoding.

---

## Quickstart

### 1. Local Environment Setup
```bash
# Clone the repository
git clone https://github.com/LakshanLahiru/CDAZZDEV-MLE-LakshaLahiru.git
cd CDAZZDEV-MLE-LakshaLahiru/task1_financial

# Install dependencies
pip install -r requirements.txt

# Configure API Key
cp .env.example .env
# Add your GROQ_API_KEY inside .env
```

### 2. Run the Pipeline
Open and run `equity_research_pipeline.ipynb` in Antigravity / Jupyter, or click the [Open In Colab](https://colab.research.google.com/github/LakshanLahiru/CDAZZDEV-MLE-LakshaLahiru/blob/main/task1_financial/equity_research_pipeline.ipynb) badge above.
