from django.db import models
from accounts.models import ProfileModel
#from jalali_date import date2jalali,datetime2jalali
# Create your models here.

class concertModel(models.Model):
    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت"
    
    Name = models.CharField(max_length=100,verbose_name = "نام کنسرت")
    SingerName = models.CharField(max_length=100,verbose_name = "نام خواننده")
    length = models.IntegerField(verbose_name = "مدت زمان")
    Poster = models.ImageField(upload_to = "concertImages/",null=True,verbose_name = "برچسب")


    def __str__(self):
        return self.SingerName

class locationModel(models.Model):
    class Meta:
        verbose_name = "محل برگزاری"
        verbose_name_plural = "محل برگزاری"
    IdNumber = models.IntegerField(primary_key=True,verbose_name = "کد محل")
    Name = models.CharField(max_length=100,verbose_name = "نام محل")
    Address = models.CharField(max_length=500, default="تهران برج میلاد",verbose_name = "آدرس")
    Phone = models.CharField(max_length=11,null=True,verbose_name = "تلفن")
    Capacity = models.IntegerField(verbose_name = "ظرفیت")
    
    def __str__(self):
        return self.Name

class timeModel(models.Model):
    class Meta:
        verbose_name = "سانس"
        verbose_name_plural = "سانس"
    concertModel = models.ForeignKey(to="concertModel", on_delete=models.PROTECT,verbose_name = "کنسرت")
    locationModel = models.ForeignKey(to="locationModel", on_delete=models.PROTECT,verbose_name = "محل برگزاری")
    StartDateTime = models.DateTimeField(verbose_name = "تاریخ برگزاری")
    seats = models.IntegerField(verbose_name = "تعداد صندلی")
    
    Start = 1
    End = 2
    Cancle = 3
    Sales = 4
    status_choices=((Start,"فروش بلیط شروع شده است"),
                    (End,"فروش بلیط تمام شده است"),
                    (Cancle,"این سانس کنسل شده است"),
                    (Sales,"درحال فروش بلیط"))
    statuses = models.IntegerField(choices = status_choices,verbose_name = "وضعیت")

    def __str__(self):
        return "Time {} ConcertName: {} Location: {}".format(self.StartDateTime,self.concertModel.Name,self.locationModel.Name)
    


class ticketModel(models.Model):
    class Meta:
        verbose_name = "بلیط"
        verbose_name_plural = "بلیط"
    ProfileModel = models.ForeignKey(ProfileModel,on_delete = models.PROTECT,verbose_name = "کاربر")
    timeModel = models.ForeignKey("TimeModel",on_delete = models.PROTECT,verbose_name = "سانس")
    ticketImage = models.ImageField(upload_to = "ticketImages",null=True,verbose_name ="عکس")
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()

    def __str__(self):
        return "Name : {} Price: {}".format(self.Name, self.Price)
        return "TicketInfo: Profile: {} ConcertInfo : {} {} {}".format(ProfileModel.__str__(),concertModel.__str__(),locationModel.__str__,timeModel.Start)
        return "TicketInfo: Profile: {} ConcertInfo : {}".format(timeModel.__str__())
