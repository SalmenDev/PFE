# -*- coding: utf-8 -*-

from odoo import models, fields


class topnet_agence(models.Model):
    _name = 'topnet_agence.modif_agence'
    _description = 'topnet_agence.modif_agence'

    Nom = fields.Char(string="Nom", required=True)
    Adresse = fields.Char(string="Adresse", required=True)
    Ville = fields.Char(string="Ville", required=True)
    Fax = fields.Integer(string="Fax")



