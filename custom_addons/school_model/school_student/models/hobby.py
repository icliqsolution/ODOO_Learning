# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# from random import randint

from odoo import fields, models

class hobbies(models.Model):
    _name = "hobby"

    name = fields.Char("Hobby")

# class StudentHobby(models.Model):

#     _name = "student.hobby"
#     _description = "student hobby"

    # def _get_default_color(self):
    #     return randint(1, 11)

    # name = fields.Char(string="Student Hobby", required=True)

    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', "Tag name already exists !"),
    # ]
