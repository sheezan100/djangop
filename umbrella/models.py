from django.db import models


class Umbrella_dep(models.Model):

  department=models.CharField(max_length=250)

  def __str__(self):
       return self.department

class Sub_department(models.Model):

    umbrella_b = models.ForeignKey(Umbrella_dep, on_delete=models.CASCADE)
    technology=models.CharField(max_length=40, default='SOME STRING')

    def __str__(self):
        return self.technology

class D_employee(models.Model):

        sub_department = models.ForeignKey(Sub_department, on_delete=models.CASCADE)

        name=models.CharField(max_length=250)
        age=models.CharField(max_length=20)
        mobile_no=models.CharField(max_length=20)
