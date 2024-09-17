import pandas as pd

# Đọc file CSV với mã hóa khác
csv_file_path = 'File Mau Xu Ly(Sheet1).csv'

try:
    # Thử với mã hóa ISO-8859-1 (latin1)
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')
except UnicodeDecodeError:
    try:
        # Thử với mã hóa cp1252
        df = pd.read_csv(csv_file_path, encoding='cp1252')
    except UnicodeDecodeError:
        # Thử với mã hóa UTF-16
        df = pd.read_csv(csv_file_path, encoding='utf-16')

# Chuyển đổi và lưu thành file Excel
xlsx_file_path = 'File Mau Xu Ly(Sheet1).xlsx'
df.to_excel(xlsx_file_path, index=False, engine='openpyxl')

print(f"File đã được chuyển đổi và lưu tại {xlsx_file_path}")
