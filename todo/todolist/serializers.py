from rest_framework import serializers
from todolist.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'user_id', 'task_name', 'description', 'completed', 'created_at']
        read_only_fields = ['id', 'user_id', 'created_at']