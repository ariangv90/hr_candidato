from odoo import api, fields, models, _
from odoo.exceptions import UserError
import babel
from collections import defaultdict
from datetime import date, datetime, time
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone
from pytz import utc

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.exceptions import Warning
from odoo.tools import float_utils
import tempfile
import binascii
import xlrd
import base64
import zipfile
from tempfile import mktemp
from odoo.modules.module import get_module_resource, get_resource_path
import datetime


class hrsolicitudreport(models.TransientModel):
    _name = 'hr.solicitud.report'
    _description = 'Behavior of the process of selection per month'

    date_month = fields.Selection([
        ('01', 'January'),
        ('02', 'Febrery'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ], string='Mouth',required=True
    )


    def action_report(self):
        candidato = []
        candidatoModel = self.env['hr.applicant']
        docs = candidatoModel.search(
            []
        )
        for doc in docs:
            if doc.create_date.__str__().split('-')[1].lower() == self.date_month:
                candidato.append({
                 'name':doc.name,
                 'ci' : doc.ci,
                 'address':doc.address,
                 'grade_possesses':doc.grade_possesses,
                 'create_date':doc.create_date,
                })

        datas={
        'doc_model': 'hr.applicant',
         'name':self.date_month,
          'candidato1':candidato,
        }
        return self.env.ref('hr_candidato.solicitud_report').report_action(self,data=datas)

class hrpuestoreport(models.TransientModel):
    _name = 'hr.puesto.report'
    _description = 'Candidates to verify for job of work'

    job_id = fields.Many2one(
        'hr.job', string='Job Position'
    )

    def action_report(self):
        candidato = []
        candidatoModel = self.env['hr.applicant']

        docs = candidatoModel.search(
            [('job_id', '=', self.job_id.id)]
        )

        for doc in docs:
            candidato.append({
                'name': doc.name,
                'ci': doc.ci,
                'job_id': doc.job_id.name,
                'address': doc.address,
                'grade_possesses': doc.grade_possesses,
                'experience': doc.experience,
            })

        datas = {
            'doc_model': 'hr.applicant',
            'name': self.job_id,
            'candidato1': candidato,
        }
        return self.env.ref('hr_candidato.puesto_doc_view').report_action(self, data=datas)

class hretatapasreport(models.TransientModel):
    _name = 'hr.etapas.report'
    _description = 'Candidates list in stages'

    etapas_id = fields.Many2one(
        'hr.recruitment.stage', string='Etapas'
    )

    def action_report(self):
        candidato = []
        candidatoModel = self.env['hr.applicant']
        docs = candidatoModel.search(
            [('stage_id', '=', self.etapas_id.id)]
        )
        for doc in docs:
            candidato.append({
                'name': doc.name,
                'ci': doc.ci,
                'job_id': doc.job_id.name,
                'stage_id': doc.stage_id.name,
                'address': doc.address,
                'grade_possesses': doc.grade_possesses,

            })
        datas = {
            'doc_model': 'hr.applicant',
            'name': self.etapas_id,
            'candidato1': candidato,
        }
        return self.env.ref('hr_candidato.etapas_report').report_action(self, data=datas)


class hrcursoreport(models.TransientModel):
    _name = 'hr.curso.report'
    _description = 'Candidates list for courses'

    course_id = fields.Many2one(
        'slide.channel', string='Course of Habilitation'
    )

    def action_report(self):
        candidato = []
        candidatoModel = self.env['hr.applicant']
        docs = candidatoModel.search(
            [('course', '=', self.course_id.id)]
        )
        for doc in docs:
            candidato.append({
                'name': doc.name,
                'ci': doc.ci,
                'job_id': doc.job_id.name,
                'course_id': doc.course.name,
                'address': doc.address,
                'grade_possesses': doc.grade_possesses,

            })
        datas = {
            'doc_model': 'hr.applicant',
            'name': self.course_id,
            'candidato1': candidato,
        }
        return self.env.ref('hr_candidato.cursos_report').report_action(self, data=datas)


def get_year():
    year_list = []

    for i in range(2000, 2040):
        year_list.append(i, str(i))
    return year_list

class hrannoreport(models.TransientModel):
    _name = 'hr.anno.report'
    _description = 'List of candidates approved per year'

    date_year = fields.Selection(
    [
     ('2015','2015'),
     ('2016', '2016'),
     ('2017', '2017'),
     ('2018', '2018'),
     ('2019', '2019'),
     ('2020', '2020'),
     ('2021', '2021'),
     ('2022', '2022'),
     ('2023', '2023'),
     ('2024', '2024'),
     ('2025', '2025'),
     ],
    string='Anno',
    required=True,
    )


    def action_report(self):
        candidato = []
        candidatoModel = self.env['hr.applicant']
        docs = candidatoModel.search([])

        for doc in docs:
            print(doc.create_date.__str__().split('-')[0].lower())
            if doc.create_date.__str__().split('-')[0].lower() == self.date_year:
                candidato.append({
                    'name': doc.name,
                    'ci': doc.ci,
                    'address': doc.address,
                    'grade_possesses': doc.grade_possesses,
                    'anno': self.date_year,
                })
        datas = {
            'doc_model': 'hr.applicant',
            'name': self.date_year,
            'candidato1': candidato,
        }
        return self.env.ref('hr_candidato.anno_report').report_action(self, data=datas)