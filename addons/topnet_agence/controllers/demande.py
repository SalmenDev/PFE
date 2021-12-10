# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class TopnetAgence(http.Controller):
    @http.route('/dem_abonn', type="http", auth='public', website=True)
    def demandeab(self, **kw):
        return http.request.render('topnet_agence.demab', {})

    class TopnetAgence(http.Controller):
        @http.route('/dem/abonn', type="http", auth='public', website=True)
        def demandeab(self, **kw):
            http.request.env['topnet_agence.demab'].sudo().create(kw)
            return http.request.render('topnet_agence.demab', {})


class TopnetAgence(http.Controller):
    @http.route(['/liste_dem'], type='http', auth="public", website=True)
    def demab(self, **kw):
        demandes = request.env['topnet_agence.demab'].sudo().search([('agence', '=', 'Topnet Agence La Marsa')])
        return http.request.render("topnet_agence.demab_list", {'demandes': demandes})

    class TopnetAgence(http.Controller):
        @http.route(['/liste_dem_Bardo'], type='http', auth="public", website=True)
        def dem(self, **kw):
            demandes = request.env['topnet_agence.demab'].sudo().search([('agence', '=', 'Topnet Agence Bardo')])
            return http.request.render("topnet_agence.demab_list", {'demandes': demandes})

class TopnetAgence(http.Controller):
        @http.route('/demande/<user_id>', type="http", auth='public', methods=['GET'], website=True)
        def dem(self, user_id, **kw):
            user = request.env['topnet_agence.demab'].sudo().search([('id', '=', user_id)])
            return http.request.render('topnet_agence.coord1', {'user': user})




