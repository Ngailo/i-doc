# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Dms(models.Model):
    _name = 'dms.dms'
    _description = 'Document'
    _parent_name = "parent_id"
    _parent_store = True
    _inherit = ['mail.thread']

    parent_id = fields.Many2one('dms.dms', 'Parent', ondelete='cascade')
    parent_left = fields.Integer('Parent Left', index=True)
    parent_right = fields.Integer('Parent Right', index=True)
    child_ids = fields.One2many('dms.dms', 'parent_id', 'Child')
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=0)
    full_name = fields.Char('Full Name', compute='_compute_full_name')
    color = fields.Integer()
    name = fields.Char('Folder Name', required=True)
    description = fields.Char('Description')
    child_count = fields.Integer(compute='_compute_child_count', string='Child')
    parent_full_name = fields.Char("Path", related='parent_id.full_name')


    _constraints = [
        (models.BaseModel._check_recursion, 'Parent already recursive!', ['parent_id'])
    ]

    _sql_constraints = [
        ('parent_id_name_uniq', 'unique(parent_id, name)', 'Name already exists!'),
    ]

    @api.multi
    def _compute_child_count(self):
        relative_field = self._fields.get("child_ids")
        comodel_name = relative_field.comodel_name
        inverse_name = relative_field.inverse_name
        count_data = self.env[comodel_name].read_group([(inverse_name, 'in', self.ids)], [inverse_name], [inverse_name])
        mapped_data = dict(
            [(count_item[inverse_name][0], count_item['%s_count' % inverse_name]) for count_item in count_data])
        for record in self:
            record.child_count = mapped_data.get(record.id, 0)

    @api.multi
    def name_get(self):
        if self.env.context.get('display_full_name', False):
            pass
        else:
            return super(Dms, self).name_get()

        def get_names(record):
            res = []
            while record:
                res.append(record.name or '')
                record = record.parent_id
            return res

        return [(record.id, " / ".join(reversed(get_names(record)))) for record in self]

    @api.multi
    def _compute_full_name(self):
        res_dict = dict(self.with_context({'display_full_name': True}).name_get())
        for record in self:
            record.full_name = res_dict.get(record.id, "")

    @api.one
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default.update(name=_("%s (copy)") % (self.name or ''))
        return super(Dms, self).copy(default)

    @api.multi
    def action(self):
        self.ensure_one()
        context = self.env.context
        action_id = context.get('module_action_id')
        if action_id:
            action_dict = self.env.ref(action_id).read([
                "type", "res_model", "view_type", "view_mode", "domain"
            ])[0]
            action_dict["name"] = self.name
        return action_dict



