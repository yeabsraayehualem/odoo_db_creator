# -*- coding: utf-8 -*-
# from odoo import http


# class CreateDb(http.Controller):
#     @http.route('/create_db/create_db', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_db/create_db/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_db.listing', {
#             'root': '/create_db/create_db',
#             'objects': http.request.env['create_db.create_db'].search([]),
#         })

#     @http.route('/create_db/create_db/objects/<model("create_db.create_db"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_db.object', {
#             'object': obj
#         })

