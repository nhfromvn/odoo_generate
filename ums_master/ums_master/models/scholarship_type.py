from odoo import models, fields

class ScholarshipType(models.Model):
    _name = "scholarship.type"
    _description = 'No description'


    code = fields.Char(string="Scholarship type code", required=True)
    name = fields.Char(string="Scholarship type name", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
