import os
import pandas as pd
from string_func import replace_dots
from string_func import convert_to_title_case
import ast


def create_po_file(save_path, module, df):
    # Nội dung của file .po
    po_content = """\
# Translation of Odoo Server.
# This file contains the translation of the following modules:
# 	* ums_master
#
msgid ""
msgstr ""
"Project-Id-Version: Odoo Server 17.0+e\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2024-08-27 13:27+0000\n"
"PO-Revision-Date: 2024-08-27 13:27+0000\n"
"Last-Translator: \n"
"Language-Team: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: \n"
"Plural-Forms: \n"

#. module: {module_name}
#: model:ir.ui.menu,name:{module_name}.menu_{module_name}
msgid ""
msgstr "" 
"""

    menu_code = """
#. module: {module_name}
#: model:ir.ui.menu,name:{module_name}.{menu_id}
msgid "{en_name}"
msgstr "{vn_name}"         
"""
    model_code = """ 
#. module: {module_name}
#: model:ir.actions.act_window,name:{module_name}.action_{model_name}
msgid "{en_model_description}"
msgstr "{model_description}"

#. module: {module_name}
#: model:ir.ui.menu,name:{module_name}.menu_{model_name}
msgid "{en_model_description}"
msgstr "{model_description}"          
"""
    field_code = """
#. module: {module_name}      
#: model:ir.model.fields,field_description:{module_name}.field_{model_name}__{field_name}
msgid "{EN_String}"
msgstr "{VN_String}"       
"""
    selection_code = """    
#. module: {module_name}      
#: model:ir.model.fields.selection,field_description:{module_name}.selection__{model_name}__{field_name}__{select_option}
msgid "{EN_String_selection}"
msgstr "{VN_String_selection}"  
"""
    sql_constraint_code = """
#. module: {module_name}
#: model:ir.model.constraint,message:ums_master.{constraint_name}
msgid "{en_constraint_message}"
msgstr "{vn_constraint_message}"
"""
    # Loops through each row in the DataFrame to generate model code
    models = {}
    current_model = None
    for index, row in df.iterrows():
        if pd.notna(row['Menu_level_1']) and row['Module'] and row['Module'] == module:
            list_menu_lv1 = eval(str(row['Menu_level_1']))
            for id, en,vn in list_menu_lv1:
                po_content += menu_code.format(
                    module_name=module,
                    menu_id=id,
                    en_name=en,
                    vn_name=vn
                )
        if pd.notna(row['Menu_level_1']) and row['Module'] and row['Module'] == module:
            list_menu_lv2 = eval(str(row['Menu_level_2']))
            for _, id, en, vn in list_menu_lv2:
                po_content += menu_code.format(
                    module_name=module,
                    menu_id=id,
                    en_name=en,
                    vn_name=vn
                )
        if row['Table'] and not pd.isna(row['Table']):
            current_model = row['Table']
            current_en_model_description = row['En_Description'] if pd.notna(
                row['En_Description']) else 'No description'
            current_model_description = row['Description'] if pd.notna(row['Description']) else 'Không có mô tả'
            if current_model not in models:
                models[current_model] = model_code.format(module_name=module,
                                                          model_name=replace_dots(current_model),
                                                          model_description=current_model_description,
                                                          en_model_description=current_en_model_description)
        current_field_code = field_code
        # Chuỗi đầu vào
        if str(row['Field Type']).lower() == 'selection' and pd.notna(row['selection']):
            option_string = row['selection']
            option_string_list = ast.literal_eval(option_string)
            option_value_en_string = row['EN_String_selection'] if pd.notna(row['EN_String_selection']) else ''
            option_value_vn_string = row['VN_String_selection'] if pd.notna(row['VN_String_selection']) else ''
            option_en_string_value_list = False
            option_vn_string_value_list = False
            if option_value_en_string:
                option_en_string_value_list = ast.literal_eval(option_value_en_string)
            if option_value_vn_string:
                option_vn_string_value_list = ast.literal_eval(option_value_vn_string)
            for index, (option, option_value) in enumerate(option_string_list):
                current_field_code += selection_code.format(
                    field_name=row['Fields'],
                    module_name=module,
                    model_name=replace_dots(current_model),
                    EN_String_selection=option_en_string_value_list[
                        index] if option_en_string_value_list else 'No value',
                    VN_String_selection=option_vn_string_value_list[index] if option_vn_string_value_list else '',
                    select_option=option,
                )

        if pd.notna(row['Fields']):
            models[current_model] += current_field_code.format(
                field_name=row['Fields'],
                module_name=module,
                model_name=replace_dots(current_model),
                EN_String=row['EN_String'] if pd.notna(row['EN_String']) else '',
                VN_String=row['VN_String'] if pd.notna(row['VN_String']) else '',
            )
            if pd.notna(row['Unique']):
                # Thêm phần dịch cho constraint unique
                constraint_name = f"constraint_{replace_dots(current_model)}_{row['Fields']}_unique_constraint"
                en_constraint_message = f"The {row['Fields']} must be unique."
                vn_constraint_message = f"{row['VN_String']} phải là duy nhất."
                models[current_model] += sql_constraint_code.format(
                    module_name=module,
                    model_name=replace_dots(current_model),
                    constraint_name=constraint_name,
                    en_constraint_message=en_constraint_message,
                    vn_constraint_message=vn_constraint_message,
                )
    for code in models.values():
        po_content += code
    # Tạo thư mục nếu chưa tồn tại
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Ghi nội dung vào file .po ở đường dẫn chỉ định
    with open(save_path, "w", encoding="utf-8") as po_file:
        po_file.write(po_content)
