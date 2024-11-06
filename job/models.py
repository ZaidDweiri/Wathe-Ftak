from django.db import models

# Create your models here.
JOB_TYPE = (
    ('FULL TIME','FULL TIME '),
    ('PART TIME','PART TIME '),
)
class category(models.Model):
        name = models.CharField(max_length=20)
        def __str__(self):
            return self.name

def upload_Image(instance, filename):
    imagename , extension = filename.split(".")
    return "Jobs/{filename}".format(filename=filename)
class job(models.Model):
    title = models.CharField(max_length=20)
    job_type = models.CharField(max_length=20, choices= JOB_TYPE)
    description = models.TextField(max_length=1200)
    published_at = models.DateTimeField(auto_now_add=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=300)
    experiences = models.IntegerField(default=0)
    catgory = models.ForeignKey(category, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='images/', null=True, blank=True)

    #location

    def __str__(self):
        return self.title