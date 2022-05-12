# -*- coding: utf-8 -*-

# import string
from odoo import models, fields, api, _, tools


class dynamic_view(models.Model):
    _name = 'dynamic_view.dynamic_view'
    _description = 'student and school dynamic'
    _auto = False

    school_name = fields.Char("School Name")
    school_phone = fields.Char("School Phone")
    school_email = fields.Char("School Email")
    school_type = fields.Selection([("public","Public School"),("private","Private School")], string="Type Of School")

    student_name = fields.Char("School Name")
    student_rno = fields.Char("School Name")
    student_fees = fields.Float(string="student Fees")
    student_seq = fields.Integer("Student Sequence")

    def init(self):
            tools.drop_view_if_exists(self.env.cr,self._table)
            self.env.cr.execute("""
            create or replace view {} as (    
                select std.id as id,
                std.roll_number as student_rno,
                std.name as student_name,
                std.student_fees as student_fees,
                std.student_seq,
                sp.name as school_name,
                sp.email as school_email,
                sp.phone as school_phone,
                sp.school_type as school_type
                from school_student_school_student as std join school_profile as sp on std.school_id=sp.id)
            """.format(self._table))



    # def init(self):
    #     tools.drop_view_if_exists(self.env.cr, self._table)
    #     self.env.cr.execute(""" Select std.id,
    #                             std.rno as roll_number,
    #                             std.student_fees as student_fees,
    #                             from school_student as std""".format(self._table)) 



    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
