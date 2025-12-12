# College Program Earnings Regression

## Purpose
The purpose of this project is to analyze the effect of college program choice on four-year post-graduation earnings, controlling for institutional characteristics such as institution type, admission rate, and student demographics. This analysis helps students, educators, and policymakers understand which programs are associated with higher earnings and informs decisions about program selection and institutional planning.

## Data
- **Source:** Merged dataset of program-level and institution-level college data (include source or link if public)  
- **Key Variables:**  
  - `Program_Name` – College program  
  - `Median_Earnings_Year_4` – Median earnings four years after graduation  
  - `Admission_Rate` – Percentage of students admitted  
  - `Institution_Type` – Public or private  
  - `Percent_Male_Year_4` – Gender composition of graduates  
- **Preprocessing:**  
  - Removed programs with fewer than 50 occurrences  
  - Filtered out rows with missing admission rates  
  - Added a log transformation of earnings (`log_earnings`) to handle skewed distributions  

## Methods
Two linear regression models were constructed:

1. **Model 1 (Raw Earnings):**  
   - Outcome: Median earnings after four years  
   - Predictors: Program name (categorical with treatment coding), admission rate, institution type, and percent male  
   - Standard errors clustered by institution (`OPEID6`) to account for within-institution correlation  

2. **Model 2 (Log Earnings):**  
   - Outcome: Log-transformed earnings to reduce skewness and heteroskedasticity  
   - Same predictors as Model 1  
   - Cluster-robust standard errors used for inference  

**Diagnostics:**  
- Fitted vs. residual plots were examined for both models to check assumptions  
- Log transformation improved residual distribution and stabilized variance  

## Results
- Programs in **STEM and Business fields** were associated with significantly higher earnings compared to the baseline program (`Business Administration, Management and Operations`)  
- Higher admission rates were modestly negatively correlated with earnings  
- Institution type and gender composition had minor effects on earnings  
- Log transformation improved model fit and reduced heteroskedasticity, making inference more reliable  

## Visualizations
- Residuals vs. Fitted plots for both raw and log earnings models  
- Tableau dashboard with program-level and institution-level earnings: [Insert Tableau Dashboard Link Here]  


