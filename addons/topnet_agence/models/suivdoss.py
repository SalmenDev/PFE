# -*- coding: utf-8 -*-

from odoo import models, fields


class topnet_agence(models.Model):
    _name = 'topnet_agence.suivdoss'
    _description = 'topnet_agence.suivdoss'

    type_offre = fields.Char(string="Type de l'offre")
    matricule = fields.Char(string="Matricule fiscale", required="True")
    registre = fields.Char(string="Registre de commerce", required="True")
    prise = fields.Selection([("oui", "Oui"), ("non", "Non")], string="Prise en charge", required="True")
    date = fields.Date(string="Date de prise en charge", required="True")
    agent = fields.Char(string="Agent commerciale", required="True")
    etat = fields.Selection(
        [("contrat en cours de traitement coté topnet", "Contrat en cours de traitement coté topnet"),
         ("Etude", "Etude"),
         ("contrat rejeté par topnet", "Contrat rejeté par topnet"),
         ("contrat rejeté par TT", "Contrat rejeté par TT"),
         ("contrat validé par topnet", "Contrat validé par topnet"),
         ("ligne installé par TT", "ligne installé par TT"),
         ("initiale", "Initiale")])

    ref_etude = fields.Char(string=" Référende Etude")
    frais = fields.Integer(string="Frais de raccordement", required="True")
