from odoo import models, fields

class WoundedSoldierClass(models.Model):
    _name = "wounded.soldier.class"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Wounded soldier class code", required=True)
    name = fields.Char(string="Wounded soldier class name", required=True)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
