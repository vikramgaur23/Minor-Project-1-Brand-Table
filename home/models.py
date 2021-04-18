from django.db import models
from django.urls import reverse

class Product(models.Model):

	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	pid=models.IntegerField(unique=True,default=0)



	class Meta:
		ordering=('name',)
		verbose_name='product'
		verbose_name_plural='products'
	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class Birthday(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)
	class Meta:
		ordering=('name',)
		

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)


class Combos(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)
	class Meta:
		ordering=('name',)
		

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)


class Sweets(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)
	class Meta:
		ordering=('name',)
		

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)



class Bevereges(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)
	class Meta:
		ordering=('name',)
		

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class Burger(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class Combo(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class Chinese(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class Paratha(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class Icecream(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class rice(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class rolls(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])
	def __str__(self):
		return(self.name)

class sandwitch(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class Snacks(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class SouthIndian(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)

class Thali(models.Model):
	name=models.CharField(max_length=250,unique=True)
	slug=models.SlugField(max_length=250,unique=True)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available=models.BooleanField(default=True)
	prod_id=models.IntegerField(unique=True,default=0)

	class Meta:
		ordering=('name',)

	def get_url(self):
		return reverse('cart:cart_detail',args=[self.slug])

	def __str__(self):
		return(self.name)


	

