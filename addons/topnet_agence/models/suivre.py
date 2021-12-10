# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class suivre(models.Model):
    _name = 'topnet_agence.suivre'
    _description = 'topnet_agence.suivre'


    def action_confirm(self):
        for rec in self:
            rec.state = 'valide'

    @api.model
    def default_get(self, fields):
        res = super(suivre, self).default_get(fields)
        res['etat'] = 'initiale'
        return res


    ID_contrat = fields.Many2one('demandes_clients.demandes_clients',
                                 ondelete='set null', string="Abonnement FO", index=True)
    type_offre = fields.Char(string="Offre client", related="ID_contrat.type_offre", required="True")
    matricule = fields.Char(string="Matricule fiscale", required="True")
    registre = fields.Char(string="Registre de commerce", related="ID_contrat.registre", required=True)
    prise = fields.Selection([("oui", "Oui"), ("non", "Non")], string="Prise en charge", required=True)
    etat = fields.Selection(
        [("contrat en cours de traitement coté topnet", "Contrat en cours de traitement coté topnet"),
         ("Etude", "Etude"),
         ("contrat rejeté par topnet", "Contrat rejeté par topnet"),
         ("contrat rejeté par TT", "Contrat rejeté par TT"),
         ("contrat validé par topnet", "Contrat validé par topnet"),
         ("ligne installé par TT", "ligne installé par TT"),
         ("initiale", "Initiale")])
    date = fields.Date(string="Date de prise en charge", required="True")
    state = fields.Selection([
        ('etude', 'Etude'),
        ('valide', 'Valide'),
    ], string='Status', readonly=True, default='etude')
    Reference = fields.Integer(string="Réference Etude", required=True)
    currency_id = fields.Many2one("res.currency", string="Devise")
    frais = fields.Monetary(string="Frais")


def action_view_suivi(self):
    action = self.env.ref('website_slides.slide_slide_action').read()[0]
    action['context'] = {
        'search_default_published': 1,
        'default_channel_id': self.id
        }
    action['domain'] = [('channel_id', "=", self.id), ('is_category', '=', False)]
    return action
