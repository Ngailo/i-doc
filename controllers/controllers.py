# -*- coding: utf-8 -*-
from odoo import http

# class Dms(http.Controller):
#     @http.route('/dms/dms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dms/dms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dms.listing', {
#             'root': '/dms/dms',
#             'objects': http.request.env['dms.dms'].search([]),
#         })

#     @http.route('/dms/dms/objects/<model("dms.dms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dms.object', {
#             'object': obj
#         })