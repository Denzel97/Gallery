from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

class Image(models.Model):
    title = models.CharField(max_length=30, unique=True)
    location_name = models.ForeignKey(Location)
    category_name = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_name = models.ImageField(upload_to = 'images/', null=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod
    def search_category(cls,search_term):
        search_result = cls.objects.filter(category_name__category_name__icontains=search_term)
        return search_result

    @classmethod
    def filter_location(cls,location):
        filter_loc = cls.objects.filter(image_location__location_name__icontains=location)
        return filter_loc

    @classmethod
    def get_image_by_id(cls,input_id):
        image_got = cls.objects.get(id=input_id)
        return image_got
