
# Inputs from user
initial_stock_level = int(input('Kindly enter an initial stock level :'))
number_of_months_to_plan = int(input('Kindly enter the number of months to plan :'))
planned_month_sales_quantity = {}
for i in range(1, number_of_months_to_plan + 1):
    sales_quantity = int(input(f'Kindly enter the planned sales quantity for month {i} : '))
    planned_month_sales_quantity[f'month_{i}'] = sales_quantity

# Displaying production quantities
print('\n''The resulting production quantities are: \n')


# Zero-level strategy calculation
def stock_quantity(stock_level: int, months: int, sales_qty: dict) -> None:
    prod_qties = []
    current_stock_level = stock_level
    for k in range(1, months + 1):
        if sales_qty[f'month_{k}'] <= current_stock_level:
            prod_qties.append(0)
            current_stock_level -= sales_qty[f'month_{k}']
            # print(sales_qty[f'month_{k}'], current_stock_level, 0)
        else:
            to_production = sales_qty[f'month_{k}'] - current_stock_level
            prod_qties.append(to_production)
            current_stock_level += to_production
            current_stock_level -= sales_qty[f'month_{k}']
            # print(sales_qty[f'month_{k}'], current_stock_level, total_prod)

    for v in range(len(prod_qties)):
        print(f'Production quantity month {v + 1} - {prod_qties[v]}')

# User Process input
stock_quantity(initial_stock_level, number_of_months_to_plan, planned_month_sales_quantity)




