# -*- coding: utf-8 -*-
from odoo import http


class RedIp(http.Controller):
     @http.route('/red_ip/red_ip/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/red_ip/red_ip/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('red_ip.listing', {
             'root': '/red_ip/red_ip',
             'objects': http.request.env['red_ip.red_ip'].search([]),
         })

     @http.route('/red_ip/red_ip/objects/<model("red_ip.red_ip"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('red_ip.object', {
             'object': obj
         })
