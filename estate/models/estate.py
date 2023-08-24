from odoo import fields, models

class Estate(models.Model): 
	_name ="res.estate"
	_description ="Estate Management"

	name = fields.Char()