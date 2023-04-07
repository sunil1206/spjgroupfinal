from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

# Create your models here.
class card(models.Model):
    name =models.CharField(max_length=50)
    cardno=models.BigIntegerField()
    issuedate=models.DateField()
    expiredate=models.DateField()
    qr_code = models.ImageField(upload_to='qr',blank=True)

    def __str__(self):
        return str(self.cardno)

    def save(self, *args, **kwargs):
        qr_info = f"{self.name}\nCard number: {self.cardno}\nExpire date: {self.expiredate}"
        qrcode_img = qrcode.make(qr_info)

        canvas = Image.new('RGB',(400,400),'white')
        drew=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.cardno}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


