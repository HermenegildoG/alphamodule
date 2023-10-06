from odoo import api,fields,models


class ClaseAlpha(models.Model):
    _name = 'alpha.clase_alpha'
    _description = 'Clase Alpha'

    nombre = fields.Char(string='Nombre de la Clase', required=True)
    ubicacion = fields.Char(string="Ubicacion del alpha donde será impartida la clase")
    usuarios_ids = fields.Many2many('res.users', string='Usuarios', limit=2)

class Usuario(models.Model):
    _inherit = 'res.users'

    nombre = fields.Char(string='Nombre del usuario', required=True)

    clase_alpha_id = fields.Many2one('alpha.clase_alpha', string='Clase Alpha')



