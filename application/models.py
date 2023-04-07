from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255,blank=True, null=True)
    
    
    def __str__(self):
        return self.name


class Product(models.Model):
    asin = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.asin

    class Meta:
        verbose_name_plural = 'products'

class Review(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True)
    reviewTime = models.CharField(max_length=50,blank=True, null=True)
    reviewerID = models.CharField(max_length=20,blank=True, null=True)
    reviewerName = models.CharField(max_length=50, blank=True, null=True)
    reviewText = models.TextField(blank=True, null=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    unixReviewTime = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    asin= models.CharField(max_length=100, blank=True, null=True)
    
    
    image = models.CharField(max_length=500, blank=True, null=True)
    vote = models.IntegerField(blank=True, null=True)
    style = models.JSONField(blank=True, null=True)


    def save(self, *args, **kwargs):
        # Set the product based on the asin
        if self.asin:
            self.product = Product.objects.filter(asin=self.asin).first()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.reviewerName



class Setup(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
            
    def __str__(self):
        return self.name


class Keyword(models.Model):
    setup = models.ForeignKey(Setup, on_delete=models.CASCADE, blank=True, null=True)
    key_adj = models.CharField(max_length=50, blank=True, null=True)
         
    def __str__(self):
        return self.key_adj

class Rating(models.Model):
    product = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=50)
    rating = models.FloatField()
    timestamp = models.DateTimeField()
    def __str__(self):
        return self.rating    
     