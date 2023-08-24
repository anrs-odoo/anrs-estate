from odoo import fields, models

class Estate(models.Model): 
	_name ="real_estate"
	_description ="Estate Management"

	name = fields.Char()