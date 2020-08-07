from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author,
                                     related_name='books',
                                     blank=True,
                                     default='')
    published_date = models.CharField(max_length=10)
    categories = models.ManyToManyField(Category,
                                        related_name='books',
                                        blank=True,
                                        default='')
    average_rating = models.PositiveSmallIntegerField()
    ratings_count = models.PositiveIntegerField()
    thumbnail = models.URLField()

    def __str__(self):
        authors = ', '.join([author.name for author in self.authors.all()])
        return f'{self.title} by {authors}'
