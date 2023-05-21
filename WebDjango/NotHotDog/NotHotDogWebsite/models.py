from django.db import models
from faker import Faker
from random import uniform

# Create your models here.
class Doc(models.Model):
  upload = models.ImageField(upload_to='images/')
  
  def __str__(self):
    return str(self.pk)
  
class Predictions(models.Model):
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE)
    prediction = models.BooleanField()
    conformity = models.BooleanField()
    t_response = models.IntegerField()
    probability = models.DecimalField(max_digits=5, decimal_places=2)
    error = models.FloatField()

fake = Faker()

def create_fake_docs():
    for _ in range(100):
        upload = fake.file_name(extension='jpg')  # Example field from the Doc model
        Doc.objects.create(upload=upload)

create_fake_docs()

def create_fake_predictions():
    for _ in range(100):
        doc = Doc.objects.order_by('?').first()  # Get a random Doc instance
        prediction = fake.boolean()
        conformity = fake.boolean()
        t_response = fake.random_int(min=1, max=60)
        probability = round(uniform(0, 100), 2)
        error = uniform(0, 1)
        Predictions.objects.create(
            doc=doc,
            prediction=prediction,
            conformity=conformity,
            t_response=t_response,
            probability=probability,
            error=error
        )

create_fake_predictions()


