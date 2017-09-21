from __future__ import unicode_literals

from django.db import models


class RoomUserModel(models.Model):
    room_name = models.CharField(max_length=20)


class SdpModel(models.Model):
    room_name = models.CharField(max_length=20)
    src_user_id = models.IntegerField(default=0)
    dst_user_id = models.IntegerField(default=0)
    is_initiator = models.IntegerField(default=0)
    sdp_type = models.CharField(max_length=50)
    sdp_description = models.CharField(max_length=5000)
    is_added = models.BooleanField(default=False)


class CandidateModel(models.Model):
    room_name = models.CharField(max_length=20)
    src_user_id = models.IntegerField(default=0)
    dst_user_id = models.IntegerField(default=0)
    is_initiator = models.IntegerField(default=0)
    ice_sdp_mid = models.CharField(max_length=2000)
    ice_sdp = models.CharField(max_length=2000)
    ice_sdp_m_line_index = models.IntegerField(default=0)
    is_added = models.BooleanField(default=False)