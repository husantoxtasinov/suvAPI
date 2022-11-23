from unittest import TestCase

from asosiy.serializers import *
from asosiy.models import *



class TestMijozSer(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id":2, "ism":"Ali",
            "tel":"+998916693704", "manzil":"Marg'ilon, markaz",
              "qarz":0,
            "user":User.objects.get(id=1)}

    def test_mijoz_ser(self):
        ser = MijozSerializer(self.data)
        assert ser.data['id'] == 2
        assert ser.data['ism'] == "Ali"
        assert ser.data['tel'] == "+998916693704"
        assert ser.data['manzil'] == "Marg'ilon, markaz"
class TestSuvSer(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id":2, "narx":3000,
            "brend":"Hamza", "batafsil":"askjhaofkjbnafdk",
              "litr":2,
            "user":User.objects.get(id=1)}

    def test_suv_ser(self):
        ser = MijozSerializer(self.data)
        assert ser.data['id'] == 2
        assert ser.data['narx'] == 3000
        assert ser.data['litr'] == 2
        assert ser.data['batafsil'] == "askjhaofkjbnafdk"
