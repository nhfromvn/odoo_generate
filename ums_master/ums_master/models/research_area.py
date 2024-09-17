from odoo import models, fields

class ResearchArea(models.Model):
    _name = "research.area"
    _description = 'No description'


    name = fields.Char(string="Name of research field", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Field of research code", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
