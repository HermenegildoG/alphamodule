from odoo import api,fields,models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description="Patient records"

    name=fields.Char(string='Name',required=True)
    age=fields.Integer(string='Age')
    isChild = fields.Boolean(string = "Is Child?")
    notes=fields.Text(string="Description in notes")
    gender=fields.Selection([('male','Male'),('female','Female'),('others','Others')],string="Gender")

    @api.onchange('age')
    def _onChangeAge(self):
        if self.age <= 10:
            self.isChild = True
        else:
            self.isChild=False