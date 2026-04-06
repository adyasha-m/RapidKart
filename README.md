# RapidKart — Quick Commerce User Behavior & Product Analytics

## Project Overview

RapidKart is an end-to-end **product analytics case study** built for a fictional quick commerce platform. The project analyzes user behavior, conversion funnels, retention, operational efficiency, and user segmentation to understand what drives growth and where users drop off.

The project covers the full pipeline: synthetic data generation, validation, Spark-based transformation, Gold-layer analytics tables, and dashboard-driven insights.

---

## Business Objective

This project answers key product questions:

- How do users move through the purchase funnel?
- Where do users drop off before completing an order?
- Does delivery speed impact conversion and retention?
- How does retention change over time?
- Which user segments contribute most to business value?

---

## Tech Stack

- Python
- Pandas
- PySpark
- Spark SQL
- Power BI

---

## Dataset Design

A **synthetic but realistic dataset** was created to simulate quick-commerce behavior for ~10,000 users across 90 days.

### Tables

#### Users
#### Events
Event types include:
app_open, product_view, add_to_cart, checkout_start, payment_success, order_placed, etc.

#### Orders

### Dataset Realism

The data simulates:
- cart abandonment
- payment failures
- delivery delays
- peak usage hours
- churn behavior
- user segmentation (regular, occasional, inactive)

---

## Architecture

The project follows a **Medallion Architecture**:

Raw Data → Bronze → Silver → Gold → Analysis → Dashboard

### Bronze Layer
Raw data ingestion

### Silver Layer
- cleaned data
- sessionization using window functions
- event enrichment

### Gold Layer
Analytics-ready tables:
- daily_kpis
- funnel_metrics
- retention_cohort
- user_summary

---

## Key Metrics

- Average DAU: 529.52  
- Total Orders: 9,425  
- Total Revenue: 49.59M  
- Conversion Rate: 19.63%  
- Avg Delivery Time: 17.68 minutes  

---

## Key Insights

### 1. Strong Growth with Stable Operations

RapidKart shows consistent growth in users, orders, and revenue. Importantly, delivery time remains stable (~17–18 minutes), indicating operations are scaling effectively alongside demand.

---

### 2. Checkout is the Biggest Funnel Bottleneck

Funnel analysis shows:

- App Open → Product View: 75.41%  
- Product View → Add to Cart: 66.41%  
- Add to Cart → Checkout: 57.20%  
- Checkout → Purchase: 69.78%  

The largest drop occurs at **Add to Cart → Checkout (~42.8% drop-off)**, indicating friction before purchase commitment.

---

### 3. Weak Retention After Early Usage

Retention is strong initially but declines sharply after early weeks. Users try the product but do not consistently return, indicating weak habit formation.

---

### 4. Delivery Time Impacts Conversion

- Correlation between delivery time and conversion: **-0.615**

Faster delivery (~16.7 min) results in higher conversion (~20.36%), while slower delivery (~18.9 min) reduces conversion (~18.98%).

Delivery performance directly impacts business outcomes.

---

### 5. Small User Segment Drives Value

User distribution:
- Occasional Users: 49.5%
- Inactive Users: 41.1%
- Regular Users: 9.36%

Regular users are highly valuable:
- 9.89 avg sessions
- 3.52 avg orders per user

Occasional users generate most orders, making them the biggest growth opportunity.

---

## Dashboard Overview

### Page 1 — Executive Overview
- DAU, Revenue, Orders, Conversion
- Growth trends
<img width="1308" height="736" alt="Screenshot 2026-04-06 233033" src="https://github.com/user-attachments/assets/ac8888fa-0059-4b3f-9bc6-f98689bc5e9f" />


### Page 2 — Funnel Analysis
- Funnel conversion
- Drop-off identification
<img width="1312" height="740" alt="Screenshot 2026-04-06 233054" src="https://github.com/user-attachments/assets/24297082-ad82-4162-a61e-183c74abfe4f" />


### Page 3 — Retention Analysis
- Cohort heatmap
- Retention decay
<img width="1311" height="739" alt="Screenshot 2026-04-06 233115" src="https://github.com/user-attachments/assets/659e060e-bc11-4599-a41f-12008f0ea212" />


### Page 4 — Delivery vs Conversion
- Operational impact on conversion
- Scatter analysis
<img width="1308" height="736" alt="Screenshot 2026-04-06 233128" src="https://github.com/user-attachments/assets/899f52ef-3523-4978-b17d-34b870ef81d0" />


### Page 5 — User Segmentation
- Segment distribution
- Behavior analysis
<img width="1306" height="729" alt="Screenshot 2026-04-06 233141" src="https://github.com/user-attachments/assets/e9618ba7-c99f-4e5d-9a3c-996f89f8eee6" />


---

## Key Business Takeaways

- Improve checkout experience to reduce drop-offs  
- Strengthen early retention (first 2 weeks)  
- Optimize delivery speed to improve conversion  
- Convert occasional users into repeat users  

---

## What This Project Demonstrates
This project demonstrates the ability to:

- design realistic synthetic product telemetry
- validate data quality and behavior
- build Spark-based transformation pipelines
- implement sessionization
- create analytics-ready Gold tables
- analyze funnel, retention, churn, and segmentation
- convert metrics into business decisions
- present insights through dashboards

---

## Final Summary

RapidKart demonstrates strong growth and product adoption, but highlights critical opportunities in checkout optimization, early retention, and delivery performance. Addressing these areas can significantly improve conversion, user experience, and long-term growth.


