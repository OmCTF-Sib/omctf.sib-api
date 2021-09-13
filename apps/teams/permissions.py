from rest_access_policy import AccessPolicy


class TeamAccessPolicy(AccessPolicy):
    statements = [{'action': ['list'], 'principal': '*', 'effect': 'allow'}]
