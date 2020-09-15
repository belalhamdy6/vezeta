from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify





TYPE_OF_PERSON =(
    ("M", "male"),
    ("F", "Female"),
)
# Create your models here.
class Profile(models.Model):
    Doctor_IN = {
        ("جلديه", "جلديه"),
        ("اسنان", "اسنان"),
        ("نفسي", "نفسي"),
        ("اطفال حديثي الولاده", "اطفال حديثي الولاده"),
        ("مخ و اعصاب", "مخ و اعصاب"),
        ("عظام", "عظام"),
        ("نساء و توليد", "نساء و توليد"),
        ("انف و اذن وحنجره", "انف و اذن وحنجره"),
        ("قلب", "قلب"),
        ("باطنه", "باطنه"),
        ("آورام", "آورام"),
        ("جراحه اطفال", "جراحه اطفال"),
        ("اوعيه دمويه", "اوعيه دمويه"),
        ("تجميل", "تجميل"),
        ("سمنه", "سمنه"),

    }
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    name = models.CharField(_('الاسم:'), max_length=50)
    surname = models.CharField(_('اللقب :'), max_length=50)
    type_of_person = models.CharField(_("النوع :"), choices=TYPE_OF_PERSON, max_length=100)
    subtitle = models.CharField(_('نبذه عنك:'), max_length=50)
    address = models.CharField(_('المحافظه :'), max_length=50)
    address_detail = models.CharField(_('العنوان بالتفصيل :'), max_length=50, blank=True, null=True)
    number_phone = models.CharField(_('الهاتف :'), max_length=50)
    work_hour = models.CharField(_('عدد ساعات العمل :'), max_length=50)
    witing_time = models.IntegerField(_('مده الانتظار :'),blank=True, null=True)
    doctor = models.CharField(_('دكتور ؟ :'),choices=Doctor_IN, max_length=50, blank=True, null=True)
    specialist_doctor = models.CharField(_('تخصص في :'), max_length=50, blank=True, null=True)
    who_i = models.TextField(_('من انا :'), max_length=250)
    price = models.IntegerField(_('سعر الكشف :'), blank=True, null=True)
    image = models.ImageField(_('الصوره الشخصيه:'), upload_to='profile', blank=True, null=True)
    faceBook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    Google = models.CharField(max_length=100, blank=True, null=True)
    join_new = models.DateTimeField(_("وقت الانضمام :"), auto_now_add=True, blank=True, null=True)
    slug = models.SlugField(_('slug :'), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return '%s' %(self.user.username)




def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)