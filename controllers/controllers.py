# -*- coding: utf-8 -*-
from odoo import http

# class Doc(http.Controller):
#     @http.route('/doc/doc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/doc/doc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('doc.listing', {
#             'root': '/doc/doc',
#             'objects': http.request.env['doc.doc'].search([]),
#         })

#     @http.route('/doc/doc/objects/<model("doc.doc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('doc.object', {
#             'object': obj
#         })