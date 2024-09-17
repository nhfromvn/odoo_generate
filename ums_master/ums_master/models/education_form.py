from odoo import models, fields

class EducationForm(models.Model):
    _name = "education.form"
    _description = 'No description'


    code = fields.Char(string="Education form code", required=True)
    name = fields.Char(string="Education form name", required=True)
    note = fields.Text(string="Note", required=False)
    abbr_name = fields.Char(string="Abbreviation name", )

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
