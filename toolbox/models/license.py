# -*- coding: utf-8 -*-
from django.db import models
from generic import GenericFields  
import markdown
from django.utils.safestring import mark_safe

class License(GenericFields):
    
    name        = models.CharField (
                                        verbose_name    = 'Naam',
                                        max_length      = 60
                                    )
                                   
    license_md   = models.TextField(   
                                        verbose_name    = 'Beschrijving',
                                        blank           = True
                                    )
                                     
    license_html = models.TextField(   
                                        verbose_name    = 'Beschrijving',
                                        blank           = True,
                                        editable        = False
                                    )                                
    icon        = models.CharField (
                                        verbose_name    = 'Font icon',
                                        blank           = True,
                                        max_length      = 32
                                    )
                                   
    open_source = models.BooleanField (
                                        verbose_name    = 'Open Source?',
                                        default         = False
                                    )

    def save(self, *args, **kw):
        """            
            Convert markdown to html to speed up the pageloading.
        """
        self.license_html = markdown.markdown(self.license_html,extensions=['extra','nl2br','smarty'],output_format='html5').encode("utf-8")
        
        super(License, self).save(*args, **kw)

    def license(self):
        return mark_safe(self.license_html) 
        
    class Meta:
        """
            Change display of model in Django admin
        """
        app_label = "toolbox"
        verbose_name = "Licentie"
        verbose_name_plural = "Licenties"
        
    def __unicode__(self):
        """
            String representation of the model
        """
        return self.name