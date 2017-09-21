# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
import json
from models import RoomUserModel, SdpModel, CandidateModel


def join(request):
    request_json = json.loads(request.body)
    room_name_value = request_json['room_name']
    room_user_list = RoomUserModel.objects.filter(room_name=room_name_value)
    if len(room_user_list) >= 4:
        return HttpResponse(json.dumps({'error': 1,
                                        'msg': '房间已满'}), content_type='application/json')

    room_user_model = RoomUserModel()
    room_user_model.room_name = room_name_value
    room_user_model.save()
    room_user_list_json = []
    for room_user_item in room_user_list:
        room_user_list_json.append({'room_user_id': room_user_item.id})

    return HttpResponse(json.dumps({'error': 0,
                                    'msg': 'success',
                                    'my_user_id': room_user_model.id,
                                    'other_user_id': room_user_list_json}), content_type='application/json')


def leave(request):
    request_json = json.loads(request.body)
    src_user_id_value = request_json['src_user_id'];
    room_name_value = request_json['room_name']
    room_user_list = RoomUserModel.objects.filter(room_name=room_name_value).filter(id=src_user_id_value)
    for room_user_item in room_user_list:
        room_user_item.delete();

    sdp_list = SdpModel.objects.filter(room_name=room_name_value) \
    .filter(src_user_id=src_user_id_value)
    for sdp_item in sdp_list:
        sdp_item.delete();

    sdp_list = SdpModel.objects.filter(room_name=room_name_value) \
    .filter(dst_user_id=src_user_id_value)
    for sdp_item in sdp_list:
        sdp_item.delete();

    candidate_list = CandidateModel.objects.filter(room_name=room_name_value) \
    .filter(src_user_id=src_user_id_value)
    for candidate_item in candidate_list:
        candidate_item.delete();

    candidate_list = CandidateModel.objects.filter(room_name=room_name_value) \
    .filter(dst_user_id=src_user_id_value)
    for candidate_item in candidate_list:
        candidate_item.delete();

    return HttpResponse(json.dumps({'error': 0,
                                    'msg': 'success'}), content_type='application/json')


def sdp(request):
    request_json = json.loads(request.body)
    print "sdp:%s" %request_json
    src_user_id_value = request_json['src_user_id']
    dst_user_id_value = request_json['dst_user_id']
    room_name_value = request_json['room_name']
    is_initiator_value = int(request_json['is_initiator'])
    sdp_type = request_json['sdp_type']
    sdp_description = request_json['sdp_description']

    sdp_list = SdpModel.objects.filter(room_name=room_name_value) \
    .filter(src_user_id=src_user_id_value).filter(dst_user_id=dst_user_id_value)
    if len(sdp_list) == 0:
        sdp_model = SdpModel()
    else:
        sdp_model = sdp_list[0]
    sdp_model.room_name = room_name_value
    sdp_model.src_user_id = src_user_id_value
    sdp_model.dst_user_id = dst_user_id_value
    sdp_model.is_initiator = is_initiator_value
    sdp_model.sdp_type = sdp_type
    sdp_model.sdp_description = sdp_description
    sdp_model.save()

    return HttpResponse(json.dumps({'error': 0,
                                    'msg': 'success'}), content_type='application/json')


def get_sdp_and_candidate(request):
    request_json = json.loads(request.body)
    room_name_value = request_json['room_name']
    dst_user_id_value = int(request_json['dst_user_id'])
    sdp_list = SdpModel.objects.filter(room_name=room_name_value).filter(dst_user_id=dst_user_id_value) \
    .filter(is_added=False)
    sdp_list_json = []
    for sdp_item in sdp_list:
        sdp_list_json.append({'room_name': sdp_item.room_name,
                              'src_user_id': sdp_item.src_user_id,
                              'dst_user_id': sdp_item.dst_user_id,
                              'is_initiator': sdp_item.is_initiator,
                              'sdp_type': sdp_item.sdp_type,
                              'sdp_description': sdp_item.sdp_description})
        sdp_item.is_added = True;
        sdp_item.save();

    ice_list = CandidateModel.objects.filter(room_name=room_name_value) \
        .filter(dst_user_id=dst_user_id_value).filter(is_added=False)
    ice_list_json = []
    for ice_item in ice_list:
        ice_json = {'room_name': ice_item.room_name,
                    'src_user_id': ice_item.src_user_id,
                    'dst_user_id': ice_item.dst_user_id,
                    'ice_sdp_mid': ice_item.ice_sdp_mid,
                    'ice_sdp': ice_item.ice_sdp,
                    'ice_sdp_m_line_index': ice_item.ice_sdp_m_line_index}
        ice_list_json.append(ice_json)
        ice_item.is_added = True;
        ice_item.save();

    return HttpResponse(json.dumps({'error': 0,
                                    'msg': 'success',
                                    'sdp_list': sdp_list_json,
                                    'ice_list_json': ice_list_json}), content_type='application/json')


def candidate(request):
    request_json = json.loads(request.body)
    room_name_value = request_json['room_name']
    src_user_id_value = request_json['src_user_id']
    dst_user_id_value = request_json['dst_user_id']
    is_initiator_value = int(request_json['is_initiator'])
    ice_sdp_mid = request_json['ice_sdp_mid']
    ice_sdp = request_json['ice_sdp']
    ice_sdp_m_line_index = int(request_json['ice_sdp_m_line_index'])

    candidate_model = CandidateModel()
    candidate_model.room_name = room_name_value
    candidate_model.src_user_id = src_user_id_value
    candidate_model.dst_user_id = dst_user_id_value
    candidate_model.is_initiator = is_initiator_value
    candidate_model.ice_sdp_mid = ice_sdp_mid
    candidate_model.ice_sdp = ice_sdp
    candidate_model.ice_sdp_m_line_index = ice_sdp_m_line_index
    candidate_model.save()

    return HttpResponse(json.dumps({'error': 0,
                                    'msg': 'success'}), content_type='application/json')
