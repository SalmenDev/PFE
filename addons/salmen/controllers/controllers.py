# -*- coding: utf-8 -*-
from odoo import http


class Salmen(http.Controller):
    @http.route('/salmen/salmen/', auth='public')
    def index(self, **kw):
        return "I am the Master Salmen"

#     @http.route('/salmen/salmen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('salmen.listing', {
#             'root': '/salmen/salmen',
#             'objects': http.request.env['salmen.salmen'].search([]),
#         })

#     @http.route('/salmen/salmen/objects/<model("salmen.salmen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salmen.object', {
#             'object': obj
#         })
