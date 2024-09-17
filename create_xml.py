import pandas as pd
import os
from string_func import replace_dots
from string_func import convert_to_title_case


def generate_odoo_views(models, module, df, output_dir):
    # Tạo thư mục chứa các file XML nếu chưa tồn tại
    os.makedirs(output_dir, exist_ok=True)
    xml_files = []
    for model_name in models.keys():
        if model_name in ['menus_level_1', 'menus_level_2']:
            continue
        model_name_lower = replace_dots(model_name.lower())
        file_path = os.path.join(output_dir, f"{replace_dots(model_name_lower)}_views.xml")
        xml_files.append(f"views/{replace_dots(model_name_lower)}_views.xml")
        with open(file_path, 'w', encoding='utf-8') as xmlfile:
            # Ghi header của file XML
            xmlfile.write("""<?xml version="1.0" encoding="utf-8"?>
<odoo>
""")
            # Form View
            form_fields = []
            tree_fields = []
            current_table = False
            current_module = False
            is_menu = True
            parent = False
            en_description = False
            search_fields = []
            search_count = False
            for index, row in df.iterrows():
                if not pd.isna(row['Module']) and row['Module'] == module:
                    current_module = True
                if not pd.isna(row['Module']) and not row['Module'] == module:
                    current_module = False
                if row['Table'] and not pd.isna(row['Table']) and row['Table'] == model_name:
                    current_table = True
                    en_description = row['En_Description']
                elif row['Table'] and not pd.isna(row['Table']) and not row['Table'] == model_name:
                    current_table = False
                if current_table and current_module:
                    if not pd.isna(row['search_view']):
                        search_fields.append(f"<field name='{row['Fields']}'/>")
                        search_count = True
                    if not pd.isna(row['is_menu']):
                        is_menu = row['is_menu']
                    else:
                        is_menu=True
                    if not pd.isna(row['parent_id']):
                        parent = row['parent_id']
                    if pd.notna(row['View_form']) and row['View_form'].lower() != 'false':
                        form_fields.append(f"<field name='{row['Fields']}'/>")
                    if pd.notna(row['View_tree']) and row['View_tree'].lower() != 'false':
                        tree_fields.append(f"<field name='{row['Fields']}'/>")
                else:
                    continue
            # Chia danh sách form_fields thành 2 nhóm
            middle_index = len(form_fields) // 2
            group1_fields = form_fields[:middle_index]
            group2_fields = form_fields[middle_index:]

            # Tạo view form với hai nhóm
            form_view = f"""
                <record id="view_{model_name_lower}_form" model="ir.ui.view">
                    <field name="name">{model_name}.form</field>
                    <field name="model">{model_name}</field>
                    <field name="arch" type="xml">
                        <form string="{convert_to_title_case(replace_dots(model_name))}">
                            <sheet>
                                <group>
                                    <group>
                                        {'\n                                        '.join(group1_fields)}
                                    </group>
                                    <group>
                                        {'\n                                        '.join(group2_fields)}
                                    </group>
                                </group>
                            </sheet>
                        </form>
                    </field>
                </record>
            """
            # Tree View
            tree_view = f"""
    <record id="view_{model_name_lower}_tree" model="ir.ui.view">
        <field name="name">{model_name}.tree</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <tree string="{convert_to_title_case(replace_dots(model_name))}">
                {'\n                '.join(tree_fields)}
            </tree>
        </field>
    </record>
"""
            # Search View
            search_view = f"""
    <record id="view_{model_name_lower}_search" model="ir.ui.view">
        <field name="name">{model_name}.search</field>
        <field name="model">{model_name}</field>
        <field name="arch" type="xml">
            <search string="{convert_to_title_case(replace_dots(model_name))}">
                {'\n                '.join(search_fields)}
            </search>
        </field>
    </record>
"""
            # Action
            action = f"""
    <record id="action_{model_name_lower}" model="ir.actions.act_window">
        <field name="type">ir.actions.act_window</field>
        <field name="name">{convert_to_title_case(replace_dots(model_name))}</field>
        <field name="res_model">{model_name}</field>
        <field name="view_mode">tree,form</field>"""
            if search_count > 0:
                action += f"""
        <field name="search_view_id" ref="view_{model_name_lower}_search"/>"""
            action += """
    </record>
"""
            menuitem = """
"""
            if is_menu:
                if parent:
                    menuitem += f"""
<menuitem id="menu_{model_name_lower}" parent="{parent}" name="{en_description}" action="action_{model_name_lower}"/>
"""
                else:
                    menuitem += f"""
<menuitem id="menu_{model_name_lower}" parent="menu_{module}" name="{en_description}" action="action_{model_name_lower}"/>
"""

            # Ghi các phần tử vào file XML
            xmlfile.write(form_view)
            xmlfile.write(tree_view)
            if search_count > 0:
                xmlfile.write(search_view)
            xmlfile.write(action)
            xmlfile.write(menuitem)
            # Kết thúc file XML
            xmlfile.write("</odoo>")

        print(f"View XML for {model_name} saved to {file_path}")
    return xml_files
