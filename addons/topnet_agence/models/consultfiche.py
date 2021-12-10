from odoo import models, fields, api

class topnet_agence(models.Model):
    _name = 'topnet_agence.consultfiche'
    _description = 'topnet_agence.consultfiche'

    segment = fields.Selection([("entreprise", "Entreprise"), ("autre", "Autre")], string="Segment", required=True)
    s_segment = fields.Char(string="Sous Segment", required=True)
    cat = fields.Selection([("standard", "Standard"), ("non standard", "Non standard")], string="Catégorie")
    charge = fields.Char(string="Chargé de compte", required=True)
    appel = fields.Integer(string="Appel Call Center")
    profil = fields.Char(string="Profil")
    statut = fields.Char(string="StatutRecouvrement")
    always = fields.Selection([("oui", "Oui"), ("non", "Non")], string="Always On")
    charge_adv = fields.Char(string="Chargé ADV")
    raison_soc = fields.Char(string="Raison Sociale", required=True)
    multi = fields.Selection([("oui", "Oui"), ("non", "Non")], string="Multi-sites")
    groupe = fields.Selection([("oui", "Oui"), ("non", "Non")], string="Groupe de société")
    effectif = fields.Integer(string="Effectif", required=True)
    contact_prin = fields.Char(string="Contact principal", required=True)
    contact_finan = fields.Char(string="Contact Financier", required=True)
    secteur = fields.Char(string="Secteur d'activité", required=True)
    fiscal = fields.Char(string="Matricule fiscal", required=True)
    chiffre = fields.Integer(string="Chiffre d'affaires annuel")
    exo = fields.Selection([("oui", "Oui"), ("non", "Non")], string="Exonération tva", required=True)
    rue = fields.Char(string="Rue", required=True)
    gouver = fields.Selection([("ariana", "Ariana"), ("beja", "Béja"), ("ben_Arous", "Ben Arous"), ("bizerte", "Bizerte"), ("gabes", "Gabés"), ("gafsa", "Gafsa"), ("jendouba", "Jendouba"), ("kairouan", "Kairouan"), ("kasserine", "Kasserine"), ("kébili", "Kébili"), ("le_Kef", "Le Kef"), ("mahdia", "Mahdia"), ("la_Manouba", "La Manouba"), ("mednine", "Médenine"), ("monastir", "Monastir"), ("nabeul", "Nabeul"), ("sfax", "Sfax"), ("sidi_Bouzid", "Sidi Bouzid"), ("siliana", "Siliana"), ("sousse", "Sousse"), ("tataouine", "Tataouine"), ("tozeur", "Tozeur"), ("tunis", "Tunis"), ("zaghouan", "Zaghouan")], required=True, string="Gouvernorat")
    local = fields.Char(string="Localité", required=True)
    ville = fields.Char(string="Ville", required=True)
    tel = fields.Char(string="Tél", required=True)
    gsm_fiche = fields.Char(string="GSM", required=True)
    mail_top = fields.Char(string="Email Topnet", required=True)
    compte = fields.Selection([("client", "Client"), ("autre", "Autre")], string="Type de compte", required=True)
    code_cli = fields.Integer(string="Code client")
    source = fields.Char(string="Source Prospect")
    ancien = fields.Integer(string="Ancien code client")
    frequence = fields.Integer(string="Fréquence", required=True)
    cat = fields.Char(string="Catégorie de systéme ", required=True)
    date_debut = fields.Date(string="Date de début d'activité ", required=True)
    contact_tech = fields.Char(string="Contact technique", required=True)
    contact_jurid = fields.Char(string="Contact juridique ", required=True)
    registre_com = fields.Char(string="Registre de commerce ", required=True)
    exo_timbre = fields.Selection([("non", "Non"), ("oui", "Oui")], string="Exonoration timbre", required=True)
    rue2 = fields.Char(string="Rue(2) ")
    delegatio = fields.Char(string="Délegation ", required=True)
    code_pos = fields.Integer(string="Code postal ", required=True)
    paysreg = fields.Char(string="Pays/Region")
    fax = fields.Integer(string="Fax ", required=True)
    gsm2 = fields.Integer(string="GSM 2", required=True)
    creation = fields.Selection([("non", "Non"), ("oui", "Oui")], string="Création nouveau email")





