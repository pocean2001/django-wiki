from django.db import models
from django.utils.translation import ugettext_lazy as _

import settings

from wiki.models.pluginbase import RevisionPlugin

class Image(RevisionPlugin):
    
    image = models.ImageField(upload_to=settings.IMAGE_PATH)
    
    def get_filename(self):
        if self.image:
            return self.image.path.split('/')[-1]
    
    class Meta:
        verbose_name = _(u'image')
        verbose_name_plural = _(u'images')
    
    def __unicode__(self):
        return _(u'Image: %s') % self.get_filename()
    