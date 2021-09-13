from rest_access_policy import AccessPolicy


class TasksAccessPolicy(AccessPolicy):
    statements = [
        {'action': ['list', 'retrieve', 'check'], 'principal': ['authenticated'], 'effect': 'allow'}
    ]


class TasksTypeAccessPolicy(AccessPolicy):
    statements = [{'action': ['list'], 'principal': ['authenticated'], 'effect': 'allow'}]
