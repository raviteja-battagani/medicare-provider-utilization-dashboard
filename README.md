# Medicare Provider & Service Utilization Dashboard

Excel dashboard analyzing the CMS **Medicare Physician & Other Practitioners — by Provider and Service** dataset (100,000-row extract). Column names follow the official CMS data dictionary (`MUP_PHY_RY25_20250312_DD_PRV_SVC_508.pdf`).

## How it was built
1. **Raw data** — kept untouched as Excel table `api_100000_rows`; headers renamed to official CMS Term Names.
2. **Pivots sheet** — 7 pivot tables aggregate the raw table (1 for KPIs + 6, one per chart), with Top-10 value filters and descending sorts where relevant.
3. **Dashboard sheet** — KPI row linked to the KPI pivot; 6 charts read directly from pivot outputs; 5 slicers (State, Provider Type, Medicare Participation, Place of Service, Drug Indicator).
4. Slicers connect to the KPI pivot; extend to charts via right-click → Report Connections.

## KPIs
12,308 providers · 27.5M services · 7.3M beneficiaries · $82.62 avg Medicare payment vs $425.82 avg submitted charge.

## Analysis flow — question → finding → decision

| Visual | Business question | Why we asked | Key finding | Decision it supports |
|---|---|---|---|---|
| KPI row | How big is this market? | Scale sets context before drilling down | Medicare pays ~19% of billed charges | Baseline; set pricing/revenue expectations |
| Top 10 Provider Types (bar) | Which specialties drive volume? | Concentration shows where investment pays off | Hematology-Oncology leads (2.46M services) | Prioritize top specialties for staffing, targeting, contracting |
| Top 10 HCPCS (bar) | Which procedures happen most? | Unit-cost changes compound on high-frequency codes | #1: Ground mileage, per statute mile (1.11M services) | Focus rate negotiation, coding audits, utilization review here |
| Avg Payment by State (column) | Where does Medicare pay most? | Geographic spread reveals favorable markets | Highest: AE at $166.07 vs $82.62 overall | Pick expansion/benchmark geographies (beware small-sample territories like AE) |
| Facility vs Non-Facility (column) | Does site of service change payment? | Site of service is a controllable lever | Facility $110.42 vs office $67.27 (~64% higher) | Steer eligible procedures to office settings / weigh facility economics |
| Provider Type Distribution (doughnut) | How concentrated is the provider mix? | Market structure flags workforce risk | 98 distinct provider types | Segment: target top types individually, treat the long tail programmatically |
| Top 10 Providers (bar) | Who are the highest-volume providers? | Outliers = concrete targets | Eye Consultants Of Atlanta Piedmont (1.09M services) | Key-account/partnership shortlist; also compliance review candidates |

## Files
- `Book1.xlsx` — workbook (Read Me, Dashboard, Pivots, raw data)
- `MUP_PHY_RY25_20250312_DD_PRV_SVC_508.pdf` — CMS data dictionary
