# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View


class ToolsView(View):
    def get(self, request):
        return render(request, 'tool/onlines.html', context={})