# -*- coding: utf-8 -*-

from odoo import models, fields, api


class resline(models.Model):
     _name = 'res.line'
     _description = 'res_line'


     client = fields.Many2one('res.bank',string='CLIENT')

     subcriptor = fields.Char(string='SUBCRIPTION')

     make_request = fields.Date(string="MAKE REQUEST")

     type_request = fields.Selection([('CHANGE CONFIGURATION','CHANGE CONFIGURATION')],string='TYPE REQUEST')

     type_client = fields.Selection([('CHANGE CONFIGURATION', 'CHANGE CONFIGURATION')], string='TYPE CLIENT')

     type_service = fields.Selection([
         ('X25/ X28', 'X25/ X28'),
         ('ARREND', 'ARREND'),
         ('F.RELAY', 'F.RELAY'),
          ('ADSL', 'ADSL')],
         string='TYPE SERVICES')

     speed = fields.Float(string='Speed')

     number_phone = fields.Integer(string='NUMBER PHONE(ONLY FOR ADSL)')

     number_line = fields.Char(string='NUMBER LINE')

     monetary1 = fields.Many2one('ir.qweb.field.monetary',string='MONETARY')

     address = fields.Char(string='ADDRESS')

     range_ip = fields.Char(string='RANGE IP PRIVATE')

     eventual = fields.Boolean(string='EVENTUAL')

     date_begin = fields.Date(string = 'DATE BEGIN')

     date_end = fields.Date(string = 'DATE END')

     technical_contact =fields.Many2one('res.partner',string='TECHNICAL CONTACT')

     phone_technical = fields.Integer(string='PHONE TECHNICAL',readonly=True)

     #Data Services X25/X28
     long_package = fields.Float(string='LONG PACKAGE')

     canals_logic = fields.Float(string='CANALS LOGIC NIVEL 2')

     long_windows = fields.Float(string='LONG WINDOWS NIVE 3')

     switched = fields.Float(string='x28 SWITCHED(KEY UP TO 8 CHAR)')

     type_protocol = fields.Selection([
         ('X25/ X28', 'X25/ X28'),
         ('IP DOWN', 'IP DOWN'),
         ('IP UP', 'IP UP')],
         string='TIPO DE PROTOCOLO(ASOCIADO AL TIPO DE TARIFA A APLICAR POR EL TRAFICO, MACAR CON UNA X)')

     description_X28 = fields.Text(string='DESCRIPTION')

     #DATA FOR FRAME RELAY SERVICES (IF YOU HAVE ONLY ONE CONNECTION DESTINATION,
     # LEAVE THE REST BLANK, IF THERE ARE MORE THAN 3 CONNECTION POINTS, ADD IN COMMENTS)

     cir = fields.Float(string='CIR')

     gateway_destination = fields.Char(string='GATEWAY DESTINATION')

     technical_contact1 = fields.Many2one('res.partner',string='TECHNICAL CONTACT')

     cir1 = fields.Float(string='CIR')

     gateway_destination1 = fields.Char(string='GATEWAY DESTINATION')

     technical_contact2 = fields.Many2one('res.partner', string='TECHNICAL CONTACT')

     cir2 = fields.Float(string='CIR')

     gateway_destination2 = fields.Char(string='GATEWAY DESTINATION')

     technical_contact3 = fields.Many2one('res.partner', string='TECHNICAL CONTACT')

     description_frame = fields.Text(string='DESCRIPTION FRAME RELAY')


     #DATA FOR LEASED LINE SERVICES (IF THERE ARE MORE THAN 1 CONNECTION POINT, ADD IN OBSERVATIONS)
     address_extre = fields.Char(string='INSTALLATION DIRECTION OF THE OTHER END')

     technical_contact4 = fields.Many2one('res.partner', string='TECHNICAL CONTACT')

     description_data = fields.Text(string='DESCRIPTION DATA')

     contact = fields.Many2one('res.partner',string='NAME AND SURNAME OF THE SERVICE APPLICANT')

     job = fields.Many2one('res.partner',string='JOB POSITION',readonly=True)


