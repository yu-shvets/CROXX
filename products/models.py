from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class Category(CommonInfo):
    class Meta(CommonInfo.Meta):
        verbose_name = "Main Category"
        verbose_name_plural = "Main Categories"

    title = models.CharField(max_length=256)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class FootwearType(CommonInfo):
    class Meta(CommonInfo.Meta):
        verbose_name = "Footwear Type"
        verbose_name_plural = "Footwear Types"

    title = models.CharField(max_length=256)
    icon = models.FileField(upload_to='footwear_types/icons', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Brand(CommonInfo):
    class Meta(CommonInfo.Meta):
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='brands/images', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Collection(CommonInfo):
    class Meta(CommonInfo.Meta):
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

    title = models.CharField(max_length=256)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Color(CommonInfo):
    class Meta(CommonInfo.Meta):
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    title = models.CharField(max_length=256)

    def __str__(self):
        return "{}".format(self.title)


class Size(CommonInfo):
    class Meta(CommonInfo.Meta):
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    number = models.IntegerField()

    def __str__(self):
        return "{}".format(self.number)


class SpecsType(CommonInfo):
    title = models.CharField(max_length=256)

    def __str__(self):
        return "{}".format(self.title)


class Specification(CommonInfo):
    title = models.CharField(max_length=256)
    type = models.ForeignKey(SpecsType, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.type, self.title)


class Product(CommonInfo):
    title = models.CharField(max_length=256)
    vendor_code = models.CharField(max_length=256, blank=True, null=True)
    title_image = models.ImageField(upload_to='items/title_images')
    price = models.IntegerField()
    old_price = models.IntegerField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    footwear_type = models.ForeignKey(FootwearType, blank=True, null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, blank=True, null=True, on_delete=models.CASCADE)
    color = models.ManyToManyField(Color, blank=True)
    size = models.ManyToManyField(Size, blank=True)
    specs = models.ManyToManyField(Specification, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.title)


class Image(CommonInfo):
    image = models.ImageField(upload_to='items/images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.product, self.image)


class CustomerEmail(CommonInfo):
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.email)