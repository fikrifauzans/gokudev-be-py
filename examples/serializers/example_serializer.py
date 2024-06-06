from rest_framework import serializers
from examples.models.example_model import ExampleModel, LANGUAGE_CHOICES, STYLE_CHOICES


class ExampleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    string = serializers.CharField(required=False)
    text = serializers.CharField(required=False)
    smallint = serializers.IntegerField(required=False)
    integer = serializers.IntegerField(required=False)
    biginteger = serializers.IntegerField(required=False)
     boolean = serializers.BooleanField(required=True)
    date = serializers.DateField(required=False)
    datetime = serializers.DateTimeField(required=False)
    time = serializers.TimeField(required=False)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    deleted_at = serializers.DateTimeField(required=False)

    created_by = serializers.IntegerField(required=False)
    updated_by = serializers.IntegerField(required=False)
    deleted_by = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return ExampleModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.string = validated_data.get("string", instance.string)
        instance.text = validated_data.get("text", instance.text)
        instance.smallint = validated_data.get("smallint", instance.smallint)
        instance.integer = validated_data.get("integer", instance.integer)
        instance.biginteger = validated_data.get("biginteger", instance.biginteger)
        instance.boolean = validated_data.get("boolean", instance.boolean)
        instance.date = validated_data.get("date", instance.date)
        instance.datetime = validated_data.get("datetime", instance.datetime)
        instance.time = validated_data.get("time", instance.time)
