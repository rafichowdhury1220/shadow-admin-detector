# Architecture — Architect's Thinking

This document captures the solution architect's reasoning and trade-offs for the Shadow Admin Detector project.

Goals

- Quickly detect accounts with effective administrative privileges that are not explicitly labelled as Admins.
- Produce reproducible, explainable results suitable for security discussions and recruiting demos.

Design overview

- Data model: simple permission graph with `users` and `roles`. Roles can grant permissions and can include other roles (inheritance).
- Analysis: expand a user's roles transitively, union their grants, and flag an account as a shadow admin if the effective grants include `admin` (or similarly high-privileged scopes) while none of the account's explicit roles are named or flagged as `admin`.

Why this model?

- It's easy to explain to non-developers and easy to extend to cloud IAM exports.
- Trade-offs: this approach assumes role inheritance and direct grants model permissions accurately. Complex policies (conditions, resource scoping, time-limited grants) require a richer policy engine.

Threat model and heuristics

- Primary target: discover privilege escalation due to role inheritance or combined privileges.
- Heuristic: treat permission name `admin` or containing `admin` as high-privilege. For production, replace with scoring and resource-aware checks.

Extensibility

- Add policy rules that infer admin-equivalence from combinations of permissions.
- Add graph visualizations and CI pipelines to run this detector against exported IAM snapshots.

Notes for recruiters

- This repo emphasizes clear design thinking, small and testable Python modules, and a path to production integrations (exports, dashboards, CI).
