from collections import defaultdict
class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # John - Johnsmith@gmail.com, john_newyork@mail.com
        # User dictionary
        # 1 - [John, emails]
        # Email dictionary
        # johnsmith@gmail.com - 1
        # john_newyork@gmail.com - 1
        # john00@mail.com - 1
        user_id = 0
        user_dict = defaultdict(list)
        email_dict = defaultdict(int)
        for account in accounts:
            name = account[0]
            emails = account[1:]
            isExist = False
            exist_dupe_users = set()
            # Get all existing dupe users from new entries
            for email in emails:
                if email in email_dict:
                    isExist = True
                    exist_dupe_users.add(email_dict[email])
            if isExist:
                emails = set(emails)
                exist_dupe_users = list(exist_dupe_users)
                # Designate an account to merget to
                merged_user = exist_dupe_users[0]
                # Merge all overlapping account to this new one
                if len(exist_dupe_users) > 1:
                    for dupe_user in exist_dupe_users[1:]:
                        emails_dupe = user_dict[dupe_user][1]
                        emails |= emails_dupe
                        del user_dict[dupe_user]
                user_dict[merged_user][1].update(emails)
                for email in user_dict[merged_user][1]:
                    email_dict[email] = merged_user
            else:
                user_dict[user_id] = [name, set(emails)]
                for email in emails:
                    email_dict[email] = user_id
            user_id += 1
        return [[v[0]] + sorted(v[1]) for v in user_dict.values()]
