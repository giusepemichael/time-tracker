from django.db import models
from django.utils import timezone

class Employees(models.Model):

            emp_id = models.CharField(max_length=300)
            password=models.CharField(max_length=10)
            fname = models.CharField(max_length=300)
            lname = models.CharField(max_length=300, null=True)
            check_in = models.DateTimeField(
                default=timezone.now)
            log_user = models.DateTimeField(
                default=timezone.now)


            def checkin(self):
                self.checkin = timezone.now()
                self.save()


            def __str__(self):
                return self.emp_id

class Admin(models.Model):

            user_id=models.ForeignKey('Employees', on_delete=models.CASCADE)
            shift_len=models.CharField(max_length=200)
