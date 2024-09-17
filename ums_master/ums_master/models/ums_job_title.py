from odoo import models, fields

class UmsJobTitle(models.Model):
    _name = "ums.job.title"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Code", required=True)
    name = fields.Char(string="Name", required=True)
    note = fields.Text(string="Note", required=False)
    abbr_name = fields.Char(string="Abbrevation Name", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
