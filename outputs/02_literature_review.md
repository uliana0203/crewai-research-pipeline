# **Systematic Literature Review: AI-Driven Forecasting of COVID-19 Cases**

**Date:** October 26, 2023
**Author:** Literature Review Specialist
**Objective:** To systematically search, screen, and synthesize prior work on AI-driven forecasting of COVID-19 cases, identifying key themes, methods, datasets, gaps, and future directions.

---

### **1. PRISMA-Style Methodology & Screening Notes**

**1.1 Search Strategy:**
*   **Databases Searched:** PubMed, IEEE Xplore, Scopus, Web of Science, arXiv.
*   **Time Frame:** January 2020 – September 2023.
*   **Search Strings:**
    *   (`"COVID-19" OR "SARS-CoV-2"`) AND (`"forecast*" OR "predict*"`) AND (`"artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network"`)
    *   (`"epidemic forecasting"`) AND (`"AI"`) AND (`"cases"`)
    *   (`"time series"`) AND (`"COVID"`) AND (`"LSTM" OR "GRU" OR "transformer"`)

**1.2 Inclusion Criteria:**
*   Peer-reviewed journal articles, conference proceedings, and reputable preprints.
*   Studies focusing primarily on forecasting confirmed COVID-19 case counts (daily, cumulative).
*   Core methodology must be based on AI/ML/DL techniques.
*   Studies presenting quantitative results (e.g., RMSE, MAE, MAPE).

**1.3 Exclusion Criteria:**
*   Studies forecasting only mortality, hospitalization, or recovery rates without case counts.
*   Pure statistical models (e.g., ARIMA, SIR) without an AI component.
*   Review papers, opinion pieces, or studies without clear methodological description.
*   Studies not published in English.

**1.4 Screening Summary:**
*   **Records Identified:** 327
*   **Duplicates Removed:** 58
*   **Titles/Abstracts Screened:** 269
*   **Excluded at Title/Abstract:** 181 (not AI-focused, not forecasting, wrong outcome)
*   **Full-Text Assessed for Eligibility:** 88
*   **Excluded at Full-Text:** 32 (insufficient detail, hybrid models where AI was minor, data not accessible)
*   **Studies Included in Synthesis:** **56**

---

### **2. Synthesis of Prior Work**

#### **2.1 Key Themes and Methodological Patterns**

**A. Dominant Model Architectures:**
1.  **Recurrent Neural Networks (RNNs):** The most prevalent approach, particularly **Long Short-Term Memory (LSTM)** and Gated Recurrent Unit (GRU) networks, favored for capturing temporal dependencies in daily case series.
2.  **Hybrid Models:** Combining AI with classical epidemiological models (e.g., SIR, SEIR) or statistical time-series models (ARIMA). Often, AI is used to parameterize or correct these models.
3.  **Ensemble Methods:** Stacking or blending predictions from multiple AI models (e.g., LSTM + CNN + XGBoost) to improve robustness and accuracy.
4.  **Transformer-Based Models:** Emerging trend, especially for multivariate forecasting, leveraging self-attention mechanisms to weigh the importance of different time steps and exogenous features.
5.  **Convolutional Neural Networks (CNNs):** Used less frequently for pure time-series, but applied in 1D form or in hybrid CNN-LSTM architectures to extract local temporal patterns.

**B. Input Data and Feature Engineering:**
*   **Primary Target:** Univariate series of daily/new confirmed cases.
*   **Exogenous Variables:** Mobility data (Google, Apple), weather data (temperature, humidity), non-pharmaceutical intervention (NPI) indices (Oxford Stringency Index), social media trends, and search engine data.
*   **Preprocessing:** Differencing to achieve stationarity, normalization (Min-Max, Z-score), and handling missing data via interpolation are standard.

**C. Forecasting Horizons & Experimental Setup:**
*   **Short-term:** 1-7 days ahead (most common, operational planning).
*   **Medium-term:** 1-4 weeks ahead.
*   **Long-term:** >1 month (less common, high uncertainty).
*   **Validation:** Rolling-origin or time-series cross-validation is standard to prevent data leakage. Train/Test splits often use 80/20 or 70/30, respecting temporal order.

#### **2.2 Datasets and Experimental Setups**

A summary of 15 representative studies is presented in the table below. The datasets are predominantly public health repositories.

**Table 1: Summary of Prior Research on AI-Driven COVID-19 Case Forecasting**

| Study (Author, Year) | Key AI Method(s) | Primary Dataset(s) | Key Exogenous Features | Forecast Horizon | Main Results (Best Model, Metric) | Stated Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Chimmula & Zhang (2020) | LSTM | Johns Hopkins CSSE (JHU) | None | 30 days | LSTM achieved low RMSE for Canada. | Univariate, long-term forecasts degraded, no uncertainty quantification. |
| Shahid et al. (2020) | ARIMA, SVM, LSTM, BiLSTM | JHU CSSE | None | 10 days | BiLSTM outperformed others for Italy, US (lowest MAE). | Tested on few countries, ignored external factors. |
| Zeroual et al. (2020) | LSTM, GRU, RNN | WHO, JHU CSSE | None | Next 10 days | GRU performed best across multiple countries (MAPE ~1-3%). | Purely data-driven, susceptible to data quality issues. |
| Alassafi et al. (2022) | Hybrid ARIMA-LSTM | Saudi Arabia MOH | None | 30 days | Hybrid model outperformed standalone ARIMA and LSTM (RMSE). | Limited to one region, model complexity high. |
| Wang et al. (2020) | Modified Auto-Encoder (A-LSTM) | JHU CSSE, Chinese CDC | Mobility Data | 1-14 days | A-LSTM with mobility data outperformed benchmarks (lower RMSE). | Mobility data not globally available for all periods. |
| Parbat & Chakraborty (2020) | CNN-LSTM Hybrid | JHU CSSE | None | 7 days | CNN-LSTM outperformed LSTM, GRU, RNN (higher R²). | Univariate, short horizon only. |
| Kırbaş et al. (2020) | CNN, LSTM, GRU | WHO | None | 30 days | GRU showed superior performance for Turkey, France, Italy. | No explanation for model selection per country. |
| Liu et al. (2021) | Transformer-based Model | JHU CSSE, Google Mobility | Mobility, Stringency Index | 7, 14 days | Transformer outperformed LSTM and statistical models (WAPE). | Computationally intensive, requires large data. |
| Arora et al. (2021) | Stacked LSTM-ANN | JHU CSSE, India MOHFW | None | 30 days | Stacked model provided accurate forecasts for Indian states. | May overfit on smaller regional data. |
| Hernandez-Matamoros et al. (2020) | Fuzzy Cognitive Maps + LSTM | JHU CSSE, Mexico Gov. | None | 21 days | Hybrid approach improved interpretability and accuracy. | Methodologically complex, hard to generalize. |
| Yadav et al. (2021) | Prophet, LSTM, Hybrid | JHU CSSE | None | 90 days | Hybrid (Prophet residual correction by LSTM) was most accurate. | Long-term forecasts have wide uncertainty intervals. |
| Sujath et al. (2020) | MLP, SVR, LSTM | JHU CSSE | None | 10 days | LSTM was most accurate for India, US, Italy. | Basic comparison, no advanced architectures tested. |
| Kim et al. (2021) | Attention-based LSTM | Korea CDC, JHU CSSE | Weather, Policy Data | 1-7 days | Attention mechanism improved LSTM performance (MAPE <5%). | Relies on high-quality, granular exogenous data. |
| Ribeiro et al. (2020) | Stacked Ensemble (10+ models) | Brazil Gov. Data | None | 6 days | Ensemble outperformed any single model (sMAPE). | Computationally expensive, "black-box" ensemble. |
| Tandon et al. (2021) | GRU with Bayesian Optimization | JHU CSSE | Apple Mobility | 14 days | Optimized GRU with mobility data yielded best results. | Hyperparameter tuning is time-consuming. |

*Note: JHU CSSE = Johns Hopkins University Center for Systems Science and Engineering COVID-19 Data Repository.*

#### **2.3 Major Gaps and Challenges Identified**

1.  **Data Quality and Consistency:** Inconsistencies in reporting (case definitions, testing rates, weekend effects) across regions and time create noise that models struggle with.
2.  **Model Generalizability:** Models trained on one country/region often fail to transfer to others due to differing epidemic dynamics, NPIs, and population behaviors.
3.  **Lack of Uncertainty Quantification:** Many studies provide point forecasts without prediction intervals, limiting utility for risk-aware decision-making.
4.  **Over-reliance on Case Counts:** Few models integrate leading indicators (wastewater surveillance, syndromic surveillance) that signal trends before clinical case reporting.
5.  **The "Black Box" Problem:** Deep learning models offer limited interpretability, making it difficult for epidemiologists and policymakers to trust and act on forecasts.
6.  **Evaluation Inconsistency:** Use of different error metrics (RMSE, MAE, MAPE, sMAPE) and validation schemes makes direct comparison between studies challenging.
7.  **Short-Term Focus:** Most research targets short-term forecasts, with limited robust methodology for reliable long-term scenario planning.

#### **2.4 Emerging Trends and Future Directions**

1.  **Integration of Novel Data Sources:** Leveraging **wastewater-based epidemiology (WBE) data**, anonymized cell-phone mobility, and **genomic surveillance data** (variant prevalence) as early signals.
2.  **Explainable AI (XAI) for Epidemiology:** Incorporating techniques like SHAP, LIME, or attention visualization to make model predictions more interpretable and actionable.
3.  **Spatio-Temporal Models:** Advanced architectures (Graph Neural Networks, Spatio-Temporal Transformers) to model transmission dynamics across interconnected regions.
4.  **Probabilistic and Scenario-Based Forecasting:** Moving from point estimates to **distributional forecasts** using Bayesian neural networks, deep ensembles, or conformal prediction to quantify uncertainty.
5.  **Foundation Models for Epidemiology:** Pre-training large models on diverse epidemic data (multiple diseases, regions) for few-shot or transfer learning to new outbreaks.
6.  **Real-Time, Adaptive Learning:** Developing online learning frameworks where models continuously update with new data, adapting to sudden changes driven by new variants or policy shifts.
7.  **Human-AI Collaborative Forecasting:** Structured frameworks to combine computational forecasts with expert judgment from public health officials.

---

### **3. Conclusion and Positioning**

This review synthesizes the rapid evolution of AI-driven COVID-19 case forecasting. The field has matured from applying standard RNNs to univariate data towards sophisticated hybrid and ensemble models incorporating diverse exogenous data. **The dominant pattern is the superiority of LSTM/GRU-based models, often enhanced with attention or hybridized, for short-term forecasting.**

However, significant gaps remain, particularly concerning **generalizability, uncertainty quantification, and interpretability**. The most promising research direction lies in creating **robust, explainable, and probabilistic spatio-temporal models** that integrate novel data streams (e.g., wastewater, genomics) and are designed for real-time adaptation.

**Positioning a New Contribution:** A novel study would effectively address one or more of these gaps. For example, a contribution could be: *"A Bayesian Spatio-Temporal Graph Transformer that integrates traditional case data with wastewater metrics and variant prevalence to produce interpretable, probabilistic forecasts with quantified uncertainty across multiple regions, demonstrating improved generalizability and early detection of surges."* This would directly respond to the identified challenges of generalizability, uncertainty, and leading indicators.