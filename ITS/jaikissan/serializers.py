from rest_framework import serializers
from .models import Kissan
from .models import Farm
from .models import Well
from .models import WellUpdate
from .models import FamilyMember
from .models import Question
from .models import Answer
from .models import Seed
from .models import Fertilizer
from .models import CropPrice
from .models import House

# Serializer data for the Kissans(household)

class KissanSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Kissan
		fields = '__all__'

# Serializer data for the Farms

class FarmSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Farm
		fields = '__all__'

# Serializer data for the Wells

class WellSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Well
		fields = '__all__'

# Serializer data for the WellUpdate

class WellUpdateSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = WellUpdate
		fields = '__all__'

# Serializer data for the Familymember

class FamilyMemberSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = FamilyMember
		fields = '__all__'

# Serializer data for the Question

class QuestionSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Question
		fields = '__all__'

# Serializer data for Answer

class AnswerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Answer
		fields = '__all__'

# Serializer data for the seeds

class SeedSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Seed
		fields = '__all__'

# Serializer data for the Fertilizer

class FertilizerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Fertilizer
		fields = '__all__'

# Serializer data for the CropPrice

class CropPriceSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = CropPrice
		fields = '__all__'

# Serializer data for the Houses

class HouseSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = House
		fields = '__all__'

