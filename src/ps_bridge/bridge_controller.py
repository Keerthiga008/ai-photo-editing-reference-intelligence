from __future__ import annotations

import os
from pathlib import Path
from typing import Any


class PhotoshopBridge:
    """Adobe Photoshop bridge contract with a Windows-only COM implementation hook."""

    def __init__(self) -> None:
        self.app = None

    def connect(self) -> bool:
        try:
            import win32com.client
        except ImportError:
            return False

        try:
            self.app = win32com.client.Dispatch("Photoshop.Application")
            return True
        except Exception:
            return False

    def open_image(self, file_path: str | Path) -> bool:
        target = str(file_path)
        if not os.path.exists(target):
            raise FileNotFoundError(target)
        if self.app is None:
            return False
        try:
            self.app.Open(target)
            return True
        except Exception:
            return False

    def export_psd_ready_workfile(self, source_path: str | Path, output_path: str | Path) -> Path:
        source = Path(source_path)
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(source.read_bytes())
        return output
