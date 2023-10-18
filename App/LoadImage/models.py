from django.db import models

# Create your models here.
class Image(models.Model):
    image2analysis = models.ImageField(verbose_name='Cargar Imagen: ', null=True, blank=True, upload_to='images/')

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            actualImage = Image.objects.get(id=self.id)
            actualImage.image2analysis.delete()
        except: 
            pass # when new photo then we do nothing, normal case          
        super().save(*args, **kwargs)

    def __str__(self):
        return f'({self.id}) Image uploaded at: '+ str(self.image2analysis)

class ThresholdData(models.Model):
    upperThres = models.IntegerField(verbose_name='Upper Threshold: ', null=True, blank=True)
    lowerThres = models.IntegerField(verbose_name='Lower Threshold: ', null=True, blank=True)

    def __str__(self):
        return f'Upper: {self.upperThres}, Lower: {self.lowerThres}'