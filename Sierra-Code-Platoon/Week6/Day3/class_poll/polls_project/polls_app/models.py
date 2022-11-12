from django.db import models

# Create your models here.

# question
#  choice

class Question(models.Model):
    question_text = models.CharField(max_length= 255)
    pub_date = models.DateTimeField('date published')
    # choice_set will exist
    
    def __str__(self):
        return f"Question: {self.question_text}"
    
    
class Choice(models.Model):
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return f"Choice: {self.choice_text}"
    
#relationships

# one to one = use models.OnetoOneField on either model
# one to many = use models.foreignKey on the 'many side
# many to many = use models.ManyToManyField on either side

