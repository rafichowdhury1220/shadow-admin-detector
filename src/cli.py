import argparse
import json
from typing import Any

from .graph import PermissionGraph
from .analyzer import detect_shadow_admins


def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Shadow Admin Detector demo CLI")
    parser.add_argument("graph", help="Path to permission graph JSON")
    args = parser.parse_args()

    data = load_json(args.graph)
    g = PermissionGraph(data)

    findings = detect_shadow_admins(g)
    if not findings:
        print("No shadow admins detected in the provided graph.")
        return

    print("Detected potential shadow admins:")
    for r in findings:
        print("- User:", r["user"])
        print("  Assigned roles:", ", ".join(r["assigned_roles"]))
        print("  Effective perms:", ", ".join(r["effective_permissions"]))
        print("  Reason:", r["reason"])
        print()


if __name__ == "__main__":
    main()
