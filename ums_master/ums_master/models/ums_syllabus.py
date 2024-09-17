from odoo import models, fields

class UmsSyllabus(models.Model):
    _name = "ums.syllabus"
    _description = 'No description'


    man_department_id = fields.Many2one(string="Management Department", comodel_name="hr.department", required=True)
    type_training_id = fields.Many2one(string="Type of Training", comodel_name="type.of.training", required=True)
    cohort_id = fields.Many2one(string="Cohort", comodel_name="ums.cohort", required=True)
    subject_id = fields.Many2one(string="Subject", comodel_name="ums.subject", required=True)
    references_docs = fields.Text(string="Reference Docs", required=False)
    syllabus_files = fields.Char(string="Syllabus files", required=False)
    state = fields.Selection(string="State", required=False, selection=[('draft', 'Mới'), ('waiting', 'Chờ phê duyệt'), ('approved', 'Đã phê duyệt')])

    _sql_constraints = [
        
    ]
