# -*- coding: utf-8 -*-
from odoo import fields, models

class Client(models.Model):
    _inherit = 'res.partner'


    agence_ids = fields.Many2many('topnet_agence.topnet_agence',
        string="Clients", readonly=True)