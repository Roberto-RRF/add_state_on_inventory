from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'



    estado = fields.Char(
        string="Estado Rep", 
        compute="_compute_estado", 
        store=True
    )

    def _compute_estado(self):
        for picking in self:
            picking.estado = picking.partner_id.state_id.name if picking.partner_id else ''