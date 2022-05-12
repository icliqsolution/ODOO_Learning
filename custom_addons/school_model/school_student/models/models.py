# -*- coding: utf-8 -*-

# from attr import field

# import string
# from unicodedata import name
# from numpy import record
# import encodings
# from pydoc import doc
# import re
from sre_parse import State
import string
from odoo import models, fields, api,_
from lxml import etree
from odoo.exceptions import UserError
import random


class Partner(models.Model):
    _inherit = "res.partner"

    def hello_hook(self):
        print("hello hook")
        for contacts in self.search([]):
            print(contacts.display_name)


# Create model name with different table name using _name and _table attribute metadata in Odoo

class student_test_fees(models.Model):
    _name = "student.test.fees"
    _table = "student_fees_testing"

    name = fields.Char(string="Fees")

# OR second method.
class student_test(models.Model):
    _name = "student.test"

    name = fields.Char(string="Test")

class Address(models.Model):
    _name = "address"
    _rec_name = "street"

    street = fields.Char("Street")
    street_one = fields.Char("Street2")
    city = fields.Char("City")
    state = fields.Char("State")
    country = fields.Char("Country")
    zip_code = fields.Char("Zip Code") 

class school_student(models.Model):
    _name = 'school_student.school_student'
    _inherit = "address"
    _description = 'school_student.school_student'
    _order = "student_seq"

    state=fields.Selection([('draft','Draft'),
                            ('progress','Progress'),
                            ('paid','Paid'),
                            ('done','Done')], string="State")
    student_seq = fields.Integer("Student Sequence")
    roll_number = fields.Char("Roll Number")
    name = fields.Char()
    school_id = fields.Many2one("school.profile",string="School",
                                #  domain = "[('school_type','=','public'),('is_virtual_class','=','True')]"
                                
                                # domain = [('currency_id','=','EUR')]
                                )

    currency_id = fields.Many2one("res.currency", string="currency_id")
    student_fees = fields.Monetary(string="student Fees")
    total_fees = fields.Float(string="Total fees")
    bday = fields.Date(string="Birthdate")
    ref_id = fields.Reference([('school.profile','School'),('account.move','Invice')], string="Reference Field")
    active = fields.Boolean(string="Active",default=True)
    hobby_list = fields.Many2many('hobby', string="Hobby")
    student_img = fields.Image()

    _sql_constraints = [('unique_name','unique(name)','Please provide other student name.Given name already exitss.'),
                        ('total_fees_check', 'check(total_fees >100)', 'minimum 101 amount allow.')
                        ]


    def buttonClickEvent(self):


        raise UserError (_("You click this button..."))

    @api.model
    def _change_roll_number(self):
        # """This method is used to add roll number to the student profile."""
        for stud in self.search([('roll_number','=',False)]):
            stud.roll_number = "STU" +str(stud.id)

    # Wizard created sapoted this function.

    def wiz_open(self):
        
        # return self.env['ir.actions.act_window']._for_xml_id("school_student_school_student.student_fees_update_action")
            # OR
        return{'type': 'ir.actions.act_window',
                'res_model': 'student.fees.update.wizard',
                'view_mode': 'form',
                'target': 'new'}

    # BUtton function with open ui part.
    def custom_button(self):
        print("This is a custom button methods calls by you ... ")
        return {
            'type':'ir.actions.act_url',
            'url':'/contactus',
            'url':'https://www.google.com',         
            # 'target':'self'
        }
        # return "https://www.google.com"
        # self.total_fees = random.randint(1,1000)
        # self.custom_new_method(random.randint(1,1000))
        # print(random, type(random))


    def custom_new_method(self, total_fees):
        self.total_fees = total_fees

    @api.model
    def create(self, values): 
        print("school student create values", values)
        return super(school_student,self).create(values)

    # How to use fields_view_get method in Odoo | Odoo ORM Methods
    
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):

    #     res = super(school_student, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
    #     if view_type == 'form':
    #         doc = etree.XML(res['arch'])
    #         name_field = doc.xpath("//field[@name='name']")
    #         if name_field:
    #             # Added one label in form view
    #             name_field[0].addnext(etree.Element('label',{'string':"Hello This is a custom label form field_view_get method"}))
                
    #         fees_field = doc.xpath("//field[@name='student_fees']")
    #         if fees_field:
    #             fees_field[0].set("string","Hello This  Is School Fees.")
    #             fees_field[0].set("nolable","0")
    #         res['arch'] = etree.tostring(doc, encoding='unicode')

    #     if view_type == 'tree':
    #         doc = etree.XML(res['arch'])
    #         school_field = doc.xpath("//field[@name = 'school_id']")
    #         if school_field:
    #             # Added one field in tree view
    #             school_field[0].addnext(etree.Element('field',{'string':'Total Fee', 'name': 'total_fees'}))
    #         res['arch'] = etree.tostring(doc, encoding='unicode')
    #     return res

    def write(self, vals):
        print("-------------",vals)
        rtn = super(school_student,self).write(vals)
        print("----------------eeeeeeeeeer----",rtn)
        return rtn

    def copy(self, default=None):
        return super(school_student,self).copy(default)

    def unlink(self):
        return super(school_student,self).unlink()

class SchoolProfile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school_student.school_student","school_id",string="school_list")

    # view_search method.
    
    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):

    #     args = args or []
    #     print("Name",name)
    #     print("Args", args)
    #     print("operator", operator)
    #     print("limit",limit)
    #     if name:
    #         records = self.search(['|','|',('name', operator, name), ('email', operator, name), ('school_type', operator, name)])
    #         return records.name_get()
    #     return self.search([('name', operator,name)]+args, limit=limit).name_get()

    # @api.model
    # def _name_search(self,name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     args = args or []
    #     print("Name",name)
    #     print("Args",args)
    #     print("Operators",operator)
    #     print("limit",limit)
    #     if name:
    #         domain =['|','|',('name', operator, name),('email', operator, name),('school_type', operator, name)]
    #     school_ids = self.search(domain+args, limit=limit)
    #     return school_ids.name_get()

    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100



class Partner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        return super(Partner,self).create(vals)

# inherit module function type 1
class SchoolStudent(models.Model):
    _inherit = 'school_student.school_student'

    parent_name = fields.Char("Parent Name")


# Extend inherit module function type 3

class Car(models.Model):
    _name="car"

    name = fields.Char("Car Name")
    price = fields.Float("Cost")

class CarEngine(models.Model):
    _name = "car.engine"
    _inherits = {"car":"car_id"}

    name = fields.Char("Car Engine Name")
    car_id = fields.Many2one("car",string="Car")

# class hobbies(models.Model):
#     _name = "hobby"

#     name = fields.Char("Hobby")
