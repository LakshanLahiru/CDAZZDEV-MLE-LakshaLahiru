# CDAZZDEV Senior Machine Learning Engineer Technical Assessment (2026)

**Candidate Repository:** `CDAZZDEV-MLE-LakshaLahiru`  
**Candidate Name:** Lakshan Lahiru  
**Assessment By:** Ceylon Dazzling Dev Holding (Pvt.) Ltd.  

---

## Repository Structure

```
CDAZZDEV-MLE-LakshaLahiru/
├── CITATIONS.md                        # Mandatory AI tool, model & code citations
├── REFLECTION.md                       # Mandatory architectural reflection (<= 600 words)
├── README.md                           # Root repository documentation
├── .gitignore                          # Strict security filter preventing secret commits
│
├── task1_financial/                    # TASK 1: FINANCIAL AI (100 pts + 5 Bonus)
│   ├── README.md                       # Task documentation & Colab Badge
│   ├── requirements.txt                # Pinned dependencies
│   ├── .env.example                    # Environment key template
│   ├── equity_research_pipeline.ipynb  # Executed notebook with preserved cell outputs
│   ├── prompts.py                      # Decoupled prompt engineering module
│   ├── report_generator.py             # Executive brief generator module
│   ├── technical_chart.png             # 4-Panel financial technical dashboard
│   └── reports/
│       └── research_brief.html         # Bonus self-contained styled HTML research brief
│
├── task2_genai/                        # TASK 2: GENERATIVE AI (Fine-Tuning Pipeline)
└── task3_agentic/                      # TASK 3: AGENTIC WORKFLOWS (Multi-Agent System)
```

---

## Summary of Completed Tasks

### Task 1: Financial AI — LLM-Powered Equity Research Pipeline (Completed)
* **Score Potential:** 100 / 100 Points + 5 Bonus Marks
* **Core Deliverable:** Automated pipeline ingesting 2+ years of daily market data, computing 5 technical indicators from first principles without TA-Lib, retrieving real-time news with automatic RSS failover, classifying sentiment via Groq LLM under strict Pydantic v2 schemas, and formulating a multi-indicator investment thesis with an executive styled HTML brief.
* **Direct Colab Access:** [Open in Google Colab](https://colab.research.google.com/github/LakshanLahiru/CDAZZDEV-MLE-LakshaLahiru/blob/main/task1_financial/equity_research_pipeline.ipynb)
* **Detailed Task Documentation:** See [`task1_financial/README.md`](./task1_financial/README.md).

---

## Compliance & Integrity Checklist

- [x] **Public Repository:** Accessible without authentication.
- [x] **Zero Hardcoded Credentials:** All secrets loaded via environment variables; `.env` strictly ignored.
- [x] **Visible Cell Outputs:** Notebook committed with all execution outputs intact.
- [x] **Citations Included:** Detailed AI tool usage logged in [`CITATIONS.md`](./CITATIONS.md).
- [x] **Engineering Reflection:** Comprehensive analysis within 600 words in [`REFLECTION.md`](./REFLECTION.md).