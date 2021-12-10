from odoo import models, fields, api


class TopnetContact(models.Model):
     _name = 'topnet.contact'
     _description = 'Liste de contacts'

     name = fields.Char(string='Nom du contact', required=True)
     tel_fixe = fields.Char(string='Tel fixe',size=8, required=True)
     tel_gsm = fields.Char(string='Tel mobile',size=8, required=True)
     email =fields.Char(string='Email', required=True)
     nature = fields.Selection(
          [
               ('Commercial', 'Commercial'), 
               ('Technique', 'Technique'), 
               ('Administratif', 'Administratif'),
               ('Financier','Financier')
          ], 
          required=True, 
          default='Commercial'          
     )
     client_id = fields.Many2one('topnet.client','Client ID')
     