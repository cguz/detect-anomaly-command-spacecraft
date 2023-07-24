import pandas as pd
import numpy as np

# Load the spacecraft command data into a pandas DataFrame
df = pd.read_csv("command.csv", delimiter=",")

df["timestamp"] = pd.to_datetime(df["timestamp"].str.replace("Z", "+00:00"))

# Calculate the time between successive commands
df["time_diff"] = (df["timestamp"].shift(-1) - df["timestamp"]) # df["timestamp"].diff()

# Identify commands that occur too frequently (e.g., more than once per hour)
freq_threshold = pd.Timedelta(hours=1)
df["freq_anomaly"] = np.where(df["time_diff"] < freq_threshold, 1, 0)

# Identify repeated commands (e.g., when the same command is sent more than once)
df["repeated_anomaly"] = np.where(df.duplicated(["command"]), 1, 0)

# Combine the results into a single "anomaly" column
df["anomaly"] = df["freq_anomaly"] + df["repeated_anomaly"]

# Display the results
print(df[df["anomaly"] > 0])
