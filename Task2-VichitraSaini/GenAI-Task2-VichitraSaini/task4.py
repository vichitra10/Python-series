## Loop Control with conditions (break & continue)
daily = [200,150,0,400,50,-1,300]
total_sales = 0
for sale in daily:
    print(sale)
    if sale == -1:
        print(f"Corrupted data")
        break
    elif sale == 0:
        print(f"No sales")
        continue
    else:
        total_sales+=sale
        print(f"Today's Sale: {sale}")
        print(f"Running Total: {total_sales}") 

print(f"\nFinal Total Sales: {total_sales}")      
        

