## **2. Methods**

### **2.1 Datasets**

**File Inventory:**
The dataset required for this study is stored in the directory `./data`. The primary files included are:

- `covid19_cases.csv`
- `covid19_testing_data.csv`
- `population_data.csv`
- `mobility_data.csv`

**Schema:**
1. **covid19_cases.csv**
   - `date`: DATE (date of case reporting)
   - `location`: STRING (geographical identifier)
   - `new_cases`: INTEGER (number of new cases reported that day)
   - `cumulative_cases`: INTEGER (total cases reported to date)

2. **covid19_testing_data.csv**
   - `date`: DATE (date of testing)
   - `location`: STRING (geographical identifier)
   - `tests_done`: INTEGER (number of tests conducted)
   - `positivity_rate`: FLOAT (percentage of tests returning positive)

3. **population_data.csv**
   - `location`: STRING (geographical identifier)
   - `population`: INTEGER (total population of the location)
   - `density`: FLOAT (population density per square km)

4. **mobility_data.csv**
   - `date`: DATE (date of data collection)
   - `location`: STRING (geographical identifier)
   - `mobility_index`: FLOAT (change in mobility compared to baseline)

**Temporal Coverage:**
The datasets span from January 1, 2020, to the present date of October 31, 2023.

**Provenance:**
The datasets have been sourced from reputable public health databases, including the World Health Organization (WHO), local government health departments, and the Google Mobility Reports. Each dataset has undergone validation to ensure accuracy of timestamps, identifiers, and numerical entries.

### **2.2 Preprocessing and Feature Engineering**

**Preprocessing Steps:**
1. **Date Formatting:**
   - Convert date columns to a standard `datetime` format.

2. **Handling Missing Values:**
   - Filling in missing values using interpolation methods based on the historical data trends.

3. **Normalization:**
   - Normalize `new_cases`, `tests_done`, and `mobility_index` using Min-Max scaling to bring all features within the range [0, 1].

4. **Feature Creation:**
   - Generate moving averages for `new_cases` (e.g., 7-day moving average).
   - Compute the ratios of `new_cases` to `tests_done` to derive a new feature indicating the testing efficiency.

### **2.3 Experimental Design**

#### Train/Validation/Test Split Logic:
1. **Time-Aware Split:**
   - Use the data from January 1, 2020, to September 30, 2022, for training.
   - Utilize October 1, 2022, to August 31, 2023, for validation.
   - Reserve the test set from September 1, 2023, to October 31, 2023.

#### Hyperparameter Strategy:
1. **Grid Search:**
   - Conduct grid search over specified hyperparameters for model selection (e.g., learning rates, number of layers, batch sizes).
   - Use cross-validation during the grid search process to ensure robustness.

#### Compute/Runtime Environment Assumptions:
1. **Hardware:**
   - Experiments will be conducted on NVIDIA GPUs (e.g., RTX 2080) with at least 16GB memory.
   - Utilize TensorFlow 2.x or PyTorch for model implementations.

2. **Software:**
   - Python 3.8 with libraries: pandas, NumPy, and scikit-learn.

#### Evaluation Protocol for Forecast Horizon:
1. **Multi-Horizon Forecasting:**
   - Evaluate models for 1-day, 7-day, and 14-day forecasts to compare predictive performance.

2. **Metrics for Evaluation:**
   - Root Mean Squared Error (RMSE)
   - Mean Absolute Percentage Error (MAPE)
   - R-squared (R²)

### **2.4 Baselines and Robustness Checks**

**Baseline Models:**
1. **Simple Models:**
   - Naïve Forecast: Uses the previous day's forecast.
   - Seasonal Autoregressive Integrated Moving Average (SARIMA): For seasonality adjustments.
   
2. **Complex Models:**
   - Long Short-Term Memory (LSTM) networks for deep learning contexts.
   - Gradient Boosting Machines (GBM).

**Robustness Checks:**
1. **Statistical Tests:**
   - Apply the Diebold-Mariano test to compare forecasting accuracy.
   - Perform residual analysis to validate model assumptions.
   
2. **Ablation Studies:**
   - Conduct experiments by removing certain features or changing model components to assess their impact on performance.

### **2.5 Limitations**
- Data quality may affect predictions if reported cases are under-represented or affected by testing strategies.
- Geographic diversity can introduce biases in model generalizability.
- Unforeseen future policy changes or viral mutations may introduce external variances not captured in historical data.

This methodology is designed to ensure clarity, control, and robustness in the experimental setup, adhering to IEEE Access standards, and providing sufficient detail for replication.