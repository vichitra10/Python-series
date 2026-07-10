## Categories (Set)

products = [
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

categories_set = set()  ## Here I am creating the set 
for product in products: 
    categories_set.add(product[2])
print(categories_set)

categories_set.add('Electronics') # Trying to add duplicate category 
print(categories_set)
categories_set.add('Toys')  # Adding new category in the set
print(categories_set)

## Here i am checking category exists or not the category set

print("Fashion" in categories_set)
print("Grocery" in categories_set)

## count length from the categories set
total = len(categories_set)
print(f"Total categories are : {total}")