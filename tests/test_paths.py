"""Tests for paths helpers."""

from __future__ import annotations

from types import SimpleNamespace

import yaml

from ytscriber import paths


def test_get_data_dir_linux(monkeypatch, tmp_path):
    monkeypatch.setattr(paths, "sys", SimpleNamespace(platform="linux"))
    monkeypatch.setattr(paths.Path, "home", lambda: tmp_path)

    assert paths.get_data_dir() == tmp_path / "ytscriber"


def test_get_data_dir_documents(monkeypatch, tmp_path):
    monkeypatch.setattr(paths, "sys", SimpleNamespace(platform="darwin"))
    monkeypatch.setattr(paths, "user_documents_path", lambda: tmp_path / "Documents")

    assert paths.get_data_dir() == tmp_path / "Documents" / "YTScriber"


def test_get_default_collection_dir(monkeypatch, tmp_path):
    data_dir = tmp_path / "data"
    monkeypatch.setattr(paths, "get_data_dir", lambda: data_dir)

    assert paths.get_default_collection_dir() == data_dir / paths.DEFAULT_COLLECTION


def test_ensure_data_structure_creates_files(monkeypatch, tmp_path):
    data_dir = tmp_path / "data"
    config_dir = tmp_path / "config"

    monkeypatch.setattr(paths, "get_data_dir", lambda: data_dir)
    monkeypatch.setattr(paths, "get_config_dir", lambda: config_dir)

    paths.ensure_data_structure()

    channels_file = data_dir / "channels.yaml"
    assert data_dir.exists()
    assert config_dir.exists()
    assert channels_file.exists()
    assert (data_dir / paths.DEFAULT_COLLECTION).exists()
    assert (data_dir / paths.DEFAULT_COLLECTION / "transcripts").exists()

    data = yaml.safe_load(channels_file.read_text(encoding="utf-8"))
    assert data["channels"] == []
    assert data["collections"] == []
