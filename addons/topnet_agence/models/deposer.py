# -*- coding: utf-8 -*-
from odoo import models, fields, api


class topnet_agence(models.Model):
    _name = 'topnet_agence.deposer'
    _description = 'topnet_agence.deposer'

    doc = fields.Image(string="Registre de commerce", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc2 = fields.Image(string="CIN gérant", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc3 = fields.Image(string="Contrat TOPNET", max_width=90, max_height=90, verify_resolution=True, required=True)
    doc4 = fields.Image(string="Contrat TT", max_width=90, max_height=90, verify_resolution=True, required=True)



