# -*- coding: utf-8 -*-
from django.utils import timezone


def myfirst(request):
    return {
        'today': timezone.now(),
    }
