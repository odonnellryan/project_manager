from project_manager.models import Member, Role

def create_new_member(name, roles):
    """

    :type name: string
    :type roles: list of [Role]
    :rtype: Member
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

def assign_role_to_member(member, role):
    """
    :type member: Member
    :type role: Role
    :rtype: Member
    """
    member.add(role)
    return member

def create_new_role(name):
    """
    :type name: string "name of new role"
    :rtype: Role
    """
    role = Role(role_name=name)
    role.save()
    return role

def get_member_by_pk(pk):
    return Member.get(pk=pk)