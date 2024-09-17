from odoo import models, fields

class UmsSpecialization(models.Model):
    _name = "ums.specialization"
    _description = 'No description'


    code = fields.Char(string="Specialization code", required=True)
    name = fields.Char(string="Specialization name", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
