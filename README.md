<h1 align="center">🏠 Chennai-Housing-Price-Prediction</h1>
<p align="center"> <img src="https://img.shields.io/badge/Language-Python-blue?logo=python" alt="Python Badge" /> <img src="https://img.shields.io/badge/Frameworks-Scikit--learn%20%7C%20XGBoost%20%7C%20Pandas-green" alt="Frameworks Badge" /> <img src="https://img.shields.io/badge/Visualization-Seaborn%20%7C%20Matplotlib-orange" alt="Visualization Badge" /> </p>

<p align="center" style="font-size:16px; color:#475569;"> This project builds a <strong>data-driven ensemble regression model</strong> to predict <strong>Chennai housing prices</strong> across the INR 20 lakh–3 crore range using <strong>XGBoost</strong>. It demonstrates end-to-end <strong>data preprocessing, model benchmarking, performance evaluation,</strong> and <strong>insight generation</strong> for real-estate analytics. </p>
<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">
<h2>📘 Project Overview</h2>
<ul style="line-height:1.8;">
    <li><strong>Goal:</strong> Predict residential property prices in Chennai using historical market data and identify key drivers of valuation.</li>
    <li><strong>Approach:</strong> Performed <em>EDA</em>, engineered custom preprocessing pipeline, and benchmarked multiple regression models to deploy the most accurate ensemble learner.</li>
    <li><strong>Tech Stack:</strong> Python, Pandas, NumPy, Scikit-learn, XGBoost, Seaborn, Matplotlib, SQL</li>
</ul>
<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">
<h2>⚙️ Workflow</h2>
<ol style="line-height:1.8;">
    <li><strong>Data Preprocessing:</strong> Handled missing values, outliers, and skewed distributions using data smoothing and transformations.</li>
    <li><strong>Exploratory Data Analysis:</strong> Used Python (Seaborn, Matplotlib) and SQL to uncover relationships between property features and price.</li>
    <li><strong>Model Benchmarking:</strong> Compared Linear Regression, Random Forest, AdaBoost, and XGBoost to select the best model for production.</li>
    <li><strong>Model Optimization:</strong> Tuned hyperparameters and engineered feature transformations to enhance predictive accuracy.</li>
    <li><strong>Evaluation:</strong> Assessed performance using R², MAPE, and segment-wise price error analysis.</li>
</ol>
<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">
<h2>📈 Key Results</h2>
<ul style="line-height:1.8;">
    <li>Achieved <strong>R² = 0.954</strong> and <strong>7.21% MAPE</strong> with the final XGBoost model.</li>
    <li>Improved baseline model performance by <strong>6%</strong> through advanced preprocessing and feature engineering.</li>
    <li>Model performs best for <strong>mid-to-high range properties (INR 50L–2Cr)</strong> with 1–7L average error.</li>
    <li>Identified systematic underestimation in <strong>budget segment (<INR 50L)</strong>, guiding future feature enhancement.</li>
</ul>
<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">
<h2>📊 Sample Visualizations</h2>
<p align="center"> <img width="1200" height="500" alt="EDA Visualization 1" src="https://github.com/user-attachments/assets/example-eda1.png" /> </p> <br>
<p align="center"> <img width="1200" height="500" alt="Model Performance Visualization" src="https://github.com/user-attachments/assets/example-eda2.png" /> </p>
<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">
<h2>📂 Repository Structure</h2>
<pre style="background:#f8fafc; padding:12px; border-radius:6px; border-left:4px solid #0ea5a6;"> Chennai_House_Price_Prediction/ │ ├── notebooks/ │ ├── eda_analysis.ipynb # Exploratory data analysis and visualizations │ ├── model_training.ipynb # Model benchmarking and evaluation │ ├── data/ │ └── chennai_housing.csv # Dataset (cleaned / preprocessed) │ ├── src/ │ ├── preprocessing.py # Data cleaning & transformation pipeline │ ├── train_model.py # XGBoost model training script │ ├── results/ │ ├── model_performance.csv # Metrics summary │ └── visuals/ # EDA and result plots │ └── README.md # Project documentation </pre>
<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">
<h2>🌐 Explore Notebook</h2>
<p align="center"> 🔗 <a href="https://colab.research.google.com/drive/YOUR_NOTEBOOK_LINK" target="_blank" style="font-size:16px; color:#0ea5a6; text-decoration:none;"> Open in Google Colab </a> </p>
<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">
<h2>📫 Contact</h2>
<p> <strong>Author:</strong> S. Rajadurai <br> <strong>Email:</strong> rajadurai3491@gmail.com <br> <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/rajadurai-2004cse" target="_blank">View Profile</a> </p>
<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">
<p align="center" style="font-size:14px; color:#94a3b8;"> © 2025 Chennai Housing Price Prediction – Data Science Project </p>
