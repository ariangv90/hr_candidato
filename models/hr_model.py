from odoo import models, fields, api

class areaAte(models.Model):
    _name = 'modelo.area'
    _description = 'Model Military Area'

    applicant_id = fields.Many2one(
        'hr.applicant', string='applicant'
    )

    job_id = fields.Many2one(
        'hr.job', string='Job Position',
    )


    @api.onchange('applicant_id')
    def change_job(self):
        if self.applicant_id:
         self.job_id = self.applicant_id.job_id

class medicalcheckup(models.Model):
    _name = 'model.checkup'
    _description = 'Model Medical checkup'

    applicant_id = fields.Many2one(
        'hr.applicant', string='Applicant'
    )
    job_id = fields.Many2one(
        'hr.job', string='Job Position',
    )
    area = fields.Char(
        string='Area of Health'
    )

    @api.onchange('applicant_id')
    def change_job(self):
        if self.applicant_id:
            self.job_id = self.applicant_id.job_id


class searchRe(models.Model):
    _name = 'model.searchre'
    _description = 'Model Search of References'

    applicant_id = fields.Many2one(
        'hr.applicant', string='Applicant'
    )

    informative_interest = fields.Text(
        string='Informative interest'
    )


class sumary(models.Model):
    _name = 'model.resumen'
    _description = 'Model Summary of Labor verifications'

    applicant_id = fields.Many2one(
        'hr.applicant', string='Applicant'
    )

    conclution = fields.Selection(
        [('NO', 'NO')],
        string='Concluciones'
    )

    recommendations = fields.Text(
        string='Recommendations'
    )


class psico(models.Model):
    _name = 'model.psico'
    _description = 'Model Summary of psychological evaluation'

    applicant_id = fields.Many2one(
        'hr.applicant', string='Applicant'
    )

    conclution = fields.Selection(
        [('NO', 'NO')],
        string='Concluciones'
    )

    recommendations = fields.Text(
        string='Recommendations'
    )


class slide(models.Model):
    _name = 'model.evalua'
    _description = 'Model the student is record of integral evaluation'

    applicant_id = fields.Many2one(
        'hr.applicant', string='Applicant'
    )

    course_id = fields.Many2one(
        'slide.channel', string='Course of Habilitation',
        readonly=True,
    )

    final_evaluation = fields.Integer(
        string='Final evaluation'
    )

    quality = fields.Text(
        string='Quality Evaluation'
    )

    @api.onchange('applicant_id')
    def change_course(self):
        if self.applicant_id:
            self.course_id = self.applicant_id.course

