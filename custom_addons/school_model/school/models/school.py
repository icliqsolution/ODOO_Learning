
from termios import VLNEXT
from unicodedata import name
from odoo import fields, models,api
import random

class SchoolProfile(models.Model):
    _name = "school.profile"
    # _rec_name = 'email' # display name
    # _order = 'name'  # sort a all record display
    _log_access = False # using auto data create stop like this uid, create datetime .....


    school_seq_name = fields.Char("school Code")
    name = fields.Char(string="school name", help='This is a school name ',size=20, required=True, default="SCHOOL NAME", index=True, trim=False)
    email = fields.Char(string="email")
    phone = fields.Char("phone", size=10)
    is_virtual_class = fields.Boolean(string="Virtual class support?", readonly=True)
    currency_id = fields.Many2one("res.currency", string="currency_id")
    result = fields.Float(string="Result", readonly=True)
    school_result = fields.Integer(string="School Result ", request=True, readonly=True)
    address = fields.Text(string="School Address", help='this file is write school address', trim=False)
    estalish_date = fields.Date(string="Estalish Date")
    open_date = fields.Datetime("open DataTime", default=fields.Datetime.now())
    school_type = fields.Selection([("public","Public School"),("private","Private School")])
    document = fields.Binary(string= "Documents", help="This file is download")
    document_name = fields.Char(string="File Name")
    upload_image = fields.Image(string="Upload Image School", max_width=100,max_height=100)
    school_discription = fields.Html(string="Description")
    auto_rank = fields.Float(compute="_auto_rank_populate", string="Auto Rank", store=True)

    _sql_constraints = [
        ('name_unique','unique (name)',"Please enter unique school name, Given school name already exists.")
    ]

    @api.depends("school_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    # How to generate sequence in Odoo - Auto sequence generate using ir.sequence
    @api.model
    def create(self,vals):
        print("School Profile Create Vals",vals)
        vals['school_seq_name'] = self.env['ir.sequence'].next_by_code("school.profile")
        return super(SchoolProfile,self).create(vals)


    # use name_get method in Odoo | Odoo ORM Methods. Show out put in School_student

    # def name_get(self):
    #     student_list = []
    #     for school in self:
    #         name = school.name
    #         if school.school_type:
    #             name += "({})".format(school.school_type)
    #     student_list.append((school.id, name))
    #     return student_list

# Seq Purpose
class TestSeqPurpose(models.Model):
    _name= "test.seq.purpose"

    name= fields.Char("Name")

@api.model
def create(self,vals):
    print("School Profile vals",vals)
    return super(SchoolProfile, self).create(vals)

def write(self,vals):
    print("School Profile vals",vals)
    return super(SchoolProfile, self).create(vals)


def specialcommand(self):
        student_obj =self.env['school_student.school_student']
        stud_id = student_obj.create({'name':"newStudent two",'school_id':self.id})


# specialcommand 0 , 0

def specialcommand(self):
    # First Way to create Chiled module for existing parent model.
    student_obj = self.env['school_student.school_student']
    stud_id = student_obj.create({'name':"Student ONE", 'school_id':self.id})

    # parent model and child model.
    # school_id = self.create({"name":"kapil sharma show"})
    # student_obj.create({"name":"kapil sharma 1", "school_id":school_id.id})
    # student_obj.create({"name":"kapil sharma 2", "school_id":school_id.id})
    # student_obj.create({"name":"kapil sharma 3", "school_id":school_id.id})
    # student_obj.create({"name":"kapil sharma 4", "school_id":school_id.id})
    # student_obj.create({"name":"kapil sharma 5", "school_id":school_id.id})


# def specialCommand1(self):
#     for student in self.school_list:
#         student.name = student.name + " " + str(student.id)
#         student.total_fees = 3600
#         student.student_fees = 12000


class SchoolStudentProfile(models.Model):
    _name = "school.student.profile.security.example"
    _description = "This is the demo of access rights tutorial."

    name= fields.Char("Name")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    