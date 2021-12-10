# -*- coding: utf-8 -*-

from odoo import models, fields, api

class historique(models.Model):
    _name = 'topnet_agence.historique'
    _description = 'topnet_agence.historique'

    date = fields.Date(string="Date de prise en charge", required="True")
    agent = fields.Char(string="Agent Commerciale", required="True")