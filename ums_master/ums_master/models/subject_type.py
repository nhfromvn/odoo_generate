from odoo import models, fields

class SubjectType(models.Model):
    _name = "subject.type"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    abbr_name = fields.Char(string="Abbrevation Name", required=False)
    sequence = fields.Integer(string="Sequence", required=False)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
