from rest_framework import serializers


class TinkoffResponseSerializer(serializers.Serializer):
    TerminalKey = serializers.CharField(max_length=20)
    OrderId = serializers.CharField(max_length=20)
    Success = serializers.BooleanField()
    Status = serializers.CharField(max_length=20)
    PaymentId = serializers.IntegerField()
    ErrorCode = serializers.CharField(max_length=20)
    Amount = serializers.DecimalField(max_digits=10, decimal_places=0)
    RebillId = serializers.IntegerField()
    CardId = serializers.IntegerField()
    Pan = serializers.CharField()
    ExpDate = serializers.CharField()
    Token = serializers.CharField()