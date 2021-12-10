
from odoo import models, fields, api,_

class topnet_agence(models.Model):
    _name = 'topnet_agence.dossier'
    _description = 'topnet_agence.dossier'

    Nom = fields.Char(string="Nom", required=True)
