from odoo import models, fields

class PolicySubjectSocialBenefit(models.Model):
    _name = "policy.subject.social.benefit"
    _description = 'No description'


    code = fields.Char(string="Policy subject social benefit code", required=True)
    name = fields.Char(string="Name of policy object and social allowance", required=True)
    note = fields.Char(string="Note", required=False)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
