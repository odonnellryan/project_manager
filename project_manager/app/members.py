from project_manager.models import Member, Role

def create_new_member(name, roles):
    """

    :type name: string
    :type roles: list of [Role]
    :rtype: bool
    """
    member = Member(member_name=name)
    member.roles.add(roles)
    member.save()
    return member


def get_all_members(member_ids):
    """
    :type member_ids: list of [int]
    :rtype: list of [Member]
    """
    return Member.filter(pk__in=member_ids)

def assign_role_to_member(member):
    return Member

def create_new_role(name):
    """
    :param type name: string "name of new role"
    :rtype: bool
    """
    role = Role(role_name=name)
    role.save()
    return role