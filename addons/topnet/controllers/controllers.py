# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request



class Topnet(http.Controller):
    @http.route('/topnet/users/', website='true',  auth='user')
    def index(self, **kw):
        users = request.env['topnet.user'].sudo().search([])
        return request.render("topnet.users_page", {'users':users})

class Topnet(http.Controller):
    @http.route('/topnet/user_create', website='true', auth='user')
    def index(self, **kw):
        return request.render("topnet.user_create", {})

#Controller for adding user success
#class Topnet(http.Controller)
#    @http.route('/create_sccuess', website='true', auth='user')
#    def index(self, **kw):
#        return.render("topnet.user_success", {})
            

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
