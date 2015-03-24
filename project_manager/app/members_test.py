from project_manager.app import members
from django.test import TestCase

class MemberTestCase(TestCase):
    def setUp(self):
        test_user_name = "test_name"
        test_role_name = "test_role"
        test_role_name_2 = "test_role_2"
        self.role = members.create_new_role(test_role_name)
        self.role2 = members.create_new_role(test_role_name_2)
        self.test_member = members.create_new_member(test_user_name, self.role)
        self.test_member = members.assign_role_to_member(self.test_member, self.role2)
        self.member_pk = self.test_member.pk

    def test_member_actions(self):
        member = members.get_member_by_pk(self.member_pk)
        assert member == self.test_member
        assert self.role2 in member.roles.all()
        assert self.role in member.roles.all()