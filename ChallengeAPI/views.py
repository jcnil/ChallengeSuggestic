from django.shortcuts import render
from django.views import View
from .models import Challenge
from django.http import JsonResponse
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from .serializers import ChallengeSerializer

# Create your views here.

class ChallengeView(APIView):

    serializer_class = ChallengeSerializer

    def get(self, request, format=None):
        if ('json_items' in request.GET):
            data = Challenge.objects.filter(json_items__contains=request.GET['json_items'])
        else:
            data = Challenge.objects.all()

        result = json.loads(data.values()[0]["json_result"])
        return Response(result)
    
    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            items = serializer.validated_data.get('items')
            items = json.loads(items)
            new_array = []
            for i in items:
                if type(i)==int:
                    new_array.append(i)
                else:
                    for val in i:
                        if type(val)==int:
                            new_array.append(val)
                        else:
                            for row in val:
                                new_array.append(row)

            return Response({'result':new_array})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



class ChallengeDetail(View):

    def get(self, request):
        data = Challenge.objects.get(pk=pk)
        return JsonResponse(model_to_dict(data))

    
