import pandas as pd
import os
from string_func import replace_dots
from string_func import convert_to_title_case
from openpyxl import load_workbook

abs_path = f'D:/generate_files/ums_master'
excel_file_path = "C:/Users/Admin/Downloads/File import danh mục (17).xlsx"
workbook = load_workbook(excel_file_path)
sheet = workbook.active

# Đọc dữ liệu từ sheet vào DataFrame
data = sheet.values
columns = next(data)[0:]
df = pd.DataFrame(data, columns=columns)

def generate_odoo_views(df, output_dir, xml_filename="odoo_views.xml"):
    # Tạo thư mục chứa file XML nếu chưa tồn tại
    os.makedirs(output_dir, exist_ok=True)
    xml_filepath = os.path.join(output_dir, xml_filename)

    with open(xml_filepath, 'w', encoding='utf-8') as xmlfile:
        # Ghi header của file XML
        xmlfile.write("""<?xml version="1.0" encoding="utf-8"?>\n<odoo>\n""")

        current_table = None
        current_table_rows = []
        en_description = None

        # Lặp qua từng dòng trong DataFrame
        for index, row in df.iterrows():
            # Kiểm tra xem dòng có chứa tên bảng (Table) hay không
            if not pd.isna(row['Table']) and row['Table'] != current_table:
                # Nếu đang có bảng khác, thì xử lý bảng đó trước khi chuyển sang bảng mới
                if current_table is not None and current_table_rows:
                    process_table(current_table, current_table_rows, en_description, xmlfile)

                # Cập nhật bảng hiện tại và `en_description` mới
                current_table = row['Table']
                en_description = row['En_Description']
                current_table_rows = []

            # Thêm dòng hiện tại vào danh sách các dòng của bảng hiện tại
            current_table_rows.append(row)

        # Xử lý bảng cuối cùng trong DataFrame
        if current_table is not None and current_table_rows:
            process_table(current_table, current_table_rows, en_description, xmlfile)

        # Kết thúc file XML
        xmlfile.write("</odoo>")

    print(f"View XML saved to {xml_filepath}")


def process_table(table_name, table_rows, en_description, xmlfile):
    """Xử lý việc tạo các view cho mỗi bảng."""
    model_name = table_name
    model_name_lower = replace_dots(model_name.lower())

    form_fields = []
    tree_fields = []
    search_fields = []
    is_menu = True
    parent = None
    generate_file = False

    # Thu thập tất cả các field liên quan đến bảng hiện tại
    for row in table_rows:
        if row.get('not_generate_file') == True:
            generate_file = True  # Xác định bảng này cần tạo file

        if pd.notna(row.get('View_form')) and row['View_form'].lower() != 'false':
            form_fields.append(f"<field name='{row['Fields']}'/>")
        if pd.notna(row.get('View_tree')) and row['View_tree'].lower() != 'false':
            tree_fields.append(f"<field name='{row['Fields']}'/>")
        if pd.notna(row.get('search_view')):
            search_fields.append(f"<field name='{row['Fields']}'/>")
        if pd.notna(row.get('is_menu')):
            is_menu = row['is_menu']
        if pd.notna(row.get('parent_id')):
            parent = row['parent_id']

    # Nếu không cần sinh file cho bảng này, bỏ qua
    if not generate_file:
        return

    # Chia danh sách form_fields thành 2 nhóm nếu có
    middle_index = len(form_fields) // 2
    group1_fields = form_fields[:middle_index]
    group2_fields = form_fields[middle_index:]

    # Tạo form view nếu có field
    form_view = ""
    if form_fields:
        form_view = f"""
    <record id="view_master_{model_name_lower}_form" model="ir.ui.view">
        <field name="name">{model_name}.form</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <form string="{convert_to_title_case(replace_dots(model_name))}">
                <sheet>
                    <group>
                        <group>
                            {'\n                            '.join(group1_fields)}
                        </group>
                        <group>
                            {'\n                            '.join(group2_fields)}
                        </group>
                    </group>
                </sheet>
            </form>
        </field>
    </record>
"""
    # Tạo tree view nếu có field
    tree_view = ""
    if tree_fields:
        tree_view = f"""
    <record id="view_master_{model_name_lower}_tree" model="ir.ui.view">
        <field name="name">{model_name}.tree</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <tree string="{convert_to_title_case(replace_dots(model_name))}">
                {'\n                '.join(tree_fields)}
            </tree>
        </field>
    </record>
"""
    # Tạo search view nếu có search_fields
    search_view = ""
    if search_fields:
        search_view = f"""
    <record id="view_master_{model_name_lower}_search" model="ir.ui.view">
        <field name="name">{model_name}.search</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <search string="{convert_to_title_case(replace_dots(model_name))}">
                {'\n                '.join(search_fields)}
            </search>
        </field>
    </record>
"""

    # Tạo action view cho mỗi bảng
    action = f"""
    <record id="action_master_{model_name_lower}" model="ir.actions.act_window">
        <field name="type">ir.actions.act_window</field>
        <field name="name">{convert_to_title_case(replace_dots(model_name))}</field>
        <field name="res_model">{model_name}</field>
        <field name="view_mode">tree,form</field>"""
    if search_fields:
        action += f"""
        <field name="search_view_id" ref="view_master_{model_name_lower}_search"/>"""
    action += """
    </record>
"""

    # Tạo menu item nếu is_menu = True
    menuitem = ""
    if is_menu:
        if parent:
            menuitem += f"""
<menuitem id="menu_master_{model_name_lower}" parent="ums_master.{parent}" name="{en_description}" action="action_master_{model_name_lower}"/>
"""
        else:
            menuitem += f"""
<menuitem id="menu_master_{model_name_lower}" parent="menu_main" name="{en_description}" action="action_master_{model_name_lower}"/>
"""

    # Ghi tất cả các view của bảng vào file XML
    xmlfile.write(form_view)
    xmlfile.write(tree_view)
    if search_view:
        xmlfile.write(search_view)
    xmlfile.write(action)
    xmlfile.write(menuitem)


generate_odoo_views(df, abs_path)
