# -*- coding: utf-8 -*-
# from odoo import http


# class Topnet(http.Controller):
#     @http.route('/topnet/topnet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/topnet/topnet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('topnet.listing', {
#             'root': '/topnet/topnet',
#             'objects': http.request.env['topnet.topnet'].search([]),
#         })

#     @http.route('/topnet/topnet/objects/<model("topnet.topnet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('topnet.object', {
#             'object': obj
#         })
