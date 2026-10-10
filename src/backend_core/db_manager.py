from __future__ import annotations

import sqlite3
from pathlib import Path


class DatabaseManager:
    """Simple SQLite access layer for project and media metadata."""

    def __init__(self, db_path: str | Path):
        self.db_path = str(db_path)
        self._initialize()

    def _initialize(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA foreign_keys=ON;")
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS projects (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    base_color_space TEXT DEFAULT 'ACEScc',
                    scratch_disk_path TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS media_assets (
                    id TEXT PRIMARY KEY,
                    project_id TEXT REFERENCES projects(id) ON DELETE CASCADE,
                    file_path TEXT UNIQUE NOT NULL,
                    file_format TEXT NOT NULL,
                    color_space TEXT,
                    bit_depth INTEGER DEFAULT 16,
                    capture_timestamp TIMESTAMP,
                    shutter_speed REAL,
                    aperture REAL,
                    iso INTEGER,
                    focal_length REAL,
                    is_raw BOOLEAN DEFAULT 1
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS classifications (
                    asset_id TEXT PRIMARY KEY REFERENCES media_assets(id) ON DELETE CASCADE,
                    scene_category TEXT,
                    lighting_type TEXT,
                    indoor_outdoor_prob REAL,
                    face_count INTEGER DEFAULT 0,
                    primary_subject_bbox JSON,
                    histogram_metrics JSON,
                    quality_flags JSON
                )
                """
            )
            conn.commit()

    def add_project(self, project_id: str, name: str, scratch_disk_path: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO projects(id, name, scratch_disk_path) VALUES (?, ?, ?)",
                (project_id, name, scratch_disk_path),
            )
            conn.commit()

    def add_media_asset(self, asset_id: str, project_id: str, file_path: str, file_format: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO media_assets(id, project_id, file_path, file_format) VALUES (?, ?, ?, ?)",
                (asset_id, project_id, file_path, file_format),
            )
            conn.commit()
