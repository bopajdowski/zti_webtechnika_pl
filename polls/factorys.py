# -*- coding: utf-8 -*-
from datetime import datetime

from factory.django import DjangoModelFactory
import factory
from polls.models import Question


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    question_text = factory.Sequence(lambda n: 'question_text%d' % n)
    pub_date = factory.LazyFunction(datetime.now)

