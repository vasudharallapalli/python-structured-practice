import pandas as pd  # Import pandas for data handling

# Load CSV file into DataFrame
df = pd.read_csv('C:\\Users\\vasud\\Documents\\python-structured-practice\\Day01\\day01_sampledataset_2.csv')

# Group by city and calculate mean temperature
avg_temperature_city = (
    df.groupby('city')['temperature']      # Group temperature by city
    .mean()                                # Calculate mean per group
    .reset_index()                         # Convert index to column
    .sort_values(by='temperature', ascending=False)  # Sort by temp desc
    .rename(columns={'temperature': 'avg_temperature'})  # Rename column
)

print("Average temperature by city:")  # Print message
print(avg_temperature_city)            # Display result DataFrame
