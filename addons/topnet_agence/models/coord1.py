# -*- coding: utf-8 -*-
from odoo import models, fields


class topnet_agence(models.Model):
    _name = 'topnet_agence.coord1'
    _description = 'topnet_agence.coord1'

    nom = fields.Char(string="Nom et Prénom du gérant")
    cinpass = fields.Integer(string="Numéro CIN/Passeport")
    raison = fields.Char(string="Raison sociale")
    registre = fields.Char(string="Registre de commerce")
    tva = fields.Integer(string="Code TVA")
    Exonere = fields.Selection([("oui", "Oui"), ("non", "Non")])
    douane = fields.Integer(string="Code en douane")
    activite = fields.Char(string="Activité de l'entreprise")
    correspondance = fields.Char(string="Adresse de correspondance")
    Ville = fields.Char(string="Ville")
    postale = fields.Integer(string="Code postale")
    tel = fields.Char(string="Tél")
    fax = fields.Char(string="Fax")
    installation = fields.Char(string="Adresse d'installation")
    ville2 = fields.Char(string="Ville")
    postale2 = fields.Integer(string="Code postale")
    tel2 = fields.Char(string="Tél")
    fax2 = fields.Char(string="Fax")
    #  Contact Administratif et Financiers

    nom2 = fields.Char(string="Nom et prénom")
    Tel_admi = fields.Char(string="Tél")
    gsm_admi = fields.Char(string="GSM")
    email_admi = fields.Char(string="Email")

    #  Contact technique

    nom_tech = fields.Char(string="Nom et Prénom")
    tel_tech = fields.Char(string="Tél")
    gsm_tech = fields.Char(string="GSM")
    email_tech = fields.Char(string="Email")

    email_pri = fields.Char(string="Email principale")
    type_offre = fields.Char(string="Type de l'offre")
    debit = fields.Char(string="Débit")
    agence = fields.Selection([("Topnet Agence centre urbain nord", "Topnet Agence centre urbain nord"),
                               ("Topnet Agence Tunis", "Topnet Agence Tunis"),
                               ("Topnet Agence Bardo", "Topnet Agence Bardo"),
                               ("Topnet Agence Ennasr", "Topnet Agence Ennasr"),
                               ("Topnet Agence La Marsa", "Topnet Agence La Marsa"),
                               ("Topnet Agence Le Passage", "Topnet Agence Le Passage"),
                               ("Topnet Agence Bizerte", "Topnet Agence Bizerte"),
                               ("Topnet Agence Nabeul", "Topnet Agence Nabeul"),
                               ("Topnet Agence Khzema", "Topnet Agence Khzema"),
                               ("Topnet Agence Sousse", "Topnet Agence Sousse"),
                               ("Topnet Agence Monastir", "Topnet Agence Monastir"),
                               ("Topnet Agence Sfax", "Topnet Agence Sfax"),
                               ("Topnet Agence Taib Mhiri Sfax", "Topnet Agence Taib Mhiri Sfax"),
                               ("Topnet Agence El Mourouj", "Topnet Agence El Mourouj"),
                               ("Topnet Agence Gabes", "Topnet Agence Gabes")])