import pandas as pd
def convert_to_title_case(snake_str):
    # Tách chuỗi theo dấu gạch dưới
    words = snake_str.split('_')
    # Viết hoa chữ cái đầu của từng từ
    capitalized_words = [word.capitalize() for word in words]
    # Nối các từ đã được viết hoa thành chuỗi hoàn chỉnh
    return ' '.join(capitalized_words)
def convert_string(input_string):
    # Tách chuỗi thành các phần tại dấu chấm
    parts = input_string.split('.')

    # Viết hoa chữ cái đầu tiên của mỗi phần và kết hợp lại
    output_string = ''.join(part.capitalize() for part in parts)

    return output_string


def replace_dots(s):
    if pd.notna(s):
        return s.replace('.', '_')
    return s
