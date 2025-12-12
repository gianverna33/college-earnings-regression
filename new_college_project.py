import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


merged_data = pd.read_csv(
    "C:/Users/gvlam/OneDrive/Documents/Python/merged_college_data.csv")

# take away the spaces in the column names
merged_data.columns = (
    merged_data.columns
    .str.replace(' ', '_')
)

pd.set_option("display.max_rows", None)

# remove this program that was included by mistake
merged_data = merged_data[merged_data['Program_Name']
                          != "Multi-/Interdisciplinary Studies, General."]

# filter out rows with missing admission rates
merged_data = merged_data[merged_data['Admission_Rate'].notna()]

# make sure that each program has a minimum of 50 occurences
print(merged_data['Program_Name'].value_counts(ascending=False))


# add a log of earnings
merged_data['log_earnings'] = np.log(merged_data['Median_Earnings_Year_4'])


# model 1, without log earnings
college_model1 = smf.ols(
    'Median_Earnings_Year_4~  C(Program_Name, Treatment(reference="Business Administration, Management and Operations."))'
    ' + Admission_Rate + C(Institution_Type) + Percent_Male_Year_4', data=merged_data).fit(
        cov_type='cluster',
        cov_kwds={'groups': merged_data['OPEID6']})

# model2, with log earnings
college_model2 = smf.ols(
    'log_earnings~  C(Program_Name, Treatment(reference="Business Administration, Management and Operations."))'
    ' + Admission_Rate + Institution_Type + Percent_Male_Year_4', data=merged_data).fit(
        cov_type='cluster',
        cov_kwds={'groups': merged_data['OPEID6']})


print(college_model1.summary())
print(college_model2.summary())


residuals1 = college_model1.resid
fitted_vals1 = college_model1.fittedvalues

# fitted vs residuals
sns.scatterplot(x=fitted_vals1, y=residuals1)
plt.title("Fitted vs. Residuals")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.show()


residuals2 = college_model2.resid
fitted_vals2 = college_model2.fittedvalues

# fitted vs residuals using log of earnings
sns.scatterplot(x=fitted_vals2, y=residuals2)
plt.title("Fitted vs. Residuals (Using Log of Earnings)")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.show()
