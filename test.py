import pandas as pd

# Đọc dữ liệu từ file Excel vào DataFrame
excel_file_path = "C:/Users/Admin/Downloads/File import danh mục (1).xlsx"

# Sử dụng pandas để đọc dữ liệu từ file Excel
df = pd.read_excel(excel_file_path, sheet_name=0)  # sheet_name=0 đọc sheet đầu tiên
# Nếu tiêu đề nằm ở hàng thứ hai, sử dụng header=1
df1 = pd.read_excel(excel_file_path, sheet_name=0, header=1)

print(df)
