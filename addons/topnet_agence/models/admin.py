# -*- coding: utf-8 -*-
from odoo import models, fields, api


class topnet_agence(models.Model):
    _name = 'topnet_agence.admin'
    _description = 'topnet_agence.admin'

    user_id = fields.Many2one('res.user',
                              ondelete='set null', string="User", index=True)
    nom = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    adresse = fields.Char(string="Adresse", required=True)
    naissance = fields.Date(string="Date de naissance", required=True)
    num_cin_num_passeport = fields.Integer(string=" N°cin / N°passeport", required=True)
    matricule = fields.Char(string="Matricule", required=True)
    email = fields.Char(string="Email", required=True)
    telephone = fields.Integer(string="Téléphone")
    role = fields.Selection([("administrateur", "Administrateur"), ("responsable agences", "Responsable agences"),
                             ("chef agence", "Chef agence"), ("agent", "Agent")], required=True)
    agence = fields.Selection([("Topnet Agence centre urbain nord", "Topnet Agence centre urbain nord"),
                               ("Topnet Agence Tunis", "Topnet Agence Tunis"),
                               ("Topnet Agence Bardo", "Topnet Agence Bardo"),
                               ("Topnet Agence Ennasr", "Topnet Agence Ennasr"),
                               ("Topnet Agence La Marsa", "Topnet Agence La Marsa"),
                               ("Topnet Agence Le Passage", "Topnet Agence Le Passage"),
                               ("Topnet Agence Bizerte", "Topnet Agence Bizerte"),
                               ("Topnet Agence Nabeul", "Topnet Agence Nabeul"),
                               ("Topnet Agence Khzema", "Topnet Agence Khzema"),
                               ("Topnet Agence Sousse", "Topnet Agence Sousse"),
                               ("Topnet Agence Monastir", "Topnet Agence Monastir"),
                               ("Topnet Agence Sfax", "Topnet Agence Sfax"),
                               ("Topnet Agence Taib Mhiri Sfax", "Topnet Agence Taib Mhiri Sfax"),
                               ("Topnet Agence El Mourouj", "Topnet Agence El Mourouj"),
                               ("Topnet Agence Gabes", "Topnet Agence Gabes")])
    active = fields.Boolean("Active", default=True)

    @api.model
    def create(self, values):
        vals_user = {
            'name': values.get('nom'),
            'login': values.get('email'),
            # other required field
        }
        user_id = self.env['res.users'].sudo().create(vals_user)
        values.update(user_id=user_id.id)
        res = super(topnet_agence, self).create(values)

        return res
