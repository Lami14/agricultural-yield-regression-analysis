# Agricultural Yield Regression Analysis

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/github/workflow/status/Lami14/agricultural-yield-regression-analysis/Python%20application)](https://github.com/Lami14/agricultural-yield-regression-analysis/actions)

## Overview

This project predicts **standardized agricultural yield** using regression and machine learning techniques.  
It helps farmers understand the impact of soil, geography, and farm management on crop yield.  

**Key features:**
- Multiple Linear Regression
- LASSO & Ridge Regression for feature selection & multicollinearity
- Decision Tree Regression
- Feature engineering and scaling
- Model evaluation with RMSE, MSE, and visual diagnostics

---

## Dataset

The dataset contains:

| Feature Group | Examples |
|---------------|---------|
| Geographic    | Elevation, Latitude, Longitude, Slope, Location |
| Soil & Crop   | Soil_type, Soil_fertility, pH, Chosen_crop |
| Weather       | Rainfall, Ave_temps, Min/Max Temperature (dummy) |
| Farm Management | Pollution_level, Plot_size, Annual_yield (not used) |
| Target        | Standard_yield |

> **Target variable:** Standard_yield (normalized per crop)

---

## Folder Structure- Ridge Regression
- Decision Tree Modelling

Model Evaluation

The models were evaluated using:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Residual Analysis

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Statsmodels
- Seaborn
- Matplotlib

Author

Lamla Mhlana
