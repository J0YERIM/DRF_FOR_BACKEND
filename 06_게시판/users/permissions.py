from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission): # GET : 누구나, PUT/PATCH : 해당 유저
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # permissions.SAFE_METHOD : 데이터에 영향을 미치지 않는 메소드 ex. GET
            return True
        return obj.user == request.user # PUT/PATCH와 같은 경우에는 요청으로 들어온 유저와 객체의 유저를 비교