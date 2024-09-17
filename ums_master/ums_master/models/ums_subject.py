from odoo import models, fields

class UmsSubject(models.Model):
    _name = "ums.subject"
    _description = 'No description'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string="Subject Code", required=True)
    name = fields.Char(string="Subject Name", required=True)
    sub_eng_name = fields.Char(string="English Name", required=True)
    credit = fields.Float(string="Credit", required=True)
    credit_theory = fields.Float(string="Credit Theory", required=True)
    credit_pract = fields.Float(string="Credit Practice", required=True)
    pract_type = fields.Float(string="Practice Type", required=True)
    old_code = fields.Char(string="Old Code", required=False)
    process_evaluation_duration = fields.Float(string="Process Evaluation Percent", required=False)
    midterm_evaluation_duration = fields.Float(string="Midterm Evaluation Percent", required=False)
    final_evaluation_duration = fields.Float(string="Final Evaluation Percent", required=False)
    practical_evaluation_duration = fields.Float(string="Practical Evaluation Percent", required=False)
    midterm_theory_exam_format = fields.Char(string="Midterm theory exam format", required=False)
    midterm_theory_exam_time = fields.Float(string="Midterm theory exam time", required=False)
    final_theory_exam_format = fields.Char(string="Final theory exam format", required=False)
    final_theory_exam_time = fields.Float(string="Final theory exam time", required=False)
    final_practical_exam_format = fields.Char(string="Final practical exam format", required=False)
    state = fields.Selection(string="State", required=False, selection=[('0', 'Còn hiệu lực'), ('1', 'Hết hiệu lực')])
    type_sub = fields.Selection(string="Type Subject", required=False, selection=[('out_training', 'Ngoài đào tạo'), ('in_training', 'Môn học'), ('equivalent_sub', 'Môn học tương đương')])
    categorization = fields.Selection(string="Categorization", required=False, selection=[('td', 'Tương đương'), ('tt', 'Thay thế')])
    sequence = fields.Integer(string="Sequence", required=False)
    note = fields.Text(string="Note", required=False)
    subject_type_id = fields.Many2one(string="Subject Type", comodel_name="subject.type", required=True)
    type_traning_ids = fields.Many2many(string="Type of Training", comodel_name="type.of.training", required=True)
    department_id = fields.Many2one(string="Management Department", comodel_name="hr.department", required=True)
    equi_sub_ids = fields.One2many(string="Equivalent Subject", inverse_name="subject_equi_id", comodel_name="ums.subject", required=False)
    pre_sub_ids = fields.One2many(string="Prerequisite Subject", inverse_name="subject_pre_id", comodel_name="ums.subject", required=False)
    req_sub_id = fields.Many2one(string="Require Subject", comodel_name="ums.subject", required=False)
    lang_id = fields.Many2one(string="Language", comodel_name="res.lang", required=True)
    specialization_id = fields.Many2one(string="Specialization", comodel_name="ums.specialization", required=False)
    from_cohort_id = fields.Many2one(string="Cohort from", comodel_name="ums.cohort", required=False)
    to_cohort_id = fields.Many2one(string="Cohort to", comodel_name="ums.cohort", required=False)
    subject_equi_id = fields.Many2one(string="Môn học", comodel_name="ums.subject", required=True)
    subject_pre_id = fields.Many2one(string="Môn học", comodel_name="ums.subject", required=True)

    _sql_constraints = [
        ('code_unique_constraint', 'unique(code)', 'The code must be unique.')
    ]
