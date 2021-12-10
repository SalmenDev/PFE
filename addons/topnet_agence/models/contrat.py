# -*- coding: utf-8 -*-
from odoo import models, fields, api


class topnet_agence(models.Model):
    _name = 'topnet_agence.contrat'
    _description = 'topnet_agence.contrat'

    doc = fields.Image(string="Contrat TOPNET", max_width=90, max_height=90, verify_resolution=True, required=True)
