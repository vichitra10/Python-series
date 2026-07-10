# Combined Operations
catalog = [
            ('UrbanFlex_Hoodie', 500, 'Fashion'),
            ('LuxeWeave_Shirt', 800, 'Fashion'),
            ('AeroFit_Joggers', 1200, 'Fashion'),
            ('VelvetAura_Dress', 1800, 'Fashion'),
            ('Classic_Edge_Sneakers', 2500, 'Footwear'),
            ('PureRadiance_Cream', 650, 'Beauty'),
            ('BloomLip_Tint', 450, 'Beauty'),
            ('HydraGlow_Serum', 950, 'Beauty'),
            ('SmartFit_Watch', 3500, 'Electronics'),
            ('NoiseCancel_Headphones', 4200, 'Electronics')
          ]

max_category = ""
max_count = 0

category_to_products = {}
for name, price, category in catalog:

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(name)
# print(category_to_products)

category_with_max_product = ''
max_count = 0

for category, products in category_to_products.items():
    # print(category)
    # print(len(products))

    if  len(products) > max_count:
        max_count= len(products)
        category_with_max_product = category

print(f"Category with maximum products:{category_with_max_product}")
print(f"Number of products {max_count}") 

for product in category_to_products[category_with_max_product]:
    print(product)


