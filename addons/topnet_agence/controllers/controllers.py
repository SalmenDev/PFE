# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

#contrroleur de la page creer utilisateur
class TopnetAgence(http.Controller):
    @http.route('/creer_user', type="http", auth='public', website=True)
    def creeruser(self, **kw):
        return http.request.render('topnet_agence.admin', {})
#creation dans la base de données
class TopnetAgence(http.Controller):
    @http.route('/creer/user', type="http", auth='public', website=True)
    def creeruser(self, **kw):
        http.request.env['topnet_agence.admin'].sudo().create(kw)
        return http.request.render('topnet_agence.admin', {})

    # recherche dans la base de données
    class TopnetAgence(http.Controller):
        @http.route(['/liste_user'], type='http', auth="public", website=True)
        def user(self, **kw):
            users = request.env['topnet_agence.admin'].sudo().search([])
            return http.request.render("topnet_agence.admin_list", {'users': users})


class TopnetAgence(http.Controller):
    @http.route('/consult/<user_id>', type="http", auth='public', methods=['GET'], website=True)
    def creeruser(self, user_id, **kw):
        user = request.env['topnet_agence.admin'].sudo().search([('id', '=', user_id)])
        return http.request.render('topnet_agence.coord', {'user': user})

    @http.route('/update/<user_id>', type="http", auth='public', methods=['POST', 'GET'], website=True)
    def updateuser(self, user_id, **kw):
        user = request.env['topnet_agence.admin'].sudo().search([('id', '=', user_id)])
        user.sudo().write(kw)
        return http.request.render('topnet_agence.modifier', {'user': user})

class TopnetAgence(http.Controller):
    @http.route('/desac/<user_id>', type="http", auth='public', methods=['GET'], website=True)
    def desacuser(self, user_id, **kw):
        user = request.env['topnet_agence.admin'].sudo().search([('id', '=', user_id)])
        return http.request.render('topnet_agence.desac_merci', {})

class TopnetAgence(http.Controller):
    @http.route('/depot', type="http", auth='public', website=True)
    def depot(self, **kw):
        return http.request.render('topnet_agence.deposerdos', {})

class TopnetAgence(http.Controller):
    @http.route('/suivi_dossier', type="http", auth='public', website=True)
    def suivi(self, **kw):
        return http.request.render('topnet_agence.suividossier', {})



class TopnetAgence(http.Controller):
    @http.route('/suivi_dossier/<user_id>', type="http", auth='public', methods=['POST', 'GET'], website=True)
    def dem(self, user_id, **kw):
        user = request.env['topnet_agence.demab'].sudo().search([('id', '=', user_id)])
        user.sudo().write(kw)
        return http.request.render('topnet_agence.suividossier', {'user': user})

    @http.route('/updatesuivi/<user_id>', type="http", auth='public', methods=['POST', 'GET'], website=True)
    def updatesuivi(self, user_id, **kw):
        user = request.env['topnet_agence.demab'].sudo().search([('id', '=', user_id)])
        user.sudo().write(kw)
        return http.request.render('topnet_agence.suivdoss', {'user': user})

class TopnetAgence(http.Controller):
    @http.route('/historique', type="http", auth='public', website=True)
    def historique(self, **kw):
        return http.request.render('topnet_agence.historique', {})


class TopnetAgence(http.Controller):
    @http.route('/historique/<user_id>', type="http", auth='public', methods=['GET'], website=True)
    def hist(self, user_id, **kw):
        user = request.env['topnet_agence.demab'].sudo().search([('id', '=', user_id)])
        return http.request.render('topnet_agence.historique', {'user': user})


class TopnetAgence(http.Controller):
    @http.route(['/liste_agent_Bardo'], type='http', auth="public", website=True)
    def agent(self, **kw):
        agents = request.env['topnet_agence.admin'].sudo().search([('role', '=', 'agent'), ('agence', '=', 'Topnet Agence Bardo')])
        return http.request.render("topnet_agence.agent_list_bardo", {'agents': agents})

class TopnetAgence(http.Controller):
    @http.route('/consultbardo/<user_id>', type="http", auth='public', methods=['GET'], website=True)
    def creeragent(self, user_id, **kw):
        user = request.env['topnet_agence.admin'].sudo().search([('id', '=', user_id)])
        return http.request.render('topnet_agence.coordbardo', {'user': user})

    @http.route('/updatebardo/<user_id>', type="http", auth='public', methods=['POST', 'GET'], website=True)
    def updateagent(self, user_id, **kw):
        user = request.env['topnet_agence.admin'].sudo().search([('id', '=', user_id)])
        user.sudo().write(kw)
        return http.request.render('topnet_agence.modifbardo', {'user': user})


class TopnetAgence(http.Controller):
    @http.route('/creer_fiche', type="http", auth='public', website=True)
    def fiche(self, **kw):
        return http.request.render('topnet_agence.fiche', {})

    class TopnetAgence(http.Controller):
        @http.route('/creer/fiche', type="http", auth='public', website=True)
        def creerfiche(self, **kw):
            http.request.env['topnet_agence.fiche'].sudo().create(kw)
            return http.request.render('topnet_agence.fiche', {})

    class TopnetAgence(http.Controller):
        @http.route(['/liste_fiches'], type='http', auth="public", website=True)
        def fiche(self, **kw):
            fiches = request.env['topnet_agence.fiche'].sudo().search([])
            return http.request.render("topnet_agence.fiche_list", {'fiches': fiches})

    class TopnetAgence(http.Controller):
        @http.route('/consultfiche/<fiche_id>', type="http", auth='public', methods=['GET'], website=True)
        def creerfiche(self, fiche_id, **kw):
            fiche = request.env['topnet_agence.fiche'].sudo().search([('id', '=', fiche_id)])
            return http.request.render('topnet_agence.consultfiche', {'fiche': fiche})

        @http.route('/updatefiche/<fiche_id>', type="http", auth='public', methods=['POST', 'GET'], website=True)
        def updatefiche(self, fiche_id, **kw):
            fiche = request.env['topnet_agence.fiche'].sudo().search([('id', '=', fiche_id)])
            fiche.sudo().write(kw)
            return http.request.render('topnet_agence.modif_fiche', {'fiche': fiche})

    class TopnetAgence(http.Controller):
        @http.route(['/liste_agent_Marsa'], type='http', auth="public", website=True)
        def agent(self, **kw):
            agents = request.env['topnet_agence.admin'].sudo().search([('role', '=', 'agent'), ('agence', '=', 'Topnet Agence La Marsa')])
            return http.request.render("topnet_agence.agent_list", {'agents': agents})

        class TopnetAgence(http.Controller):
            @http.route('/consultag/<user_id>', type="http", auth='public', methods=['GET'], website=True)
            def creeragent(self, user_id, **kw):
                user = request.env['topnet_agence.admin'].sudo().search([('id', '=', user_id)])
                return http.request.render('topnet_agence.coordag', {'user': user})

        @http.route('/updateag/<user_id>', type="http", auth='public', methods=['POST', 'GET'], website=True)
        def updateagent(self, user_id, **kw):
            user = request.env['topnet_agence.admin'].sudo().search([('id', '=', user_id)])
            user.sudo().write(kw)
            return http.request.render('topnet_agence.modifag', {'user': user})


class TopnetAgence(http.Controller):
    @http.route('/Contactez_nous', type="http", auth='public', website=True)
    def contact(self, **kw):
        return http.request.render('topnet_agence.contactus', {})


class TopnetAgence(http.Controller):
    @http.route('/Contactez/nous', type="http", auth='public', website=True)
    def contact(self, **kw):
        http.request.env['topnet_agence.contactus'].sudo().create(kw)
        return http.request.render('topnet_agence.contactus', {})

    class TopnetAgence(http.Controller):
        @http.route('/rdv', type="http", auth='public', website=True)
        def contact(self, **kw):
            return http.request.render('topnet_agence.rdv', {})



class TopnetAgence(http.Controller):
    @http.route('/propos', type="http", auth='public', website=True)
    def contact(self, **kw):
        return http.request.render('topnet_agence.us', {})


class TopnetAgence(http.Controller):
    @http.route('/creer_agence', type="http", auth='public', website=True)
    def creeragence(self, **kw):
        return http.request.render('topnet_agence.agence', {})


class TopnetAgence(http.Controller):
    @http.route('/creer/agence', type="http", auth='public', website=True)
    def creeragence(self, **kw):
        http.request.env['topnet_agence.agence'].sudo().create(kw)
        return http.request.render('topnet_agence.agence', {})

    class TopnetAgence(http.Controller):
        @http.route(['/liste_agences'], type='http', auth="public", website=True)
        def agence(self, **kw):
            agences = request.env['topnet_agence.agence'].sudo().search([])
            return http.request.render("topnet_agence.agence_list", {'agences': agences})

    class TopnetAgence(http.Controller):
        @http.route('/consultagence/<agence_id>', type="http", auth='public', methods=['GET'], website=True)
        def creeragence(self, agence_id, **kw):
            agence = request.env['topnet_agence.agence'].sudo().search([('id', '=', agence_id)])
            return http.request.render('topnet_agence.consult', {'agence': agence})

        @http.route('/updateagence/<agence_id>', type="http", auth='public', methods=['POST', 'GET'], website=True)
        def updateagence(self, agence_id, **kw):
            agence = request.env['topnet_agence.agence'].sudo().search([('id', '=', agence_id)])
            agence.sudo().write(kw)
            return http.request.render('topnet_agence.modif_agence', {'agence': agence})

    class TopnetAgence(http.Controller):
        @http.route('/importer', type="http", auth='public', website=True)
        def depot(self, **kw):
            return http.request.render('topnet_agence.importer', {})

    class TopnetAgence(http.Controller):
        @http.route('/telecharger', type="http", auth='public', website=True)
        def creeruser(self, **kw):
            return http.request.render('topnet_agence.telecharger', {})
