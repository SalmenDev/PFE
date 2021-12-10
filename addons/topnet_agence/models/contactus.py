# -*- coding: utf-8 -*-

from odoo import models, fields


class topnet_agence(models.Model):
    _name = 'topnet_agence.contactus'
    _description = 'topnet_agence.contactus'

    service = fields.Selection([("service technique", "Service Technique"), ("service commerciale", "Service Commercial")])
    nom = fields.Char(string="Nom", required="True")
    prenom = fields.Char(string="Prénom", required="True")
    email = fields.Char(string="Email", required="True")
    tel = fields.Integer(string="Tél", required="True")
    objet = fields.Char(string="Objet", required="True")
    fax = fields.Integer(string="Fax", required="True")
    mobile = fields.Integer(string="Mobile", required="True")
    message = fields.Char(string="Message", required="True")

