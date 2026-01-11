"""Tests for initialization helpers."""

from __future__ import annotations

import yaml

from ytscriber import config as cfg
from ytscriber import init, paths


def _patch_dirs(monkeypatch, tmp_path):
    data_dir = tmp_path / "data"
    config_dir = tmp_path / "config"

    monkeypatch.setattr(paths, "get_data_dir", lambda: data_dir)
    monkeypatch.setattr(paths, "get_config_dir", lambda: config_dir)
    monkeypatch.setattr(cfg, "get_config_dir", lambda: config_dir)

    return data_dir, config_dir


def test_ensure_initialized_creates_files(monkeypatch, tmp_path):
    data_dir, config_dir = _patch_dirs(monkeypatch, tmp_path)

    config = init.ensure_initialized()
    assert (config_dir / "config.yaml").exists()
    assert (data_dir / "channels.yaml").exists()
    assert config["version"] == cfg.CONFIG_VERSION


def test_check_for_updates_migrates(monkeypatch, tmp_path):
    _, config_dir = _patch_dirs(monkeypatch, tmp_path)
    config_dir.mkdir(parents=True, exist_ok=True)

    config_path = config_dir / "config.yaml"
    config_path.write_text(
        yaml.safe_dump({"version": 0, "defaults": {"delay": 5}}),
        encoding="utf-8",
    )

    updated = init.check_for_updates()
    assert updated is not None
    assert updated["version"] == cfg.CONFIG_VERSION
