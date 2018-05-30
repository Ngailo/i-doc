# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Doc(models.Model):
	_name = 'doc.doc'
	_description = 'Document'
	_inherit = ['mail.thread']
	_order = 'sequence,id'


	#Add Fields:
	name = fields.Char('Create folder Name')
	description = fields.Char('Description')
	content = fields.Html('Content')
	file = fields.Binary('File')
	created_date = fields.Date('Created Date')
	created_by = fields.Char('Created By')
	color = fields.Integer()
	sequence = fields.Integer(default=0)
	name_count = fields.Integer(string="Number of Folder", compute="_get_name_count")

	_sql_constraints = [
		('name_description_check',
		 'CHECK(name != description)',
		 "The name of the folder should not be the description!!!"),

		('name_unique',
		 'UNIQUE(name)',
		 "The folder name is already exist!!! "),
	]

	@api.depends('name')
	def _get_name_count(self):
		for r in self:
			r.name_count = len(r.name)





	

	


