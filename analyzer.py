import pandas as pd
import numpy as np
from datetime import datetime

# Set a seed so results are the same every time you run
np.random.seed(42)

# 1. Create hourly time range from Jan 1 to Jan 31, 2024
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='h')  # 'h' is correct now

# 2. Define sample devices and rooms
devices = ['Air Conditioner', 'Refrigerator', 'Washing Machine', 'Lights', 'Fan', 'TV', 'Heater', 'Computer']
rooms = ['Living Room', 'Bedroom', 'Kitchen', 'Bathroom']

# 3. Generate realistic data
data = {
    'Timestamp': date_range,
    'Device': np.random.choice(devices, size=len(date_range)),
    'Room': np.random.choice(rooms, size=len(date_range)),
    'Voltage (V)': np.random.normal(230, 10, size=len(date_range)).round(1),
    'Usage (kWh)': np.random.uniform(0.1, 2.0, size=len(date_range)).round(3)
}

# 4. Create a DataFrame
df = pd.DataFrame(data)

# 5. Add cost column (₹6.5 per kWh)
df['Cost (INR)'] = (df['Usage (kWh)'] * 6.5).round(2)

# 6. (Optional) Extract Date and Hour columns for analysis
df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
df['Hour'] = pd.to_datetime(df['Timestamp']).dt.hour

# 7. Save to CSV
df.to_csv('electricity_usage.csv', index=False)

# 8. Print result
print("✅ Dataset generated and saved as 'electricity_usage.csv'")
print("📄 Columns in the dataset:", df.columns.tolist())
print(df.head())  # shows first 5 rows


