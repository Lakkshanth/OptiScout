# OptiScout — Enterprise Third-Party AI Risk Governance & OSINT Platform

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-Proprietary%20%26%20Confidential-red.svg)]()

OptiScout is an enterprise-grade Third-Party Risk Management (TPRM) and Open-Source Intelligence (OSINT) platform engineered to discover, evaluate, and govern undisclosed or unmonitored artificial intelligence footprints across institutional vendor ecosystems.

> 📖 **Complete Presenter & Demonstration Guide:** See [`PRESENTATION_GUIDE.md`](./PRESENTATION_GUIDE.md) for the end-to-end presentation walkthrough, talking points, architecture deep dive, and Q&A defense playbook.

---

## 🎯 Key Capabilities

* **Institutional Criticality Scoring:** Deterministic multi-factor tiering driven by data classification (Public, Confidential, Restricted, Highly Restricted/PII), operational dependency (Low to Critical), annual transaction volume, and systemic payment infrastructure role.
* **Evidentiary Strength Tagging:** Rigorously tags every OSINT finding with transparent evidentiary strength (`Strong`, `Moderate`, `Weak`, `Marketing-only`, `None / Unassessed`).
* **Marketing Commentary vs. Genuine Product AI:** Semantically distinguishes between vendors writing thought leadership blog posts vs. vendors deploying active AI models on institutional customer data.
* **Sub-Processor & Model Transparency:** Eliminates guesswork. Names third-party AI foundation models (OpenAI, Anthropic, Bedrock, etc.) only when disclosed; distinguishes data warehouses (Snowflake) and automation engines (Broadcom) from AI model providers.
* **Hybrid OSINT Engine:** Real-time DuckDuckGo domain dorking (`site:{domain}`), deep directory scanning across 13 compliance/security paths (`/privacy`, `/legal/subprocessors`, `trust.{domain}`, `/ai`), and Gemini 3.1 Flash-Lite semantic extraction.
* **1-Click Completed Excel Export:** Automatically populates the official multi-sheet assignment workbook (`Meridian_Vendor_Input.xlsx`), preserving original fonts, styles, and extra sheets (`Field Guide`, `Points to consider`).
* **Interactive TPRM Copilot & Questionnaire Generator:** Ask questions directly against the scraped vendor corpus and generate tailored DPA inquiry questionnaires in one click.

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch Platform
```bash
python run.py
```
*Or directly via Uvicorn:*
```bash
cd advanced_app
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Open Web Interface
Navigate to **`http://localhost:8000`** in your browser.

---

## 📁 Repository Structure
```
OptiScout/
├── advanced_app/
│   ├── main.py                      # FastAPI Backend & Hybrid OSINT Engine
│   ├── static/
│   │   └── index.html               # Modern TPRM Analytics Dashboard
│   ├── assignment_vendors.csv       # Benchmark Institutional Vendor Dataset
│   └── Meridian_Vendor_Input.xlsx   # Official Master Workbook Template
├── PRESENTATION_GUIDE.md            # Exhaustive Demonstration & Architecture Handbook
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
└── run.py                           # 1-Click root launcher script
```

---

## 📊 Benchmark Vendor Results Overview

| ID | Vendor Name | Category | Crit Tier | AI Detected | Risk Level | Evidentiary Basis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **V-001** | **AutomWorx** | Professional Services | **High** | Inconclusive | **Low (Marketing Only)** | Thought leadership blog on batch automation; no AI in consulting delivery. |
| **V-002** | **Fiserv, Inc.** | Core Platform | **Critical** | **Yes** | **Critical** | SEC Form 10-K: AI embedded in DNA/Finxact account processing solutions. |
| **V-003** | **FSSI** | Document & Comms | **Medium** | Inconclusive | **Low (Unverified)** | 19M customer statements; passive scan found no disclosures; unverified OCR. |
| **V-004** | **Terrapin Tech** | Data & Reporting | **Medium** | Inconclusive | **Low (Marketing Only)** | Wealth data platform; commentary on AI data readiness; no operational models. |
| **V-005** | **BNY** | Payments | **Critical** | **Yes** | **Critical** | Deploys proprietary Eliza enterprise AI across Global Payments & Trade. |
| **V-006** | **The Clearing House** | Payments Infrastructure | **Critical** | Inconclusive | **High (Unverified)** | Operates national RTP network (14M msgs); unverified exposure on core rail. |

---

## 🛡️ License & Confidentiality
Proprietary & Confidential. All rights reserved for Meridian Bank case study evaluation.
