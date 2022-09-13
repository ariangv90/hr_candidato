# -*- coding: utf-8 -*-
from odoo import http


class HrModelo(http.Controller):
     @http.route('/hr_modelo/hr_modelo/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/hr_modelo/hr_modelo/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('hr_modelo.listing', {
             'root': '/hr_modelo/hr_modelo',
             'objects': http.request.env['hr_modelo.hr_modelo'].search([]),
         })

     @http.route('/hr_modelo/hr_modelo/objects/<model("hr_modelo.hr_modelo"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('hr_modelo.object', {
             'object': obj
         })
