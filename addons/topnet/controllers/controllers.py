# -*- coding: utf-8 -*-
from odoo import http
from werkzeug.wrappers import Request
from odoo.http import request




class Topnet(http.Controller):
    @http.route('/contact_list', website='true', auth='user')
    def index(self, **kw):
        contacts = request.env['topnet.contact'].sudo().search([])
        return http.request.render("topnet.list_contact", {'contacts':contacts})

class Topnet(http.Controller):
    @http.route('/adduser_form', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("topnet.create_user", {})
        
class Topnet(http.Controller):
    @http.route('/addsubscription_form', website='true', auth='user')
    def index(self, **kw):
        contacts = request.env['topnet.contact'].sudo().search([])
        return http.request.render("topnet.create_subscription", {'contacts':contacts})

class Topnet(http.Controller):
    @http.route('/followdemands', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("topnet.create_subscription", {})

class Topnet(http.Controller):
    @http.route('/CreateContact', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("topnet.create_contact", {})

class Topnet(http.Controller):
    @http.route('/contact_thanks', website='true', auth='user')
    def index(self, **kw):
        return http.request.render("topnet.contact_thanks", {})


class Topnet(http.Controller):
    @http.route('/create/contact',type='http', website='true', auth='user')
    def index(self, **post):
        contact = request.env['topnet.contact'].create({
            'name': post.get('contact_name'),
            'tel_fixe': post.get('contact_telfix'),
            'tel_gsm': post.get('contact_telgsm'),
            'email': post.get('contact_email'),
            'nature': post.get('contact_nature'),
            #'client_id': request.uid,  
        })
        return http.request.render("topnet.contact_thanks", {})
