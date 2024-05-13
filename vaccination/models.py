from django.db import models
from campaign.models import Campaign,Slot
from django.contrib.auth.models import User


# Create your models here.


class Vaccination(models.Model):
    patient=models.ForeignKey(User,related_name='patient',on_delete=models.CASCADE)
    campaign=models.ForeignKey(Campaign,related_name='campaign',on_delete=models.CASCADE)
    slots=models.ManyToManyField(Slot,related_name='slots',blank=True)
    date=models.DateField(null=True,blank=True)
    is_vaccinated=models.BooleanField(default=False)
    updated_date=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.get_full_name() + " | " + str(self.campaign.vaccine.name)

