# College Program Earnings Regression

## Purpose
The purpose of this project is to analyze the effect of college program choice on four-year post-graduation earnings, controlling for institutional characteristics such as institution type, admission rate, and student demographics. This analysis helps students make informed decisions about program selection.

## Data
- **Source:** Merged dataset of program-level and institution-level college data 
- **Key Variables:**  
  - Program_Name – College program/major
  - Median_Earnings_Year_4 – Median earnings four years after graduation  
  - Admission_Rate – Percentage of students admitted  
  - Institution_Type – Public or private  
  - Percent_Male_Year_4 – Gender composition of graduates  
- **Preprocessing (after initial cleaning using Power Query):**  
  - Verifyed that there were no programs which appeared less than 50 times
  - Filtered out rows with missing admission rates  
  - Added a log transformation of earnings to handle skewed distributions  

## Methods
Two linear regression models were constructed:

1. **Model 1 (Raw Earnings):**  
   - Outcome: Median earnings after four years  
   - Predictors: Program name (Business Administration used as treatment), admission rate, institution type, and percent male  
   - Standard errors clustered by institution to account for within-institution correlation  

2. **Model 2 (Log Earnings):**  
  - Same as Model 1 but with log-transformed earnings to reduce skewness and heteroskedasticity  

**Diagnostics:**  
- Fitted vs. residual plots were examined for both models to check assumptions  
- Log transformation improved residual distribution and stabilized variance  

## Results
- Registered Nursing and Finance were associated with the highest percent increase in earnings over the baseline program (Business Administration)
- Higher admission rates were modestly negatively correlated with earnings  
- Institution type and gender composition had minor effects on earnings  
- Log transformation improved model fit and reduced heteroskedasticity, making inference more reliable  

## Visualizations 
- Residuals vs. Fitted plots for both raw and log earnings models  
- Tableau dashboard with program-level and institution-level earnings: https://public.tableau.com/app/profile/gian.verna5813/viz/CollegeProgramEarnings/Dashboard1

