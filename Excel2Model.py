import os
import pandas as pd
from openpyxl import load_workbook
from string_func import replace_dots
from string_func import convert_to_title_case
from create_xml import generate_odoo_views
from create_csv import generate_access_rights_csv
from create_python import generate_odoo_model
from create_po import create_po_file

def update_init_file(module_path):
    init_file_path = os.path.join(module_path, '__init__.py')

    # Ghi các import statement vào __init__.py
    with open(init_file_path, 'w', encoding="utf-8") as init_file:
        # Ghi import cho models
        init_file.write('from . import models\n')
        # Ghi import cho controllers
        init_file.write('from . import controllers\n')

    print(f"__init__.py has been updated with models and controllers imports.")


def update_controllers_init(controllers_path):
    controllers_init_path = os.path.join(controllers_path, '__init__.py')

    # Ghi các import statement vào __init__.py trong controllers
    with open(controllers_init_path, 'w', encoding="utf-8") as controllers_init_file:
        controllers_init_file.write('from . import main\n')

    print(f"__init__.py in controllers has been updated to import main.py.")


def create_manifest_file(module_path, module_name, xml_files):
    manifest_file_path = os.path.join(module_path, '__manifest__.py')

    # Nội dung cho __manifest__.py
    manifest_content = f'''# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{{
    'name': '{convert_to_title_case(module_name)}',
    'version': '1.0',
    'author': 'BMSTECH',
    'summary': '',
    'sequence': 1,
    'description': """
    """,
   'depends': [],

   'data': [
       'security/ir.model.access.csv',
     {',\n'.join(f"'{file}'" for file in xml_files)},
   ],
   'demo': [],
   'qweb': [],
   'license': 'LGPL-3',
   'installable': True,
   'application': True,
   'auto_install': False,
}}
'''

    with open(manifest_file_path, 'w', encoding="utf-8") as manifest_file:
        manifest_file.write(manifest_content)

    print(f"__manifest__.py has been created at {manifest_file_path}.")


# Đọc dữ liệu từ file Excel vào DataFrame
excel_file_path = "C:/Users/Admin/Downloads/File import danh mục (17).xlsx"
workbook = load_workbook(excel_file_path)
sheet = workbook.active

# Đọc dữ liệu từ sheet vào DataFrame
data = sheet.values
columns = next(data)[0:]
df = pd.DataFrame(data, columns=columns)

# Generate Odoo model code
odoo_modules = generate_odoo_model(df)

for module, odoo_models in odoo_modules.items():
    abs_path = f'D:/generate_files/ums_master/{module}'
    # Tạo các thư mục cần thiết
    models_path = os.path.join(abs_path, 'models/')
    controllers_path = os.path.join(abs_path, 'controllers/')
    security_path = os.path.join(abs_path, 'security/')
    views_path = os.path.join(abs_path, 'views/')
    po_path = os.path.join(abs_path, 'i18n/')
    os.makedirs(models_path, exist_ok=True)
    os.makedirs(controllers_path, exist_ok=True)
    os.makedirs(security_path, exist_ok=True)
    os.makedirs(views_path, exist_ok=True)
    os.makedirs(po_path, exist_ok=True)
    models_init_path = os.path.join(models_path, "__init__.py")
    with open(models_init_path, 'w', encoding="utf-8") as models_init_file:
        # Save the models to Python files
        for model_name, code in odoo_models.items():
            if model_name not in ['menus_level_1', 'menus_level_2']:
                file_path = os.path.join(models_path, f"{replace_dots(model_name.lower())}.py")
                with open(file_path, 'w', encoding="utf-8") as file:
                    file.write(code)
                print(f"Model {model_name} saved to {file_path}")
                models_init_file.write(f"from . import {replace_dots(model_name.lower())}\n")

    # Tạo file main.py rỗng trong thư mục controllers
    main_file_path = os.path.join(controllers_path, 'main.py')
    with open(main_file_path, 'w', encoding="utf-8") as main_file:
        pass  # Tạo file rỗng
    print(f"Main file created at {main_file_path}")

    # Cập nhật __init__.py sau khi đã tạo tất cả các file mô hình
    update_init_file(abs_path)

    # Cập nhật __init__.py trong thư mục controllers để import main.py
    update_controllers_init(controllers_path)

    # Path to save the CSV file
    output_csv_file = os.path.join(security_path, 'ir.model.access.csv')

    # Generate the CSV
    generate_access_rights_csv(odoo_models, module, output_csv_file)

    # Tạo file XML menu nếu có parent_id
    xml_files = []
    # Tạo các file XML
    xml_files.append('views/menu.xml')
    xml_files.extend(generate_odoo_views(odoo_models, module, df, views_path))
    xml_file_path = os.path.join(views_path, "menu.xml")
    menus_level_1 = odoo_models['menus_level_1']
    menus_level_2 = odoo_models['menus_level_2']
    with open(xml_file_path, 'w', encoding='utf-8') as xmlfile:
        menuitem = f"""<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <menuitem id="menu_{module}" name="{convert_to_title_case(module)}"/>"""
        lv1_code = ''
        lv2_code = ''
        for menu in menus_level_1:
            lv1_code += f"""
            <menuitem id="{menu['id']}" name="{menu['en_name']}" parent="menu_{module}"/>"""
        for menu in menus_level_2:
            if menu['parent']:
                lv2_code += f"""
                <menuitem id="{menu['id']}" name="{menu['en_name']}" parent="{menu['parent']}"/>"""
            else:
                lv2_code += f"""
<menuitem id="{menu['id']}" name="{menu['en_name']}" parent="menu_{module}"/>
"""
        xmlfile.write(menuitem)
        xmlfile.write(lv1_code)
        xmlfile.write(lv2_code)
        xmlfile.write("\n</odoo>")
    # Đường dẫn thư mục lưu file .po
    output_po_file = os.path.join(po_path, 'vi_VN.po')

    # Tạo file .po và lưu vào đường dẫn chỉ định
    create_po_file(output_po_file, module, df)

    # Tạo file __manifest__.py
    create_manifest_file(abs_path, module, xml_files)
