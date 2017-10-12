from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Kissan
from .serializers import KissanSerializer
from .models import Farm, Well, WellUpdate, FamilyMember, Question, Answer, Seed, Fertilizer, CropPrice, House
from .serializers import FarmSerializer,WellSerializer,WellUpdateSerializer,FamilyMemberSerializer,QuestionSerializer,AnswerSerializer,SeedSerializer,FertilizerSerializer,CropPriceSerializer,HouseSerializer
from rest_framework import generics
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render



def rend(request):
	data = Well.objects.all()
	data1= FamilyMember.objects.all()
	data2= Farm.objects.all()
	data3= House.objects.all()
        return render(request, 'jaikissan/rend.html',context={'data':data,'data1':data1,'data2':data2,'data3':data3})

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render_to_response('jaikissan/rend.html', context_dict, context)


# For viewing the JSON data of Kissans

class KissanList(generics.ListCreateAPIView):
	queryset = Kissan.objects.all()
	serializer_class = KissanSerializer

class KissanDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Kissan.objects.all()
	serializer_class = KissanSerializer

# For viewing the JSON data of Farms

class FarmList(generics.ListCreateAPIView):
	queryset = Farm.objects.all()
	serializer_class = FarmSerializer

class FarmDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Farm.objects.all()
	serializer_class = FarmSerializer

# For viewing the JSON data of Wells

class WellList(generics.ListCreateAPIView):
	queryset = Well.objects.all()
	serializer_class = WellSerializer

class WellDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Well.objects.all()
	serializer_class = WellSerializer

# For viewing the JSON data of WellUpdates

class WellUpdateList(generics.ListCreateAPIView):
	queryset = WellUpdate.objects.all()
	serializer_class = WellUpdateSerializer

class WellUpdateDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = WellUpdate.objects.all()
	serializer_class = WellUpdateSerializer

# For viewing the JSON data of Family members

class FamilyMemberList(generics.ListCreateAPIView):
	queryset = FamilyMember.objects.all()
	serializer_class = FamilyMemberSerializer

class FamilyMemberDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = FamilyMember.objects.all()
	serializer_class = FamilyMemberSerializer

# For viewing the JSON data of Questions

class QuestionList(generics.ListCreateAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer

# For viewing the JSON data of Answers

class AnswerList(generics.ListCreateAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer

# For viewing the JSON data of different Seeds and their prices

class SeedList(generics.ListCreateAPIView):
	queryset = Seed.objects.all()
	serializer_class = SeedSerializer

class SeedDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Seed.objects.all()
	serializer_class = SeedSerializer


# For viewing the JSON data of different Fertilizers and their prices

class FertilizerList(generics.ListCreateAPIView):
	queryset = Fertilizer.objects.all()
	serializer_class = FertilizerSerializer

class FertilizerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Fertilizer.objects.all()
	serializer_class = FertilizerSerializer


# For viewing the JSON data of market prices of different Crops

class CropPriceList(generics.ListCreateAPIView):
	queryset = CropPrice.objects.all()
	serializer_class = CropPriceSerializer

class CropPriceDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CropPrice.objects.all()
	serializer_class = CropPriceSerializer

# For viewing the JSON data of Houses

class HouseList(generics.ListCreateAPIView):
	queryset = House.objects.all()
	serializer_class = HouseSerializer

class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = House.objects.all()
	serializer_class = HouseSerializer
