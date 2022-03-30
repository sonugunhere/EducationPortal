from accounts.models import StudentRegisteration,SchoolManagement
from rest_framework import serializers


class SchoolManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolManagement
        fields = ['id', 'user', 'username', 'school', 'email', 'contact', 'dise_code', 'address', 'city', 'state', 'country', 'school_type', 'password', 'confirm_password']



class StudentRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegisteration
        fields = ['id', 'school', 'first_name', 'last_name', 'email', 'contact_no', 'father_name', 'mother_name', 'address', 'dob', 'standard', 'gender', 'batch', 'adhar_card']