# save_as: generate_traffic_data.py
import pandas as pd
import numpy as np
import os

def generate_traffic_data(num_points=1000):
    """Generate realistic Dehradun traffic data and save to CSV"""
    np.random.seed(42)
    hotspots = [
        ('Clock Tower', 30.3165, 78.0321, 180),  # (name, lat, lon, avg_vehicles)
        ('ISBT', 30.3457, 78.0332, 150),
        ('Rajpur Road', 30.3256, 78.0413, 160),
        ('Prem Nagar', 30.3165, 78.0289, 120)
    ]
    
    data = []
    for _ in range(num_points):
        loc, lat, lon, avg_veh = hotspots[np.random.choice(len(hotspots))]
        lat += np.random.normal(0, 0.0012)  # ~100m radius
        lon += np.random.normal(0, 0.0012)
        vehicles = int(np.random.normal(avg_veh, 30))
        speed = max(5, 50 - (vehicles/5) + np.random.normal(0, 5))
        hour = np.random.randint(6, 22)  # 6AM-10PM
        time = f"{hour}:{np.random.randint(0, 59):02d}"
        data.append([loc, vehicles, speed, time, hour, lat, lon])
    
    return pd.DataFrame(data, columns=['Location','Vehicles','Speed','Time','Hour','Latitude','Longitude'])

# Generate and save the data
df = generate_traffic_data(1000)
output_file = 'dehradun_traffic_data.csv'

try:
    df.to_csv(output_file, index=False)
    print(f"✅ Successfully generated and saved {len(df)} records to {output_file}")
    print(f"📁 File saved to: {os.path.abspath(output_file)}")
    print("\nFirst 5 rows:")
    print(df.head())
except Exception as e:
    print(f" Error saving file: {e}")
    print("Please check directory permissions or try a different filename")

