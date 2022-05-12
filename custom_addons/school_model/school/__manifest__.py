{
    'name':'School',
    'version':'1.1',
    'author':'WebSchool',
    'summary':"school Management System",
    'sequence': 1,
    'description': "This is School Management Software suppored in "
                    "odoo V15",
    'category':"School_management",
    'website':'https://www.odoo.com/app/school',
    'depends':['base'],
    'data':[
        "data/school_data.xml",
        "security/security_access_data.xml",
        "security/ir.model.access.csv",
        "views/school_view.xml"
    ]
}