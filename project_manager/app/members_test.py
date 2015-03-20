from project_manager.app import members
from django.test import TestCase

class MemberTestCase(TestCase):
    def setUp(self):
        test_user_name = "test_name"
        test_role_name = "test_role"
        test_role_name_2 = "test_role_2"
        role = members.create_new_role(test_role_name)
        role2 = members.create_new_role(test_role_name_2)
        test_member = members.create_new_member(test_user_name, role)
        test_member = members.assign_role_to_member(test_member, role2)
        self.member_pk = test_member.pk

    def test_member_role_assignment(self):
        member = members.get_member_by_pk(self.member_pk)
        print(member.roles.all())
        assert True == False