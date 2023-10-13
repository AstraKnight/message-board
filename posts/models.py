from django.db import models

# Create your models here:
# create a new database model called Post:
# it has the database field text. 
# We’ve also specified the type of content it will hold, TextField().


# To store the textual content of a message board post
class Post(models.Model):  # new
    text = models.TextField()

    # Make your post more descriptive:
    def __str__(self):  # new
        return self.text[:50]