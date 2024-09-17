from odoo import models, fields

class ExemptCategory(models.Model):
    _name = "exempt.category"
    _description = 'No description'


    code = fields.Char(string="Exempt category code", required=True)
    name = fields.Char(string="Exempt category name", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
