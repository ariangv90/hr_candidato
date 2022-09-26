# -*- coding: utf-8 -*-
from odoo import http


class HrCandidato(http.Controller):
     @http.route('/hr_candidato/hr_candidato/', auth='user')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/hr_candidato/hr_candidato/objects/', auth='user')
     def list(self, **kw):
         return http.request.render('hr_candidato.listing', {
             'root': '/hr_candidato/hr_candidato',
             'objects': http.request.env['hr_candidato.hr_candidato'].search([]),
         })

     @http.route('/hr_candidato/hr_candidato/objects/<model("hr_candidato.hr_candidato"):obj>/', auth='user')
     def object(self, obj, **kw):
         return http.request.render('hr_candidato.object', {
             'object': obj
         })
