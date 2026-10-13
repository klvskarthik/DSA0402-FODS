import pandas as pd

property_data = pd.DataFrame({
    'PropertyID': [101, 102, 103, 104],
    'Location': ['Chennai', 'Vijayawada', 'Chennai', 'Hyderabad'],
    'Bedrooms': [3, 5, 6, 4],
    'Area': [1500, 2500, 3000, 1800],
    'Price': [5000000, 7000000, 9000000, 6000000]
})

print("Average Price by Location:")
print(property_data.groupby('Location')['Price'].mean())

print("\nProperties with More Than 4 Bedrooms:")
print((property_data['Bedrooms'] > 4).sum())

print("\nProperty with Largest Area:")
print(property_data.loc[property_data['Area'].idxmax()])
