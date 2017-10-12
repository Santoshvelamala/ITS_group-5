from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Database table for the Farmer(household)


class Kissan(models.Model):
    CLASS_CHOICES = ((u'Male','Male'),(u'Female', 'Female'),)
    CLASS_DISTRICTS = ((u'Ananthapur','Ananthapur'),(u'Chittoor','Chittoor'),(u'Karimnagar','Karimnagar'),(u'East Godavari','East Godavari'),(u'Guntur','Guntur'),(u'Kadapa','Kadapa'),(u'Krishna','Krishna'),(u'Kurnool','Kurnool'),(u'Nellore','Nellore'),(u'Prakasam','Prakasam'),(u'Srikakulam','Srikakulam'),(u'Visakhapatnam','Visakhapatnam'),(u'Vijayanagaram','Vijayanagaram'),(u'West Godavari','West Godavari'),)

    K_id = models.IntegerField()
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Password = models.CharField(max_length=50)
    Phone = models.IntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    No_of_acres= models.IntegerField()
    H_no= models.CharField(max_length=50)
    Village= models.CharField(max_length=50)
    District= models.CharField(max_length=50,choices=CLASS_DISTRICTS)
    Gender= models.CharField("Gender",max_length=50,choices=CLASS_CHOICES)
    D_o_b= models.DateField(null=True)
    Total_monthly_income= models.IntegerField()
    Profile_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    Audio = models.FileField(upload_to = u'mp3/', max_length=200)

    def __str__(self):
     return str(self.K_id)


# Database table for Farms (Precisely taken with 8 latitude and longitude points)

	
class Farm(models.Model):
    CLASS_CROP = ((u'Rice','Rice'),(u'Jowar','Jowar'),(u'Bajra','Bajra'),(u'Maize','Maize'),(u'Ragi','Ragi'),(u'Small Millets','Small Millets'),(u'Pulses','Pulses'),(u'Castor','Castor'),(u'Tobacco','Tobacco'),(u'Cotton','Cotton'),(u'Sugarcane','Sugarcane'),)
    CLASS_CHOICES = ((u'Karif','Karif'),(u'Rabi', 'Rabi'),(u'zaid', 'zaid'),)
    FF_id = models.IntegerField()
    Profit = models.IntegerField()
    Investment = models.IntegerField()
    F_id  = models.ForeignKey(Kissan, on_delete=models.CASCADE) 
    Lat_1 = models.FloatField()
    Long_1= models.FloatField()
    Lat_2 = models.FloatField()
    Long_2= models.FloatField()
    Lat_3 = models.FloatField()
    Long_3= models.FloatField()
    Lat_4 = models.FloatField()
    Long_4= models.FloatField()
    Lat_5=models.FloatField()
    Long_5=models.FloatField()
    Lat_6=models.FloatField()
    Long_6=models.FloatField()
    Lat_7=models.FloatField()
    Long_7=models.FloatField()
    Lat_8=models.FloatField()
    Long_8=models.FloatField()
    Season = models.CharField("Season",max_length=50,choices=CLASS_CHOICES)
    Crop = models.CharField("Crop",max_length=50,choices=CLASS_CROP)
    Farm_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    Audio = models.FileField(upload_to = u'mp3/', max_length=200)

    def __str__(self):
     return str(self.FF_id)


# Database table for Wells


class Well(models.Model):
        W_Id = models.IntegerField()
	FF_id  = models.ForeignKey(Farm, on_delete=models.CASCADE) 
	Lat = models.FloatField()
	Long = models.FloatField()
	Depth = models.FloatField()
	Avg_water= models.FloatField()
	Well_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
	Audio = models.FileField(upload_to = u'mp3/', max_length=200)

	def __str__(self):
	 return str(self.W_Id)


# Database table for Well updates


class WellUpdate(models.Model):
    
	W_id  = models.ForeignKey(Well, on_delete=models.CASCADE) 
	Date = models.DateField(null=True)
	Water_Yeild = models.FloatField()
	Wellupadte_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
	Audio = models.FileField(upload_to = u'mp3/', max_length=200)

	def __str__(self):
	 return str(self.W_id)


# Database table for the Family Members of the household


class FamilyMember(models.Model):
    
    CLASS_RELATION = ( 
    (u'Father','Father'), 
    (u'Mother', 'Mother'),
    (u'Son','Son'), 
    (u'Daughter', 'Daughter'),
    (u'Wife','Wife'), 
    (u'Husband', 'Husband'),
    (u'Brother','Brother'), 
    (u'Sister', 'Sister'),
    (u'Other','Other'), 
    )

    CLASS_CHOICES = ( 
    (u'Male','Male'), 
    (u'Female', 'Female'), 
    )

    F_id  = models.ForeignKey(Kissan, on_delete=models.CASCADE) 
    Name = models.CharField(max_length=30)
    Relation= models.CharField(max_length=20,choices=CLASS_RELATION)
    Gender= models.CharField("Gender",max_length=50,choices=CLASS_CHOICES)
    D_o_b= models.DateField(null=True)
    Photo = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    Audio = models.FileField(upload_to = u'mp3/', max_length=200)
  
    def __str__(self):
     return str(self.F_id)



# Database table for the Questions (for discussion forum)


class Question(models.Model):
    
	F_id  = models.ForeignKey(Kissan, on_delete=models.CASCADE) 
	Question = models.TextField(max_length=100)
	
	def __str__(self):
	 return str(self.F_id)


# Database table for the Answers(for discussion forum)


class Answer(models.Model):
    
	F_id  = models.ForeignKey(Kissan, on_delete=models.CASCADE)
	Q_id  = models.ForeignKey(Question, on_delete=models.CASCADE) 
	Answer = models.TextField(max_length=100)

	def __str__(self):
	 return str(self.F_id,self.Q_id)


# Database table for Seeds(for the prices of different types of seeds)


class Seed(models.Model):
    
	SeedName = models.CharField(max_length=20) 
	Price = models.FloatField(max_length=20)

	def __str__(self):
	 return self.SeedName


# Database table for Fertilizers(for the prices of different types of fertilizers)

class Fertilizer(models.Model):
    
	FertilizerName = models.CharField(max_length=20) 
	Price = models.FloatField(max_length=20)

	def __str__(self):
	 return self.FertilizerName


# Database table for CropPrices(for knowing the market prices of different types of crops)

class CropPrice(models.Model):
    
	CropName = models.CharField(max_length=20) 
	Price = models.FloatField(max_length=20)

	def __str__(self):
	 return self.CropName


# Database table for Houses(the latitude and longitude values of the houses of the households)

class House(models.Model):
        H_Id = models.IntegerField()
	F_id  = models.ForeignKey(Kissan, on_delete=models.CASCADE) 
	HLat = models.FloatField()
	HLong = models.FloatField()
	
	def __str__(self):
	 return str(self.H_Id)

