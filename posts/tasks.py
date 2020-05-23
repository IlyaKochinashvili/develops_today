from __future__ import absolute_import, unicode_literals
from celery.task import task

from posts.models import Post


@task()
def refresh_upvotes():
    Post.objects.all().update(amount_of_upvotes=0)
