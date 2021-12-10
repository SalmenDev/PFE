# -*- coding: utf-8 -*-
from odoo import models, fields


class topnet_agence(models.Model):
    _name = 'topnet_agence.modifier'
    _description = 'topnet_agence.modifier'

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
