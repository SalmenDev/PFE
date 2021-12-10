from odoo import models, fields, api


class TopnetClient(models.Model):
     _name = 'topnet.client'
     #_inherit = ['res.users']
     _description = 'Topnet Clients'

     name = fields.Char(string='Nom', required=True)
     cin = fields.Integer(string='cin', required=True)
     raison = fields.Char(string='Raison Sociale', required=True)
     rc = fields.Char(string='Registre de Commerce', required=True)
     tva = fields.Char(string='Raison', required=True)
     exoneration = fields.Boolean(string='Exoneration', required=True)
     douane = fields.Char(string='Raison', required=True)
     activity = fields.Char(string='Raison', required=True)
     adresse_siege = fields.Text(string='Adresse Siege Sociale', required=True)
     ville_siege = fields.Integer(string='Ville du Siege', required=True)
     tel_siege = fields.Char(string='Tel Siege',size=8, required=True)
     adresse_facture = fields.Text(string='Adresse Facturation', required=True)
     ville_facture = fields.Integer(string='Ville Facturation', required=True)
     tel_facture = fields.Char(string='Tel Facturation',size=8, required=True)
     email =fields.Char(string='Email', required=True)
     contact_id = fields.One2many('topnet.contact','client_id', string='Contact ID')
     #ville_id = fields.many2one('topnet.ville','id')
     