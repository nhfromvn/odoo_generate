from odoo import models, fields

class TrainingType(models.Model):
    _name = "training.type"
    _description = 'No description'


    code = fields.Char(string="Training type code", required=True)
    name = fields.Char(string="Training type name", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
