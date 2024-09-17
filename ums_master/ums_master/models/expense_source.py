from odoo import models, fields

class ExpenseSource(models.Model):
    _name = "expense.source"
    _description = 'No description'


    name = fields.Char(string="Expense Source Name", required=True)
    abbr_name = fields.Char(string="Abbreviation", required=False)
    code = fields.Char(string="Expense Source Code", required=True)
    note = fields.Text(string="Note", required=False)
    type = fields.Selection(string="Type of Expense Source", required=False, selection=[('cdl', 'Chi độc lập'), ('ctnt', 'Chi theo nguồn thu')])
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
