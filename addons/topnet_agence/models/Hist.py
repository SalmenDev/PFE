# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class historique(models.Model):
    _name = 'topnet_agence.hist'
    _description = 'topnet_agence.hist'

    Date_prise = fields.Date(string="Date de prise en charge", required="True")
    Agent_commerciale = fields.Char(string="Agent Commerciale", required="True")