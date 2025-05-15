    # Import the required libraries
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
import sys
import os

    # And set the project root path in the system to the project root for importing modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    # Also save the project root path for importing data
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # load the data
file_path = os.path.join(project_root, "data", "marketing_AB.csv")  # Ensure this file is in the same directory
data = pd.read_csv(file_path)

    # A/B Test Analysis: Ad vs PSA Group

    # First group summary
group_conversion = data.groupby('test group')['converted'].agg(['sum', 'count'])
group_conversion['conversion_rate'] = group_conversion['sum'] / group_conversion['count']
print("\nTest groups statistics:")
print("-" * 50)
print(group_conversion)

    # Statistical strength indicators. Z-Test and p-value for Proportions

z_stat, p_val = proportions_ztest(count=group_conversion['sum'], nobs=group_conversion['count'])
print("\nStatistical strength indicators:")
print("-" * 50)
print(f"Z-statistic: {z_stat:.2f}")
print(f"P-value: {p_val:.4f}")

    # And conclusion

print("\nConversion Rates:")
print("-" * 50)
print("Treatment group (ad): ", group_conversion['conversion_rate'].ad)
print("Control group (psa): ", group_conversion['conversion_rate'].psa)

print("\nConclusion:")
print("*" * 50)
if p_val < 0.05:
    print("RELIABLE: The difference in conversion rates for the treatment and control groups \
is statistically significant (p < 0.05).\n")
else:
    print("QUESTIONABLE: The difference in conversion rates for the treatment and control groups is \
not statistically significant (p ≥ 0.05).\n")
