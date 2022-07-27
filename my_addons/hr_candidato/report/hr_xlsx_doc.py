from odoo import models, fields, tools
from odoo.exceptions import UserError, ValidationError, AccessError
from datetime import datetime, time, date, timedelta
import calendar
from datetime import timedelta
import pytz

class reportPuesto(models.AbstractModel):
    _name = 'report.hr_candidato.puesto_doc_view'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):

        domain = []

        # Formats
        grey_format = workbook.add_format({
            'bg_color': '#b2beb5'
        })
        grey_border_format = workbook.add_format({
            'bg_color': '#b2beb5',
            'bottom': 1,
        })
        grey_bold_format = workbook.add_format({
            'bg_color': '#b2beb5',
            'bold': True,
        })

        merge_format = workbook.add_format(
            {'bold': 1, 'border': 1, 'align': 'center', 'valign': 'vdistributed', 'font_size': 8, 'bg_color': '#C0C0C0',
             'font_color': '#000000', 'font_name': 'Calibri'})
        merge_format1 = workbook.add_format(
            {'bold': 1, 'border': 1, 'align': 'center', 'valign': 'vdistributed', 'font_size': 8, 'bg_color': '#E78B93',
             'font_color': '#000000', 'font_name': 'Calibri'})
        info_format = workbook.add_format(
            {'bold': 1, 'border': 1, 'align': 'left', 'valign': 'vdistributed', 'font_size': 10, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        info_format_center = workbook.add_format(
            {'bold': 1, 'border': 1, 'align': 'center', 'valign': 'vdistributed', 'font_size': 10,
             'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        info_format_rigth = workbook.add_format(
            {'bold': 1, 'border': 1, 'align': 'right', 'valign': 'vdistributed', 'font_size': 10, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        merge_format2 = workbook.add_format(
            {'bold': 1, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'font_size': 12, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        merge_format3 = workbook.add_format(
            {'bold': 1, 'border': 1, 'align': 'right', 'valign': 'vcenter', 'font_size': 12, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        merge_format4 = workbook.add_format(
            {'bold': 1, 'border': 1, 'align': 'left', 'valign': 'vcenter', 'font_size': 12, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        merge_format5 = workbook.add_format(
            {'bold': 0, 'border': 1, 'align': 'left', 'valign': 'vcenter', 'font_size': 10, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        normal_format = workbook.add_format(
            {'bold': 0, 'border': 1, 'align': 'left', 'valign': 'vcenter', 'font_size': 10, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        normal_format_center = workbook.add_format(
            {'bold': 0, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'font_size': 10, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri'})
        head_format = workbook.add_format(
            {'bold': 1, 'border': 0, 'align': 'center', 'valign': 'vdistributed', 'font_size': 10,
             'bg_color': '#CC8034'})
        head_format1 = workbook.add_format(
            {'bold': 1, 'border': 0, 'align': 'center', 'valign': 'vdistributed', 'font_size': 10,
             'bg_color': '#FBBA00'})

        date_format = workbook.add_format(
            {'bold': 0, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'font_size': 10, 'bg_color': '#FFFEFE',
             'font_color': '#000000', 'font_name': 'Calibri', 'num_format': 'dd/mm/yy'})

        #Crear una Hoja
        sheet = workbook.add_worksheet('Candidates to verify for Job Position')
        col = 0
        row = 0
        sheet.write(row,col,'Name')
        col+=1
        sheet.write(row, col, 'Job Position')
        col += 1
        sheet.write(row, col, 'CI')
        col += 1
        sheet.write(row, col, 'Address')
        col += 1
        sheet.write(row, col, 'Formal Grade That You Possess')
        col += 1
        sheet.write(row, col, 'Experience that you possess')
        col = 0
        row = 1
        for a in data['candidato1']:

            sheet.write(row, col, a['name'])
            col+=1
            sheet.write(row, col, a['job_id'])
            col += 1
            sheet.write(row, col, a['ci'])
            col += 1
            sheet.write(row, col, a['address'])
            col += 1
            sheet.write(row, col, a['grade_possesses'])
            col += 1
            sheet.write(row, col, a['experience'])
            row += 1
            col=0