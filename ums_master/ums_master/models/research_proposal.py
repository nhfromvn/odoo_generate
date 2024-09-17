from odoo import models, fields

class ResearchProposal(models.Model):
    _name = "research.proposal"
    _description = 'No description'


    code = fields.Char(string="Research proposal code", required=True)
    name = fields.Char(string="Research proposal name", required=True)
    abbr_name = fields.Char(string="Abbreviation name", required=False)
    note = fields.Text(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
