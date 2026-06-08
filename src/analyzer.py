from typing import Dict, List


def detect_shadow_admins(graph) -> List[Dict]:
    """Detect users who have `admin` in their effective permissions but don't have an explicit admin role name."""

    results = []
    for user in graph.users.keys():
        perms = graph.effective_permissions_for_user(user)
        if any(p.lower() == "admin" or "admin" in p.lower() for p in perms):
            assigned_roles = graph.roles_for_user(user)
            has_explicit_admin_role = any("admin" in r.lower() for r in assigned_roles)
            if not has_explicit_admin_role:
                results.append({
                    "user": user,
                    "effective_permissions": list(perms),
                    "assigned_roles": assigned_roles,
                    "reason": "effective admin privilege without explicit admin role",
                })

    return results
