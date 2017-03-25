# from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('title'), max_length=128)
    created_at = models.DateTimeField(_('created_ad'), auto_now_add=True)
    announce_text = models.TextField(_('announce'), max_length=512, blank=True)
    body = models.TextField(_('body'), max_length=4096)

    def __str__(self):
        return self.title

    @property
    def announce(self):
        return self.announce_text or self.body[:512].rsplit(' ', 1)[0]

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('post')
        verbose_name_plural = _('posts')
