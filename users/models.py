from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # hier überschreiben wir die ursprüngliche save() Methode mit einer Objektspezifischen Save() Methode
    def save(self):
        super().save() # das ist die save Methode der übergeordneten klasse
 
        img = Image.open(self.image.path) #das Bild wird als Objekt img geöffnet
        if img.height > 300 or img.width > 300: # check der Größe
            output_size = (300, 300) # die resize Parameter werden festgelegt
            img.thumbnail(output_size)
            img.save(self.image.path)

