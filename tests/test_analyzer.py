import json
from pathlib import Path

from src.graph import PermissionGraph
from src.analyzer import detect_shadow_admins


def load_sample():
    p = Path(__file__).resolve().parents[1] / "data" / "sample_graph.json"
    return json.loads(p.read_text(encoding="utf-8"))


def test_detects_alice_as_shadow_admin():
    data = load_sample()
    g = PermissionGraph(data)
    findings = detect_shadow_admins(g)
    users = {f["user"] for f in findings}
    assert "alice" in users
    assert "bob" not in users
    assert "carol" not in users
