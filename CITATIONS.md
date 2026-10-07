# Citations and Attributions Log

In accordance with **Section 2 (AI Tools and Citation Policy)** of the *CDAZZDEV Senior Machine Learning Engineer Technical Assessment*, this document provides an exhaustive record of AI tool usage, code generation prompts, and external open-source references utilized during this assessment.

---

## 1. AI Assistant Usage Log

### Task 1: Financial AI (LLM-Powered Equity Research Pipeline)

1. **OHLCV Dynamic Data Ingestion**
   * **Assistant / Model:** Gemini 3.8 Flash
   * **Date:** 2026-10-07
   * **Prompt:** `'Dynamic 2-year OHLCV data ingestion using yfinance without hardcoded dates and warm-up buffer'`
   * **Scope:** Dynamic datetime computation, schema verification, and missing value cleaning.

2. **Technical Indicators Engine from First Principles**
   * **Assistant / Model:** Gemini 3.8 Flash
   * **Date:** 2026-10-07
   * **Prompt:** `'Calculate 50 SMA, 200 SMA, Wilder RSI 14, MACD (12,26,9), and Bollinger Bands from first principles without TA-Lib'`
   * **Scope:** Vectorized implementations of Welles Wilder decay smoothing, exponential moving average recursion, and standard deviation bands.

3. **Multi-Panel Financial Chart Visualization**
   * **Assistant / Model:** Gemini 3.8 Flash
   * **Date:** 2026-10-07
   * **Prompt:** `'Generate multi-panel technical indicator financial chart with Bollinger Bands, MACD, and RSI using Matplotlib'`
   * **Scope:** Matplotlib 4-panel layout, color-coded volume/MACD histograms, and high-DPI export.

4. **News Ingestion & Financial Summary Dictionary**
   * **Assistant / Model:** Gemini 3.8 Flash
   * **Date:** 2026-10-07
   * **Prompt:** `'Fetch >= 10 news headlines and build summary dictionary with momentum signal and RSS fallback'`
   * **Scope:** Fallback pipeline via Yahoo Finance RSS XML parser, momentum scoring model, and safe dictionary packaging.

5. **Pydantic Validation & Decoupled Prompt Templates**
   * **Assistant / Model:** Gemini 3.8 Flash
   * **Date:** 2026-10-07
   * **Prompt:** `'Define decoupled prompts for financial sentiment and multi-indicator investment reasoning with Pydantic v2 schemas'`
   * **Scope:** Pydantic v2 validation models, system/user persona definitions, and strict JSON schema contracts.

6. **Executive Report Generation & Base64 Chart Embedding**
   * **Assistant / Model:** Gemini 3.8 Flash
   * **Date:** 2026-10-07
   * **Prompt:** `'Create standalone modular report generator module for equity research brief with embedded base64 chart and risk disclaimer'`
   * **Scope:** Clean CSS grid styling, base64 self-contained encoding, and regulatory disclaimer formatting.

---

## 2. LLM Inference APIs & Models

* **Inference Platform:** Groq Cloud API (`console.groq.com`)
* **Primary Model:** `openai/gpt-oss-120b` (and compatible `openai/gpt-oss-20b`)
* **Usage:** Structured per-headline sentiment classification and multi-indicator investment reasoning synthesis under JSON mode (`response_format={"type": "json_object"}`).

---

## 3. Open-Source Libraries & References

* **`yfinance` (v1.7.0):** Yahoo Finance market data scraping interface.
* **`pandas` (v3.0.6) & `numpy` (v2.5.3):** Vectorized mathematical and statistical calculations.
* **`pydantic` (v2.13.5):** Runtime schema validation and JSON serialization.
* **`matplotlib` (v3.11.2):** High-resolution financial charting.
* **`groq` (v1.7.0):** Python client for high-throughput LPU inference.
* **`python-dotenv` (v1.2.4):** Secure environment configuration loading.
