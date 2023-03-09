from django.db import models
from django.contrib.auth import get_user_model


CATEGORY = [
    ('', 'Category'),
    ('Cartoon', 'Cartoon'),
    ('Documentary', 'Documentary'),
    ('Action', 'Action'),
]

User = get_user_model()


class Movies(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=100, choices=CATEGORY)

    class Meta:
        db_table = 'movies'
