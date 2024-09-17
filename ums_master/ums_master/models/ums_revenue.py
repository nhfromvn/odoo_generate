from odoo import models, fields


class UmsRevenue(models.Model):
    _name = "ums.revenue"
    _description = 'No description'

    code = fields.Char(string="Additional fees code", required=True)
    name = fields.Char(string="Additional fees code", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="note", required=False)
    type = fields.Selection(string="Type", required=False,
                            selection=[('additional', 'Besides Tuition Fees'), ('tuition', 'Tuition Fees')])

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
