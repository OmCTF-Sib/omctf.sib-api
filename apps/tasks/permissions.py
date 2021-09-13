from rest_access_policy import AccessPolicy


class TasksAccessPolicy(AccessPolicy):
    statements = [
        {'action': ['list', 'retrieve', 'check'], 'principal': ['authenticated'], 'effect': 'allow'}
    ]
