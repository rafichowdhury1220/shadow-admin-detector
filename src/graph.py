from typing import Dict, Set, List


class PermissionGraph:
    """Simple permission graph supporting roles that include other roles and grant permissions."""

    def __init__(self, data: Dict):
        self.users = data.get("users", {})
        self.roles = data.get("roles", {})

    def roles_for_user(self, user: str) -> List[str]:
        return self.users.get(user, {}).get("roles", [])

    def _walk_role_inheritance(self, start_roles: List[str]) -> Set[str]:
        seen = set()
        stack = list(start_roles)
        while stack:
            r = stack.pop()
            if r in seen:
                continue
            seen.add(r)
            children = self.roles.get(r, {}).get("roles", [])
            for c in children:
                if c not in seen:
                    stack.append(c)
        return seen

    def effective_permissions_for_user(self, user: str) -> Set[str]:
        roles = self.roles_for_user(user)
        all_roles = self._walk_role_inheritance(roles)
        perms = set()
        for r in all_roles:
            grants = self.roles.get(r, {}).get("grants", [])
            for p in grants:
                perms.add(p)
        return perms
