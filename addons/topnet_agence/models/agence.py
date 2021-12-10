# -*- coding: utf-8 -*-

from odoo import models, fields


class topnet_agence(models.Model):
    _name = 'topnet_agence.agence'
    _description = 'topnet_agence.agence'

    Nom = fields.Char(string="Nom", required=True)
    Adresse = fields.Char(string="Adresse", required=True)
    Ville = fields.Selection([("ariana", "Ariana"), ("beja", "Béja"), ("ben_Arous", "Ben Arous"), ("bizerte", "Bizerte"), ("gabes", "Gabés"), ("gafsa", "Gafsa"), ("jendouba", "Jendouba"), ("kairouan", "Kairouan"), ("kasserine", "Kasserine"), ("kébili", "Kébili"), ("le_Kef", "Le Kef"), ("mahdia", "Mahdia"), ("la_Manouba", "La Manouba"), ("mednine", "Médenine"), ("monastir", "Monastir"), ("nabeul", "Nabeul"), ("sfax", "Sfax"), ("sidi_Bouzid", "Sidi Bouzid"), ("siliana", "Siliana"), ("sousse", "Sousse"), ("tataouine", "Tataouine"), ("tozeur", "Tozeur"), ("tunis", "Tunis"), ("zaghouan", "Zaghouan")], required=True, string="Ville")
    Fax = fields.Integer(string="Fax")



