# Engineering Reflection

### 1. Architectural Decisions Made
For Task 1, the architecture was designed to transition from typical exploratory notebooks to a production-grade, fault-tolerant financial ML pipeline:

* **First-Principles Vectorized Indicators:** Rather than relying on heavyweight compiled binaries like TA-Lib, all five technical indicators (SMA 50/200, Wilder's RSI 14, MACD 12/26/9, and Bollinger Bands) were implemented using pure `pandas` and `numpy`. Welles Wilder's original exponential smoothing ($\alpha = 1/14$) was preserved precisely. Lookback window constants were explicitly parameterized to eliminate magic numbers.
* **Warm-up Buffer for Dynamic Date Ingestion:** Standard 2-year queries truncate rolling indicators (the 200 SMA produces 199 initial `NaN` values). An automated 120-day historical buffer was introduced dynamically so the full 2-year analysis window remains valid and non-null.
* **Fault-Tolerant News Ingestion:** Because scraping financial endpoints (e.g., `yfinance.Ticker.news`) is prone to rate-limiting and empty payload responses, an automated RSS XML parser fallback was implemented against Yahoo Finance's live feed. This guarantees meeting the $\ge 10$ headline constraint under transient API failures.
* **Decoupled Prompt Logic & Strict Contract Validation:** System personas and user prompts were separated into `prompts.py`. Rather than relying on fragile regex string parsing, all LLM responses were validated against Pydantic v2 schemas (`HeadlineSentiment` and `InvestmentRecommendation`) under JSON mode with retry loops.
* **Self-Contained Report Portability:** The executive brief encodes generated Matplotlib figures into inline Base64 data URIs within a clean CSS grid layout, ensuring the report can be distributed as a single standalone file without broken asset paths.

### 2. Limitations Encountered
* **Free-Tier API Catalog Evolution:** Groq’s fast-moving model catalog required dynamically identifying active models (`openai/gpt-oss-120b`) rather than relying on static model identifiers.
* **Context Depth of Financial News:** Free news endpoints provide headlines and short snippets rather than full-text article bodies or earnings call transcripts, slightly limiting the qualitative depth available to the LLM.
* **Single-Point-in-Time Inference:** While the prompt synthesizes historical indicators, the current pipeline produces a point-in-time recommendation rather than a continuous backtested trading strategy.

### 3. What I Would Improve With More Time
* **Retrieval-Augmented Generation (RAG) on SEC 10-K/10-Q Filings:** Ingest quarterly SEC EDGAR filings via a local ChromaDB vector store, enabling the LLM to cross-reference fundamental debt covenants, risk factors, and revenue guidance against technical momentum.
* **Quantitative Backtesting Engine:** Integrate a backtesting framework (e.g., `vectorbt`) to evaluate historical Sharpe ratio, maximum drawdown, and win-rate of the combined technical/sentiment signal over a 5-year universe.
* **Asynchronous Batch Inference:** Implement `asyncio` batching for LLM headline calls to reduce news sentiment processing latency by $5\times$.
* **Automated CI/CD Verification:** Add GitHub Actions running headless notebook execution and unit tests validating indicator accuracy against ground-truth benchmarks.
