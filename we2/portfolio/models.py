from django.db import models 

class Portfolio(models.Model): 
    title = models.CharField(max_length = 100, verbose_name = 'Titulacho')
    content = models.TextField(verbose_name = 'Relleno') 
    image = models.ImageField(verbose_name = 'Cuadro Magico', upload_to = 'multimedia') 
    link = models.URLField(blank = True, null = True, verbose_name = 'zelda')
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Primer dia')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Modificacion') 

    class Meta: 
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        ordering = ['-created']

    def __str__(self): 
        return self.title
