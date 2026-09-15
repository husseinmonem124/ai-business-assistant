"""
AI Business Assistant

A Python-based management decision-support tool that analyzes
revenue, costs, profitability, financial risk, forecasts,
business performance, and management priorities.
"""

print("AI BUSINESS ASSISTANT")

# ==========================================
# CALCULATION FUNCTIONs
# Core business calculations used throughout
# the management analysis.
# ==========================================

def calculate_revenue_change(revenue, previous_revenue):
    revenue_change = revenue - previous_revenue
    revenue_change_percentage = (revenue_change / previous_revenue) * 100
    return revenue_change, revenue_change_percentage

def calculate_forecast(revenue, revenue_change_percentage):
    annual_growth_rate = revenue_change_percentage / 100
    forecast_revenue = revenue * (1 + annual_growth_rate)
    forecast_change = forecast_revenue - revenue
    forecast_growth_percentage = (forecast_change / revenue) * 100
    return forecast_revenue, forecast_change, forecast_growth_percentage

def calculate_total_costs(staff_costs, operations_costs, marketing_costs):
    return staff_costs + operations_costs + marketing_costs

def calculate_profitability(revenue, total_costs):
    profit = revenue - total_costs
    profit_margin = (profit / revenue) * 100
    return profit, profit_margin

def assess_financial_risk(profit_margin, revenue, break_even_revenue):
    if profit_margin >= 20 and revenue >= break_even_revenue * 1.2:
        return "Low"
    elif profit_margin >= 10 and revenue >= break_even_revenue:
        return "Moderate"
    else:
        return "High"

# ==========================================
# INPUT & VALIDATION
# Collect and validate monthly business data.
# ==========================================

print("-" * 30)

print("Hello! I can help you analyze basic business information.")

revenue = float(input("Enter monthly revenue (€): "))

while revenue <= 0:
    print("Revenue must be greater than €0.")
    revenue = float(input("Enter monthly revenue (€): "))

previous_revenue = float(input("Enter previous month's revenue (€): "))

while previous_revenue <= 0:
    print("Previous month's revenue must be greater than €0.")
    previous_revenue = float(input("Enter previous month's revenue (€): "))

# ==========================================
# REVENUE ANALYSIS
# Evaluate month-over-month revenue performance.
# ==========================================

revenue_change, revenue_change_percentage = calculate_revenue_change(
    revenue, previous_revenue
)

data_quality_flag = "Valid"

if abs(revenue_change_percentage) > 50:
    data_quality_flag = "Review"
    data_quality_flag = "Review"

# ==========================================
# FORECAST & SCENARIO ANALYSIS
# Estimate future revenue and evaluate scenarios.
# ==========================================

forecast_revenue, forecast_change, forecast_growth_percentage = calculate_forecast(
    revenue, revenue_change_percentage
)

if abs(revenue_change_percentage) <= 5:
    forecast_confidence = "High"
elif abs(revenue_change_percentage) <= 15:
    forecast_confidence = "Moderate"
else:
    forecast_confidence = "Low"

conservative_revenue = revenue * 1.05
expected_revenue = revenue * 1.10
optimistic_revenue = revenue * 1.20

staff_costs = float(input("Enter monthly staff costs (€): "))

while staff_costs < 0:
    print("Staff costs cannot be negative.")
    staff_costs = float(input("Enter monthly staff costs (€): "))

operations_costs = float(input("Enter monthly operations costs (€): "))

while operations_costs < 0:
    print("Operations costs cannot be negative.")
    operations_costs = float(input("Enter monthly operations costs (€): "))

marketing_costs = float(input("Enter monthly marketing costs (€): "))

while marketing_costs < 0:
    print("Marketing costs cannot be negative.")
    marketing_costs = float(input("Enter monthly marketing costs (€): "))

total_costs = calculate_total_costs(
    staff_costs, operations_costs, marketing_costs
)

# ==========================================
# COST & PROFITABILITY ANALYSIS
# Evaluate costs, profit, margins, and break-even.
# ==========================================

conservative_profit = conservative_revenue - total_costs
expected_profit = expected_revenue - total_costs
optimistic_profit = optimistic_revenue - total_costs

conservative_margin = (conservative_profit / conservative_revenue) * 100
expected_margin = (expected_profit / expected_revenue) * 100
optimistic_margin = (optimistic_profit / optimistic_revenue) * 100

profit, profit_margin = calculate_profitability(revenue, total_costs)

cost_efficiency_ratio = (total_costs / revenue) * 100

break_even_revenue = total_costs
break_even_margin = ((revenue - break_even_revenue) / revenue) * 100

financial_risk = assess_financial_risk(
    profit_margin, revenue, break_even_revenue
)

# ==========================================
# FINANCIAL RISK & BUSINESS SCORE
# Evaluate financial risk and overall performance.
# ==========================================

business_score = 0

if profit_margin >= 30:
    business_score += 40
elif profit_margin >= 20:
    business_score += 30
elif profit_margin >= 10:
    business_score += 20

if revenue_change_percentage > 0:
    business_score += 30

if financial_risk == "Low":
    business_score += 30
elif financial_risk == "Moderate":
    business_score += 20
else:
    business_score += 10

# ==========================================
# BUSINESS ANALYSIS OUTPUT
# Present detailed financial and management insights.
# ==========================================

print("\nREVENUE TREND")
print("-" * 30)
print(f"Previous month: €{previous_revenue:,.2f}")
print(f"Current month: €{revenue:,.2f}")

if revenue_change > 0:
    print(f"Revenue growth: +{revenue_change_percentage:.2f}%")
elif revenue_change < 0:
    print(f"Revenue decline: {revenue_change_percentage:.2f}%")
else:
    print("Revenue change: 0.00%")

print("\nANNUALIZED REVENUE FORECAST")
print("-" * 30)
print(f"Current monthly revenue: €{revenue:,.2f}")
print(f"Annualized growth assumption: {revenue_change_percentage:.2f}%")
print(f"Annualized revenue forecast: €{forecast_revenue:,.2f}")
print(f"Projected revenue change: €{forecast_change:+,.2f}")
print(f"Projected revenue growth: {forecast_growth_percentage:+.2f}%")
print(f"Forecast confidence: {forecast_confidence}")
print("Forecast uses the latest month-over-month growth rate as an annualized estimate.")

if forecast_revenue > revenue:
    print("Forecast outlook: Revenue is expected to increase if current growth continues.")
elif forecast_revenue < revenue:
    print("Forecast outlook: Revenue is expected to decrease if current trend continues.")
else:
    print("Forecast outlook: Revenue is expected to remain stable.")

if forecast_growth_percentage < 0:
    print("Forecast risk: Negative revenue growth requires management attention.")
elif forecast_growth_percentage >= 20:
    print("Forecast risk: Growth assumptions should be monitored to ensure they remain realistic.")
else:
    print("Forecast risk: Forecast appears relatively moderate based on the current trend.")

print("\nFORECAST MANAGEMENT RECOMMENDATION")
print("-" * 30)

if forecast_growth_percentage < 0:
    print("Recommendation: Review the causes of declining revenue and develop a recovery plan.")
elif forecast_growth_percentage >= 20:
    print("Recommendation: Validate growth assumptions before making major expansion decisions.")
else:
    print("Recommendation: Continue monitoring revenue performance and support sustainable growth.")

print("\nREVENUE SCENARIO ANALYSIS")
print("-" * 30)

print(f"Conservative scenario (+5%): €{conservative_revenue:,.2f}")
print(f"Expected scenario (+10%): €{expected_revenue:,.2f}")
print(f"Optimistic scenario (+20%): €{optimistic_revenue:,.2f}")

print("\nPROJECTED MONTHLY PROFIT")
print("-" * 30)

print(f"Conservative profit: €{conservative_profit:,.2f}")
print(f"Expected profit: €{expected_profit:,.2f}")
print(f"Optimistic profit: €{optimistic_profit:,.2f}")

print("\nSCENARIO PROFIT MARGINS")
print("-" * 30)

print(f"Conservative margin: {conservative_margin:.2f}%")
print(f"Expected margin: {expected_margin:.2f}%")
print(f"Optimistic margin: {optimistic_margin:.2f}%")

print("\nBREAK-EVEN ANALYSIS")
print("-" * 30)
print(f"Monthly costs to cover: €{total_costs:,.2f}")
print(f"Simplified break-even revenue proxy: €{break_even_revenue:,.2f}")
print(f"Revenue buffer above cost proxy: {break_even_margin:.2f}%")

if revenue > break_even_revenue:
    print("Status: Above break-even")
elif revenue < break_even_revenue:
    print("Status: Below break-even")
else:
    print("Status: At break-even")

if revenue > break_even_revenue:
    print("Break-even assessment: Current revenue provides a positive operating buffer.")
elif revenue < break_even_revenue:
    print("Break-even assessment: Current revenue is insufficient to cover monthly costs.")
else:
    print("Break-even assessment: Current revenue exactly covers monthly costs.")

print("\nBREAK-EVEN RECOMMENDATION")
print("-" * 30)

if revenue > break_even_revenue:
    print("Recommendation: Maintain the current revenue buffer while monitoring cost growth.")
elif revenue < break_even_revenue:
    print("Recommendation: Increase revenue or reduce costs to reach break-even.")
else:
    print("Recommendation: Improve the revenue buffer to reduce financial risk.")

print("\nFINANCIAL RISK ASSESSMENT")
print("-" * 30)
print(f"Financial risk level: {financial_risk}")

if financial_risk == "Low":
    print("The business has a healthy financial position.")
elif financial_risk == "Moderate":
    print("The business should monitor costs and profitability closely.")
else:
    print("The business should prioritize cost control and profitability improvement.")

print("\nCOST EFFICIENCY KPI")
print("-" * 30)
print(f"Cost-to-revenue ratio: {cost_efficiency_ratio:.2f}%")
print(
    f"The business spends €{cost_efficiency_ratio / 100:.2f} "
    "for every €1 of revenue."
)

print("\nBUSINESS ANALYSIS")
print("-" * 30)
print(f"Revenue: €{revenue:,.2f}")
print(f"Total costs: €{total_costs:,.2f}")
print(f"Profit: €{profit:,.2f}")
print(f"Profit margin: {profit_margin:.2f}%")

print("\nEXPENSE ANALYSIS")
print("-" * 30)

expenses = {
    "Staff": staff_costs,
    "Operations": operations_costs,
    "Marketing": marketing_costs,
}

largest_expense = max(expenses, key=expenses.get)
second_largest_expense = sorted(expenses, key=expenses.get, reverse=True)[1]
top_two_cost_share = (
    (expenses[largest_expense] + expenses[second_largest_expense])
    / total_costs
) * 100

print(f"Largest expense category: {largest_expense}")
print(f"Amount: €{expenses[largest_expense]:,.2f}")
print(f"Second-largest expense category: {second_largest_expense}")
print(f"Amount: €{expenses[second_largest_expense]:,.2f}")
print(f"Top two cost categories: {top_two_cost_share:.1f}% of total costs")

if top_two_cost_share >= 80:
    print("Cost concentration: High.")
elif top_two_cost_share >= 60:
    print("Cost concentration: Moderate.")
else:
    print("Cost concentration: Low.")

if top_two_cost_share >= 80:
    print("Recommendation: Management should prioritize the two largest cost categories for efficiency improvements.")
elif top_two_cost_share >= 60:
    print("Recommendation: Management should monitor the two largest cost categories closely.")
else:
    print("Recommendation: Costs are relatively diversified across the main categories.")

print("\nCOST BREAKDOWN")
print("-" * 30)

for category, amount in expenses.items():
    percentage = (amount / total_costs) * 100
    print(f"{category}: {percentage:.1f}% of total costs")

print("\nKEY BUSINESS INSIGHT")
print("-" * 30)

largest_percentage = (expenses[largest_expense] / total_costs) * 100

print(
    f"{largest_expense} represents {largest_percentage:.1f}% "
    "of total operating costs."
)

if largest_percentage >= 50:
    print(
        f"Management should prioritize reviewing {largest_expense.lower()} "
        "costs because they represent a major share of total expenses."
    )
elif largest_percentage >= 35:
    print(
        f"{largest_expense} is the largest cost driver. "
        f"Management should investigate opportunities to improve efficiency "
        f"in {largest_expense.lower()}."
    )
else:
    print(
        "Costs are relatively distributed across the main expense categories. "
        "Management should review all categories for optimization opportunities."
    )

print("\nPERFORMANCE RATING")
print("-" * 30)

if profit_margin >= 30:
    rating = "Excellent"
elif profit_margin >= 20:
    rating = "Good"
elif profit_margin >= 10:
    rating = "Moderate"
else:
    rating = "Needs Improvement"

if profit_margin >= 30 and revenue_change_percentage > 0:
    business_recommendation = "Focus on sustainable growth and protect profitability."
elif profit_margin >= 15:
    business_recommendation = "Improve cost efficiency while maintaining revenue growth."
else:
    business_recommendation = "Prioritize profitability improvement and cost control."

print(f"Business performance: {rating}")

print("\nBUSINESS RECOMMENDATION")
print("-" * 30)
print(business_recommendation)

print("\nMANAGEMENT DECISION")
print("-" * 30)

if financial_risk == "Low" and revenue_change_percentage > 0:
    print("Management priority: Maintain growth while monitoring major cost drivers.")
elif financial_risk == "Moderate":
    print("Management priority: Improve cost efficiency and closely monitor profitability.")
else:
    print("Management priority: Prioritize cost reduction and profitability improvement.")

print("\nBUSINESS HEALTH SCORE")
print("-" * 30)
print(f"Overall business score: {business_score}/100")

if business_score >= 80:
    print("Overall assessment: Strong business position.")
elif business_score >= 60:
    print("Overall assessment: Stable business position.")
else:
    print("Overall assessment: Business requires attention.")

# ==========================================
# MANAGEMENT REPORTING
# Summarize KPIs, risks, and management actions.
# ==========================================

print("\nEXECUTIVE SUMMARY")
print("-" * 30)

print(f"Revenue: €{revenue:,.2f}")
print(f"Profit: €{profit:,.2f}")
print(f"Profit margin: {profit_margin:.2f}%")
print(f"Revenue growth: {revenue_change_percentage:+.2f}%")
print(f"Financial risk: {financial_risk}")
print(f"Data quality status: {data_quality_flag}")
if data_quality_flag == "Review":
    print("Data quality note: The revenue change is unusually large and should be validated before making decisions.")
else:
    print("Data quality note: Revenue inputs passed the basic validation check.")
print(f"Top-two cost concentration: {top_two_cost_share:.1f}%")
print(f"Business health score: {business_score}/100")
print(f"Primary recommendation: {business_recommendation}")

if business_score >= 80:
    print("Conclusion: The business is performing strongly and is positioned for continued growth.")
elif business_score >= 60:
    print("Conclusion: The business is stable but has opportunities to improve performance.")
else:
    print("Conclusion: The business requires attention to improve financial performance.")

print("\nMANAGEMENT KPI DASHBOARD")
print("-" * 30)
print(f"Revenue: €{revenue:,.2f}")
print(f"Profit: €{profit:,.2f}")
print(f"Profit margin: {profit_margin:.2f}%")
print(f"Revenue growth: {revenue_change_percentage:+.2f}%")
print(f"Cost-to-revenue ratio: {cost_efficiency_ratio:.2f}%")
print(f"Top-two cost concentration: {top_two_cost_share:.1f}%")
print(f"Financial risk: {financial_risk}")
print(f"Data quality: {data_quality_flag}")

if data_quality_flag == "Review":
    print("Data quality action: Validate revenue figures before making management decisions.")
else:
    print("Data quality action: No additional revenue validation required.")

if profit_margin >= 30:
    print("KPI assessment: Strong profitability.")
elif profit_margin >= 15:
    print("KPI assessment: Acceptable profitability.")
else:
    print("KPI assessment: Profitability requires attention.")

print("\nGROWTH ASSESSMENT")
print("-" * 30)

if revenue_change_percentage >= 10:
    print("Growth status: Strong growth.")
elif revenue_change_percentage > 0:
    print("Growth status: Positive but moderate growth.")
elif revenue_change_percentage == 0:
    print("Growth status: No revenue growth.")
else:
    print("Growth status: Revenue decline requires attention.")

print("\nMANAGEMENT INSIGHT")
print("-" * 30)

if revenue_change_percentage >= 10 and profit_margin >= 30:
    print("The business shows strong growth and strong profitability.")
elif revenue_change_percentage > 0 and profit_margin >= 15:
    print("The business is growing while maintaining acceptable profitability.")
elif revenue_change_percentage > 0:
    print("Revenue is growing, but profitability should be monitored.")
else:
    print("Management should prioritize improving revenue performance and profitability.")

print("\nCOST RISK ASSESSMENT")
print("-" * 30)

if cost_efficiency_ratio >= 80:
    print("Cost risk: High.")
elif cost_efficiency_ratio >= 65:
    print("Cost risk: Moderate.")
else:
    print("Cost risk: Low.")

if cost_efficiency_ratio >= 80:
    print("Recommendation: Immediate cost reduction is required.")
elif cost_efficiency_ratio >= 65:
    print("Recommendation: Management should review major cost drivers.")
else:
    print("Recommendation: Maintain cost discipline while supporting growth.")

print("\nREVENUE STABILITY ASSESSMENT")
print("-" * 30)

if revenue_change_percentage >= 10:
    print("Revenue stability: Strong positive momentum.")
elif revenue_change_percentage > 0:
    print("Revenue stability: Positive but moderate momentum.")
elif revenue_change_percentage == 0:
    print("Revenue stability: Stable with no growth.")
else:
    print("Revenue stability: Declining revenue requires attention.")

if revenue_change_percentage >= 10:
    print("Recommendation: Continue investing in sustainable revenue growth.")
elif revenue_change_percentage > 0:
    print("Recommendation: Strengthen the factors contributing to revenue growth.")
elif revenue_change_percentage == 0:
    print("Recommendation: Identify opportunities to increase revenue.")
else:
    print("Recommendation: Investigate the causes of revenue decline.")

print("\nPROFITABILITY ASSESSMENT")
print("-" * 30)

if profit_margin >= 30:
    print("Profitability status: Strong.")
elif profit_margin >= 15:
    print("Profitability status: Acceptable.")
else:
    print("Profitability status: Needs improvement.")

if profit_margin >= 30:
    print("Recommendation: Protect margins while pursuing sustainable growth.")
elif profit_margin >= 15:
    print("Recommendation: Identify opportunities to improve profitability.")
else:
    print("Recommendation: Prioritize margin improvement and cost control.")

print("\nOVERALL MANAGEMENT ASSESSMENT")
print("-" * 30)

if (
    revenue_change_percentage >= 10
    and profit_margin >= 30
    and cost_efficiency_ratio < 65
):
    print("Overall status: Strong business performance.")
elif (
    revenue_change_percentage > 0
    and profit_margin >= 15
    and cost_efficiency_ratio < 80
):
    print("Overall status: Stable business performance.")
else:
    print("Overall status: Business performance requires attention.")

if (
    revenue_change_percentage >= 10
    and profit_margin >= 30
    and cost_efficiency_ratio < 65
):
    print("Management recommendation: Sustain growth and protect profitability.")
elif (
    revenue_change_percentage > 0
    and profit_margin >= 15
    and cost_efficiency_ratio < 80
):
    print("Management recommendation: Maintain growth while improving efficiency.")
else:
    print("Management recommendation: Prioritize performance improvement.")

print("\nMANAGEMENT PRIORITY AREA")
print("-" * 30)

if largest_percentage >= 50:
    print(f"Priority area: {largest_expense} cost control.")
elif profit_margin < 15:
    print("Priority area: Profitability improvement.")
elif revenue_change_percentage < 0:
    print("Priority area: Revenue recovery.")
else:
    print("Priority area: Sustainable growth.")

if largest_percentage >= 50:
    print("Priority action: Review staffing levels and improve workforce efficiency.")
elif profit_margin < 15:
    print("Priority action: Reduce costs and identify opportunities to improve margins.")
elif revenue_change_percentage < 0:
    print("Priority action: Investigate the causes of revenue decline and strengthen sales performance.")
else:
    print("Priority action: Invest selectively in revenue growth while maintaining financial discipline.")

print("\nACTION PRIORITY LEVEL")
print("-" * 30)

if largest_percentage >= 50 or profit_margin < 15 or revenue_change_percentage < 0:
    print("Priority level: High.")
elif profit_margin < 25 or cost_efficiency_ratio >= 65:
    print("Priority level: Medium.")
else:
    print("Priority level: Low.")

if largest_percentage >= 50:
    print("Reason: A major expense category requires immediate management attention.")
elif profit_margin < 15:
    print("Reason: Low profitability creates a significant financial concern.")
elif revenue_change_percentage < 0:
    print("Reason: Declining revenue requires immediate investigation.")
elif profit_margin < 25:
    print("Reason: Profitability is acceptable but could be strengthened.")
elif cost_efficiency_ratio >= 65:
    print("Reason: Operating costs represent a relatively high share of revenue.")
else:
    print("Reason: Current financial indicators are performing well.")

print("\nBUSINESS ANALYSIS REPORT")
print("=" * 40)
print("AI Business Assistant")
print("Management Decision Support Report")
print("=" * 40)
print("Report type: Financial and operational business analysis")
print("Analysis scope: Monthly business performance")
print("Decision support level: Management")

print("\nDECISION SUMMARY")
print("-" * 30)
print(f"Overall status: {business_score}/100")
print(f"Priority level: {financial_risk}")
print(f"Primary focus: {largest_expense}")
if business_score >= 80 and revenue_change_percentage > 0:
    print("Management decision: Continue growth while protecting profitability.")
elif business_score >= 60:
    print("Management decision: Maintain stability and improve operational efficiency.")
else:
    print("Management decision: Prioritize corrective action and financial improvement.")

print("\nBUSINESS ACTION PLAN")
print("-" * 30)

if revenue_change_percentage >= 10:
    print("Action 1: Continue sustainable revenue growth initiatives.")
else:
    print("Action 1: Develop initiatives to improve revenue performance.")

if profit_margin >= 30:
    print("Action 2: Protect current profit margins.")
else:
    print("Action 2: Implement measures to improve profitability.")

if cost_efficiency_ratio >= 65:
    print("Action 3: Review major operating costs.")
else:
    print("Action 3: Maintain cost discipline while supporting growth.")

print("\nACTION PRIORITY")
print("-" * 30)

if profit_margin < 15 or revenue_change_percentage < 0:
    print("High priority: Financial performance improvement.")
elif cost_efficiency_ratio >= 65:
    print("Medium priority: Cost efficiency improvement.")
else:
    print("Low priority: Maintain current performance.")

print("\nBUSINESS HEALTH INDICATOR")
print("-" * 30)

if business_score >= 80:
    print("Health indicator: 🟢 Strong")
elif business_score >= 60:
    print("Health indicator: 🟡 Stable")
else:
    print("Health indicator: 🔴 Needs attention")

print("\nHEALTH INDICATOR EXPLANATION")
print("-" * 30)

if business_score >= 80:
    print("The business is performing strongly across the main financial indicators.")
elif business_score >= 60:
    print("The business is relatively stable but has areas that could be improved.")
else:
    print("The business requires attention to improve its financial performance.")

print("\nSTRATEGIC FOCUS")
print("-" * 30)

if business_score >= 80 and revenue_change_percentage > 0:
    print("Strategic focus: Scale growth while maintaining financial discipline.")
elif business_score >= 60:
    print("Strategic focus: Strengthen efficiency and improve business performance.")
else:
    print("Strategic focus: Stabilize financial performance before pursuing growth.")

print("\nKEY KPI TO MONITOR")
print("-" * 30)

if profit_margin < 15:
    print("Monitor: Profit margin.")
elif revenue_change_percentage < 0:
    print("Monitor: Revenue growth.")
elif cost_efficiency_ratio >= 65:
    print("Monitor: Cost-to-revenue ratio.")
else:
    print("Monitor: Revenue growth and profit margin.")

if profit_margin < 15:
    print("Reason: Profitability is currently below the desired level.")
elif revenue_change_percentage < 0:
    print("Reason: Revenue is declining and requires close monitoring.")
elif cost_efficiency_ratio >= 65:
    print("Reason: Costs represent a relatively high share of revenue.")
else:
    print("Reason: Revenue growth and profitability are key indicators of continued business performance.")

print("\nMANAGEMENT RISK FLAG")
print("-" * 30)

if financial_risk == "High":
    print("Risk flag: 🔴 Immediate management attention required.")
elif financial_risk == "Moderate":
    print("Risk flag: 🟡 Management monitoring required.")
else:
    print("Risk flag: 🟢 No immediate financial risk detected.")

if financial_risk == "High":
    print("Risk reason: Profitability or financial stability is below the acceptable level.")
elif financial_risk == "Moderate":
    print("Risk reason: The business is stable but should be monitored closely.")
else:
    print("Risk reason: Current profitability, revenue performance, and financial stability are healthy.")