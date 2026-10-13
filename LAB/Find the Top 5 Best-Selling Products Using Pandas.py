import pandas as pd

data = pd.DataFrame({
    'Product': ['Pen', 'Book', 'Bag', 'Pen', 'Book',
                'Pencil', 'Bottle', 'Bag'],
    'Quantity': [50, 80, 30, 40, 60, 90, 20, 25]
})

top5 = data.groupby('Product')['Quantity'].sum().sort_values(
    ascending=False
).head(5)

print("Top 5 Best-Selling Products:")
print(top5)
