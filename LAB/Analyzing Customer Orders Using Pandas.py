import pandas as pd

order_data = pd.DataFrame({
    'CustomerID': [101, 102, 101, 103, 102],
    'OrderDate': ['2026-01-05', '2026-01-10', '2026-01-15',
                  '2026-01-20', '2026-01-25'],
    'Product': ['Pen', 'Book', 'Pen', 'Bag', 'Book'],
    'Quantity': [2, 3, 4, 1, 5]
})

order_data['OrderDate'] = pd.to_datetime(order_data['OrderDate'])

print("Orders per Customer:")
print(order_data.groupby('CustomerID').size())

print("\nAverage Quantity per Product:")
print(order_data.groupby('Product')['Quantity'].mean())

print("\nEarliest Order Date:", order_data['OrderDate'].min())
print("Latest Order Date:", order_data['OrderDate'].max())
