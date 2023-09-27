from odoo import fields, models

class Estate(models.Model): 
	_name = "real_estate"
	_description = "Estate Management"

	name = fields.Char("Name", default="Unknown")
	last_seen = fields.Datetime("Last Seen", default= lambda self: fields.Datetime.now())
	bedrooms = fields.Integer("Number of bedrooms", default=2)
	selling_price = fields.Monetary("Selling Price", readonly=True)
	availability_date = fields.Datetime("Availability date")