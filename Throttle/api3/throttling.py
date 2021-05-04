from rest_framework.throttling import UserRateThrottle

class perticular(UserRateThrottle):
    scope='times'