from rest_access_policy import AccessPolicy


class NotificationAccessPolicy(AccessPolicy):
    statements = [{'action': ['list'], 'principal': '*', 'effect': 'allow'}]
