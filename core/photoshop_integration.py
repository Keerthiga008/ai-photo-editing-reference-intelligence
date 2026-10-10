from __future__ import annotations

import os
import subprocess
from pathlib import Path


class PhotoshopIntegration:
    """Handles Photoshop detection and file handoff for approved edits."""

    def __init__(self, photoshop_executable: str | None = None) -> None:
        self.photoshop_executable = photoshop_executable or self.detect_photoshop()

    def detect_photoshop(self) -> str | None:
        typical_paths = [
            r"C:\Program Files\Adobe\Adobe Photoshop 2025\Photoshop.exe",
            r"C:\Program Files\Adobe\Adobe Photoshop 2024\Photoshop.exe",
            r"C:\Program Files\Adobe\Adobe Photoshop 2023\Photoshop.exe",
            r"C:\Program Files\Adobe\Adobe Photoshop 2022\Photoshop.exe",
            r"C:\Program Files\Adobe\Adobe Photoshop 2021\Photoshop.exe",
        ]

        for path in typical_paths:
            if os.path.exists(path):
                return path
        return None

    def open_in_photoshop(self, file_path: str | Path) -> bool:
        target = str(file_path)
        if not os.path.exists(target):
            raise FileNotFoundError(f"File does not exist: {target}")

        if not self.photoshop_executable:
            raise RuntimeError("Photoshop executable not found on the system.")

        try:
            subprocess.Popen([self.photoshop_executable, target])
            return True
        except Exception as exc:
            raise RuntimeError(f"Failed to launch Photoshop for {target}: {exc}") from exc

    def export_for_photoshop(self, source_path: str | Path, output_path: str | Path) -> Path:
        source = Path(source_path)
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        if not source.exists():
            raise FileNotFoundError(f"Source file not found: {source}")

        # This is a placeholder implementation. In a full app, the project would
        # preserve layers, metadata, and full-resolution output requirements.
        output.write_bytes(source.read_bytes())
        return output


if __name__ == "__main__":
    integration = PhotoshopIntegration()
    print(f"Photoshop executable: {integration.photoshop_executable}")
