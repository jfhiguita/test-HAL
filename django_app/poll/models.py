"""Open questions models"""

from django.db import models

class Questions(models.Model):
    """Questions model."""
    question = models.TextField()

    def __str__(self):
        return f'{self.question}'




