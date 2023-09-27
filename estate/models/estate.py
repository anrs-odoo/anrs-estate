from odoo import fields, models
from dateutil.relativedelta import relativedelta

class Estate(models.Model): 
	_name = "real_estate"
	_description = "Estate Management"

	name = fields.Char("Name", default="Unknown")
	last_seen = fields.Datetime("Last Seen", default= lambda self: fields.Datetime.now())
	bedrooms = fields.Integer("Number of bedrooms", default=2)
	selling_price = fields.Float("Selling Price", readonly=True, copy=False)
	availability_date = fields.Date("Availability date", default=lambda self: fields.datetime.today() + relativedelta(months=3),copy=False)
	active = fields.Boolean(default=True)