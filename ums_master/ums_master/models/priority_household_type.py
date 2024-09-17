from odoo import models, fields

class PriorityHouseholdType(models.Model):
    _name = "priority.household.type"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Priority household code", required=True)
    name = fields.Char(string="Priority household name", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
