# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'upna_id', 'name', 'email', 'telephone', 'timetable')
