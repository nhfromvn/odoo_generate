from odoo import models, fields

class ObjectClassification(models.Model):
    _name = "object.classification"
    _description = 'No description'


    name = fields.Char(string="Name ", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Code", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
