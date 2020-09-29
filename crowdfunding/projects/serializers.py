from rest_framework import serializers
from .models import Project, Pledge
from users.models import CustomUser
from django.utils import timezone

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    kudos = serializers.BooleanField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.ReadOnlyField(source='supporter.id')
    date_created = serializers.DateTimeField(default=timezone.now())
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    total_raised = serializers.SerializerMethodField()
    num_supporters = serializers.SerializerMethodField()
    image = serializers.URLField()
    is_open = serializers.SerializerMethodField()
    date_created = serializers.DateTimeField(default=timezone.now())
    date_end = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    # owner = serializers.CharField(max_length=200)
    # pledges = PledgeSerializer(many=True, read_only=True)

    def get_total_raised(self, obj):
        total_pledges = obj.pledges.all()
        total = 0
        for pledge in total_pledges:
            total += pledge.amount
        return total

    def get_num_supporters(self, obj):
        filtered_supporters = []
        total_supporters = obj.pledges.all()
        for supporters in total_supporters:
            temp_supporter = supporters.supporter
            if temp_supporter in filtered_supporters:
                pass
            else:
                filtered_supporters.append(temp_supporter)  
        return len(filtered_supporters)

    def get_is_open(self, obj):
        if timezone.now() > obj.date_end:
            is_open = False
        else:
            is_open = True
        return is_open

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
    
class PledgeDetailSerializer(PledgeSerializer):
    project = ProjectSerializer(many=False, read_only=True)
    amount = serializers.IntegerField()

    def update(self, instance, validated_data):

        new_amount = validated_data.get('amount', instance.amount)
        if new_amount >= instance.amount:
            instance.amount = new_amount
            instance.save()
            return instance
        else:
            return 