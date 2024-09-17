import ast
import pandas as pd
from string_func import convert_string


def generate_odoo_model(df):
    model_template = """from odoo import models, fields

class {model_class_name}(models.Model):
    _name = "{model_name}"
    _description = '{model_description}'

{fields}

    _sql_constraints = [
        {sql_constraints}
    ]
"""
    inherit_model_template = """from odoo import models, fields

class {model_class_name}(models.Model):
    _inherit = "{model_name}"

{fields}

    _sql_constraints = [
        {sql_constraints}
    ]
"""
    field_template = """
    {field_name} = fields.{field_type}(string="{field_label}", {field_params})"""

    sql_constraint_template = """('{constraint_name}', 'unique({field_name})', 'The {field_name} must be unique.')"""

    # Dictionary to store modules and models
    modules = {}

    field_type_mapping = {
        'char': 'Char',
        'boolean': 'Boolean',
        'many2one': 'Many2one',
        'one2many': 'One2many',
        'many2many': 'Many2many',
        'float': 'Float',
        'integer': 'Integer',
        'int': 'Integer',
        'text': 'Text',
        'selection': 'Selection',
        # Add more field types as needed
    }

    current_module = None
    current_model = None
    list_menu_level_1 = []
    list_menu_level_2 = []

    # Dictionary to store SQL constraints for each model
    sql_constraints = {}

    # Dictionary to store fields for each model
    model_fields = {}

    for _, row in df.iterrows():
        module = row['Module']
        model = row['Table']
        field_name = row['Fields']
        unique = row['Unique']
        not_generate_file = row.get('not_generate_file', False)  # Default is False
        menu_level_1 = row['Menu_level_1']
        menu_level_2 = row['Menu_level_2']

        if pd.notna(module):
            current_module = module
            if current_module not in modules:
                modules[current_module] = {}
                modules[current_module]['menus_level_1'] = []
                modules[current_module]['menus_level_2'] = []

        if pd.notna(menu_level_1):
            list_menu_level_1 = eval((menu_level_1))
            for id, en_name, vn_name in list_menu_level_1:
                modules[current_module]['menus_level_1'].append({
                    'id': id,
                    'en_name': en_name,
                    'vn_name': vn_name,
                })

        if pd.notna(menu_level_2):
            list_menu_level_2 = eval((menu_level_2))
            for parent, id, en_name, vn_name in list_menu_level_2:
                modules[current_module]['menus_level_2'].append({
                    'parent': parent,
                    'id': id,
                    'en_name': en_name,
                    'vn_name': vn_name,
                })

        if not not_generate_file:  # Only process if not_generate_file is not True
            if pd.notna(model):
                current_model = model
                model_class_name = convert_string(current_model)
                model_description = row['En_Description'] if pd.notna(row['En_Description']) else 'No description'
                sql_constraints[current_model] = []  # Initialize the constraints list for the model
                model_fields[current_model] = ""  # Initialize field storage

                modules[current_module][current_model] = model_template if not pd.notna(
                    row['Inherit']) else inherit_model_template

            if pd.notna(field_name) and current_model:
                field_type = field_type_mapping.get(str(row['Field Type']).lower(), 'Char')
                field_label = row['EN_String'] if pd.notna(row['EN_String']) else row['VN_String'] if pd.notna(
                    row['VN_String']) else field_name
                field_params = ', '.join(
                    f'{col}="{row[col]}"' if isinstance(row[col],
                                                        str) and not col.lower() == 'selection' else f'{col}={row[col]}'
                    for col in df.columns[df.columns.get_loc('VN_String') + 1: df.columns.get_loc('selection') + 1]
                    if pd.notna(row[col])
                )
                field_code = field_template.format(
                    field_name=field_name,
                    field_type=field_type,
                    field_label=field_label,
                    field_params=field_params
                )

                model_fields[current_model] += field_code

                # Add SQL constraint if 'unique' field is marked
                if pd.notna(unique) and unique:
                    constraint_name = f"{field_name}_unique_constraint"
                    sql_constraint = sql_constraint_template.format(
                        constraint_name=constraint_name,
                        field_name=field_name
                    )
                    sql_constraints[current_model].append(sql_constraint)

    # Replace the placeholders with actual fields and SQL constraints
    for module, models in modules.items():
        for model, model_code in models.items():
            if isinstance(model_code, str):
                constraints = ",\n        ".join(sql_constraints.get(model, [])) if model in sql_constraints else ""
                fields = model_fields.get(model, "")
                modules[module][model] = model_code.format(
                    model_class_name=convert_string(model),
                    model_name=model,
                    model_description="No description",
                    fields=fields,
                    sql_constraints=constraints
                )

    return modules
