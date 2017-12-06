from rest_framework import serializers
from models import RiskType, RiskField


class RiskFieldSerializer(serializers.ModelSerializer):
    field_choices = serializers.SerializerMethodField()

    class Meta:
        model = RiskField
        fields = '__all__'

    def get_field_choices(self, obj):
        if obj.field_choices:
            choices = obj.field_choices.split(',')
            if obj.is_required is True:
                select_choices = ()
            else:
                select_choices = (('', '---------'),)
            for choice in choices:
                select_choices = select_choices + ((choice, choice),)
            return select_choices
        else:
            return ()


class RiskTypeSerializer(serializers.ModelSerializer):
    riskfield_set = RiskFieldSerializer(many=True, read_only=True)
    class Meta:
        depth=1
        model = RiskType
        fields = ('name', 'riskfield_set')
