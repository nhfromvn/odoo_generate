from odoo import models, fields

class HrTilte(models.Model):
    _name = "hr.tilte"
    _description = 'No description'


    name = fields.Char(string="Name lecturer position", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Lecturer position code ", required=True)
    note = fields.Text(string="Note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
