# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Doc(models.Model):
	_name = 'doc.doc'
	_description = 'Document'
	_inherit = ['mail.thread']


	#Add Fields:
	name = fields.Char('Create folder Name')
	description = fields.Char('Description')
	content = fields.Html('Content')
	file = fields.Binary('File')
	created_date = fields.Date('Created Date')
	created_by = fields.Char('Created By')
	color = fields.Integer()
	

	


