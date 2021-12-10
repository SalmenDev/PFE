# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
import re

class topnet_agence(models.Model):
    _name = 'topnet_agence.topnet_agence'
    _description = 'topnet_agence.topnet_agence'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'Nom'

    _sql_constraints = [
        ('email_uniq', 'unique(email)', 'Email id is unique change your custom email id'),
        ('num_cin_num_passeport_uniq', 'unique(num_cin_num_passeport)', 'Numero de cin/passeport existe déja'),
    ]

    @api.model
    def default_get(self, fields):
        res = super(topnet_agence, self).default_get(fields)
        res['Rôle'] = 'responsable agence'
        return res

    def action_confirm(self):
        for rec in self:
            rec.state = 'draft'


    Nom = fields.Char(string="Nom", required=True)
    prenom =fields.Char(string="Prénom", required=True)
    Adresse = fields.Char(string="Adresse", required=True)
    naissance = fields.Date(string="Date de naissance", required=True)
    num_cin_num_passeport = fields.Integer(string=" N°cin / N°passeport",required=True)
    matricule = fields.Char(string="Matricule", required=True)
    email = fields.Char(string="Email",required=True)
    Téléphone =fields.Integer(string="Téléphone")
    Rôle = fields.Selection([("administrateur","Administrateur"), ("responsable agence","Responsable agence"),("chef agence","Chef agence"), ("agent","Agent")],required=True)
    Agence = fields.Selection([("Topnet Agence centre urbain nord","Topnet Agence centre urbain nord"), ("Topnet Agence Tunis", "Topnet Agence Tunis"), ("Topnet Agence Bardo", "Topnet Agence Bardo"), ("Topnet Agence Ennasr", "Topnet Agence Ennasr"), ("Topnet Agence La Marsa", "Topnet Agence La Marsa"), ("Topnet Agence Le Passage", "Topnet Agence Le Passage"), ("Topnet Agence Bizerte", "Topnet Agence Bizerte"), ("Topnet Agence Nabeul", "Topnet Agence Nabeul"), ("Topnet Agence Khzema", "Topnet Agence Khzema"), ("Topnet Agence Sousse", "Topnet Agence Sousse"), ("Topnet Agence Monastir", "Topnet Agence Monastir"), ("Topnet Agence Sfax", "Topnet Agence Sfax"), ("Topnet Agence Taib Mhiri Sfax", "Topnet Agence Taib Mhiri Sfax"), ("Topnet Agence El Mourouj", "Topnet Agence El Mourouj"), ("Topnet Agence Gabes", "Topnet Agence Gabes")])
    image = fields.Image(string="Télécharger une image", max_width=90, max_height=90, verify_resolution=True)
#    Agence_id = fields.Many2one('agence.agence',
#                                ondelete='set null', string="Agence", index=True)
    active = fields.Boolean(string="Active", default="Ture")
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('done', 'Done'),
    ], string='Status', readonly=True, default='draft')

    @api.constrains('Téléphone', 'num_cin_num_passeport', 'Nom', 'prenom')
    def check_Téléphone(self):
      for rec in self:
        if len(str(abs(self.Téléphone))) != 8:
            raise ValidationError(_('Numéro de tel doit contenir seulement 8 chiffres'))
        elif len(str(abs(self.num_cin_num_passeport))) != 8:
            raise ValidationError(_('Nméro de cin / passeport doit contenir seulement 8 chiffres'))
        elif len(self.Nom) > 20:
            raise ValidationError(_('Nom trop long'))
        elif len(self.prenom) > 20:
            raise ValidationError(_('Prénom trop long'))

    @api.constrains('email')
    def validate_email(self):
      for obj in self:
       if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",obj.email) == None:
        raise ValidationError("Vérifier votre adresse mail : %s" % obj.email)
        return True









#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
