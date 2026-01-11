"""Tests for config helpers."""

from __future__ import annotations

from ytscriber import config as cfg


def test_load_config_defaults(monkeypatch, tmp_path):
    monkeypatch.setattr(cfg, "get_config_dir", lambda: tmp_path)

    config = cfg.load_config()
    assert config["version"] == cfg.CONFIG_VERSION
    assert config["defaults"]["delay"] == 60


def test_save_and_read_config(monkeypatch, tmp_path):
    monkeypatch.setattr(cfg, "get_config_dir", lambda: tmp_path)

    config = cfg.default_config()
    config["defaults"]["delay"] = 10
    cfg.save_config(config)

    read_back = cfg.read_config()
    assert read_back["defaults"]["delay"] == 10


def test_set_config_value():
    config = cfg.default_config()
    cfg.set_config_value(config, "summarization.max_words", 800)

    assert config["summarization"]["max_words"] == 800


def test_parse_config_value():
    assert cfg.parse_config_value("123") == 123
    assert cfg.parse_config_value("[\"a\", \"b\"]") == ["a", "b"]
