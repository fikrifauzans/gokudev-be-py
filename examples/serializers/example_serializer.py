from rest_framework import serializers
from examples.models.example_model import ExampleModel, LANGUAGE_CHOICES, STYLE_CHOICES


class ExampleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    string = serializers.CharField(required=False, max_length=255)
    text = serializers.CharField(required=False, max_length=1024)
    smallint = serializers.IntegerField(required=False, min_value=-32768, max_value=32767)
    integer = serializers.IntegerField(required=False, min_value=-2147483648, max_value=2147483647)
    biginteger = serializers.IntegerField(required=False, min_value=-9223372036854775808, max_value=9223372036854775807)
    boolean = serializers.BooleanField(required=True)
    date = serializers.DateField(required=False)
    datetime = serializers.DateTimeField(required=False)
    time = serializers.TimeField(required=False)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    deleted_at = serializers.DateTimeField(required=False)

    created_by = serializers.IntegerField(required=False, min_value=1)
    updated_by = serializers.IntegerField(required=False, min_value=1)
    deleted_by = serializers.IntegerField(required=False, min_value=1)

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
