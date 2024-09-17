from string_func import replace_dots
import csv

def generate_access_rights_csv(models,module, output_csv_path):
    # Open CSV file for writing
    with open(output_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(
            ['id', 'name', 'model_id:id', 'group_id:id', 'perm_read', 'perm_write', 'perm_create', 'perm_unlink'])

        # Generate access rights for each model
        for model_name in models.keys():
            # Generate the ID and name for the access rights
            access_rights_id = f"access_{replace_dots(model_name)}"
            access_rights_name = f"{replace_dots(model_name)}_access_rights"

            # Assuming the model_id and group_id will be generated like this (you may need to adjust this)
            model_id = f"{module}.model_{replace_dots(model_name.lower())}"
            group_id = "base.group_user"  # This is an example group, adjust as needed

            # Permissions can be adjusted as needed. Below example gives full access.
            perm_read = 1
            perm_write = 1
            perm_create = 1
            perm_unlink = 1

            # Write the row to CSV
            writer.writerow(
                [access_rights_id, access_rights_name, model_id, group_id, perm_read, perm_write, perm_create,
                 perm_unlink])

    print(f"Access rights CSV saved to {output_csv_path}")