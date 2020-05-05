from django.db import models
from django.utils import timezone

class Dream(models.Model):
    dream = models.CharField(max_length=500)
    date_created = models.DateTimeField(editable=False)
    date_modified = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        return super(Dream, self).save(*args, **kwargs)    
    
    class Meta:
        verbose_name = "Dream"
        verbose_name_plural = "Dreams"
    def __str__(self):
        return self.dream