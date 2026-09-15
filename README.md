# AI Business Assistant

A Python-based management decision-support tool for analyzing business performance, financial health, revenue trends, profitability, costs, business risk, and management priorities.

## Overview

AI Business Assistant is a portfolio project designed to demonstrate how Python can be used to support structured business analysis and management decision-making.

The application collects basic monthly financial information and transforms it into a structured management report containing financial KPIs, revenue analysis, forecasting, scenario analysis, cost analysis, risk assessment, business scoring, and recommended management actions.

The project focuses on the intersection of **business analysis, data-driven decision support, and Python automation**.

## Business Problem

Managers often need to turn basic financial information into actionable business insights.

Simply knowing revenue and expenses is not enough. Management may also need to understand:

* Is revenue growing or declining?
* Is the business profitable?
* How efficient are operating costs?
* Which expense categories require attention?
* Is the business above its simplified break-even cost level?
* What is the current financial risk level?
* What revenue scenarios could management consider?
* Which KPI should management monitor?
* What should management prioritize next?

AI Business Assistant addresses these questions by converting a small set of financial inputs into a structured decision-support report.

## Key Features

### Revenue Analysis

* Compares current revenue with the previous month
* Calculates revenue change
* Calculates month-over-month revenue growth
* Identifies positive or negative revenue momentum
* Performs a basic data-quality check for unusually large revenue changes

### Annualized Revenue Forecast

* Uses the latest month-over-month growth rate as an annualized growth assumption
* Calculates an annualized revenue estimate
* Reports projected revenue change
* Provides a forecast confidence level
* Identifies potential forecast risks
* Generates a management recommendation based on the forecast

### Revenue Scenario Analysis

The application evaluates three simple revenue scenarios:

* **Conservative:** +5%
* **Expected:** +10%
* **Optimistic:** +20%

Each scenario includes projected revenue, profit, and profit margin.

### Cost & Profitability Analysis

* Calculates total operating costs
* Calculates profit
* Calculates profit margin
* Calculates cost-to-revenue ratio
* Identifies the largest expense category
* Identifies the second-largest expense category
* Calculates top-two cost concentration
* Provides cost-management recommendations

### Simplified Break-Even Analysis

The application provides a simplified break-even revenue proxy based on total monthly costs.

This is intentionally presented as a **simplified proxy**, rather than a full accounting break-even calculation, because the application does not currently separate fixed costs, variable costs, and contribution margin.

### Financial Risk Assessment

The application evaluates financial risk using:

* Profit margin
* Current revenue
* Simplified break-even revenue proxy

The resulting risk classification is:

* **Low**
* **Moderate**
* **High**

### Business Health Score

The application calculates an overall business health score out of 100 based on:

* Profitability
* Revenue growth
* Financial risk

The result is translated into a management-oriented assessment.

### Management Reporting

The final report provides:

* Executive summary
* KPI dashboard
* Growth assessment
* Management insight
* Cost risk assessment
* Revenue stability assessment
* Profitability assessment
* Overall management assessment
* Management priority area
* Action priority level
* Business action plan
* Strategic focus
* Key KPI to monitor
* Management risk flag
* Business health indicator

## Example Analysis

Example input:

| Metric                   |   Value |
| ------------------------ | ------: |
| Current monthly revenue  | €50,000 |
| Previous monthly revenue | €45,000 |
| Staff costs              | €15,000 |
| Operations costs         | €12,000 |
| Marketing costs          |  €5,000 |

Example results:

| KPI                         |     Result |
| --------------------------- | ---------: |
| Revenue growth              |    +11.11% |
| Annualized revenue forecast | €55,555.56 |
| Total costs                 |    €32,000 |
| Profit                      |    €18,000 |
| Profit margin               |     36.00% |
| Cost-to-revenue ratio       |     64.00% |
| Financial risk              |        Low |
| Business health score       |    100/100 |
| Data quality                |      Valid |

### Management Interpretation

The example indicates strong revenue momentum and profitability. Staff is the largest individual expense category, while Staff and Operations together represent a high concentration of total operating costs.

The resulting management focus is therefore to **sustain revenue growth while protecting profitability and monitoring major cost drivers**.

## Decision-Support Logic

The application follows a structured analytical workflow:

```text
Financial Inputs
      ↓
Input Validation
      ↓
Revenue Analysis
      ↓
Annualized Forecast
      ↓
Revenue Scenarios
      ↓
Cost Analysis
      ↓
Profitability Analysis
      ↓
Break-Even Proxy
      ↓
Financial Risk
      ↓
Business Health Score
      ↓
Management KPIs
      ↓
Recommendations & Action Plan
```

## Technology

* **Python**
* Python functions
* Conditional logic
* Dictionaries
* Lists and sorting
* User input and validation
* Financial calculations
* Basic business analytics
* Automated management reporting

## Project Structure

```text
ai-business-assistant/
│
├── business_assistant.py
└── README.md
```

## Skills Demonstrated

This project demonstrates practical skills relevant to Business Analyst, Business IT, and process-oriented roles:

### Business Analysis

* KPI analysis
* Financial performance analysis
* Cost analysis
* Profitability analysis
* Risk assessment
* Scenario analysis
* Management recommendations
* Decision-support reporting

### Data & Analytical Thinking

* Input validation
* Quantitative analysis
* Trend analysis
* Forecasting assumptions
* Threshold-based classification
* Business scoring
* Structured interpretation of financial indicators

### Python

* Functions
* Variables and calculations
* Conditional statements
* Dictionaries
* Sorting
* Input validation
* Formatted output
* Modular calculation logic

## Design Approach

The project intentionally uses a straightforward procedural structure.

The objective is not to demonstrate complex software architecture, but to demonstrate how a business problem can be translated into:

**Inputs → Calculations → KPIs → Insights → Management Actions**

This keeps the application easy to understand while maintaining a clear separation between core calculations and business reporting.

## Limitations

This project is a simplified management decision-support prototype and does not replace professional financial or accounting software.

Current limitations include:

* Forecasting is based on a single observed month-over-month growth rate
* Revenue forecasting should be treated as an estimate rather than a guaranteed prediction
* Break-even analysis uses a simplified total-cost proxy
* The financial risk model uses predefined thresholds
* Scenario assumptions are simplified
* The application currently focuses on monthly financial information
* The project does not use a database or external business data source

These limitations are intentionally documented to make the analytical assumptions transparent.

## Future Improvements

Potential future development could include:

* Historical monthly data input
* CSV data import
* Automated trend analysis across multiple months
* More advanced forecasting models
* Separate fixed and variable cost inputs
* Full contribution-margin break-even analysis
* Interactive dashboards
* Data visualization
* Database integration
* Automated PDF management reports
* AI-assisted natural-language business recommendations
* Sensitivity analysis
* KPI trend monitoring

## Portfolio Context

AI Business Assistant is part of a broader Business Analyst / Business IT portfolio demonstrating the use of technology to solve business and operational problems.

The project complements other portfolio work focused on:

* Business management
* Business intelligence
* Process optimization
* Data analysis
* Management decision support

## Author

**Hussein Monem**
