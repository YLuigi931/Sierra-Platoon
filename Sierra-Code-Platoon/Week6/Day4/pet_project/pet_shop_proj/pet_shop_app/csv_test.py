from csv_handler import CSV_Interface

product_interface = CSV_Interface('./data/products.csv')

print(product_interface.column_names)
print()
print(product_interface.all_data)
print('1 ----------------------------------------\n')
# test appending 1 row to csv 

new_data = {'id': '5', 'name': 'fluffy_feather_string', 'category': 'accessories', 'image_url' : 'https://image.chewy.com/is/image/catalog/91380_MAIN._AC_SL600_V1539005221_.jpg', 'cost': 30}

updated_data = product_interface.append_one_row_to_file(new_data)
print(updated_data)

# print('2 ----------------------------------------\n')

# for row in product_interface.all_data:
#     if row['id'] == '5':
#         product_interface.remove_a_row(row)
#         break

# print(product_interface.all_data)