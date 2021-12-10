from odoo import models, fields, api


class TopnetGouvernorat(models.Model):
     _name = 'topnet.gouvernorat'
     _description = 'Liste des Gouvernorats'

     name = fields.Char(string='Nom du Gouvernorat', required=True)
     ville_id = fields.One2many('topnet.ville', 'gov_id' , string ='Ville ID')