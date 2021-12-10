from odoo import models, fields, api

class TopnetVille(models.Model):
     _name = 'topnet.ville'
     _description = 'Liste des villes'
     

     name = fields.Char(string='Nom du ville', required=True)
     postal = fields.Integer(string='Code Postal', required=True)
     gov_id = fields.Many2one('topnet.gouvernorat', string='Gouvernorat ID')
