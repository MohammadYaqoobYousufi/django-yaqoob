from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

# 1 - py manage.py makemigration members
# 2 - py manage.py migrate
# 3 - CRUD
# 4 - py manage.py shell
# 5 - 
