from main.models import Person, Category, Achievements
from rest_framework import serializers

app_name = 'main'

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'surname', 'date_of_birth', 'email', 'number', 'gender', 'year_at_school', 'category', 'achievements', 'date_created']

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'date_created')

class AchievementsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ('id', 'title', 'date_created')