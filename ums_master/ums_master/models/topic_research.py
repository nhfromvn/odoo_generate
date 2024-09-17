from odoo import models, fields

class TopicResearch(models.Model):
    _name = "topic.research"
    _description = 'No description'


    code = fields.Char(string="Research area code", required=True)
    name = fields.Char(string="Research area name", required=True)
    note = fields.Text(string="note", required=False)
    sequence = fields.Integer(string="Sequence", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
