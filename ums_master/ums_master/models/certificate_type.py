from odoo import models, fields

class CertificateType(models.Model):
    _name = "certificate.type"
    _description = 'No description'


    code = fields.Char(string="Certificate type code", required=True)
    name = fields.Char(string="Certificate type code", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
