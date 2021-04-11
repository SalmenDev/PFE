from odoo import models, fields, api

class TopnetUser(models.Model):
     _name = 'topnet.user'
     _description = 'topnet BackOffice users'

     name = fields.Char(string='Name', required=True)
     
     gender = fields.Selection(
          [
               ('male', 'Homme'), 
               ('female', 'Femme'), 
               ('other', 'Autre')
          ], 
          required=True, 
          default='other'          
     )
     cin = fields.Integer(string='cin', required=True)
     email =fields.Char(string='Email', required=True)
     password =fields.Char(string='Password', required=True)
     
