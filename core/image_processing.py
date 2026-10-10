from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import cv2
import numpy as np


@dataclass
class ImageAnalysis:
    width: int
    height: int
    channels: int
    brightness: float
    contrast: float
    exposure_status: str
    white_balance: str
    is_portrait: bool = False
    has_skin_tone: bool = False
    quality_score: float = 0.0


class PhotoProcessor:
    """Core image processing operations for wedding and portrait enhancement."""

    def __init__(self) -> None:
        self.default_profile = {
            "exposure": 1.0,
            "contrast": 1.0,
            "saturation": 1.0,
            "temperature": 0,
            "tint": 0,
        }

    def load_image(self, image_path: str | Path) -> np.ndarray:
        image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"Unable to load image: {image_path}")
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def analyze_image(self, image: np.ndarray) -> ImageAnalysis:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        brightness = float(np.mean(gray))
        contrast = float(np.std(gray))

        if brightness < 80:
            exposure_status = "underexposed"
        elif brightness > 200:
            exposure_status = "overexposed"
        else:
            exposure_status = "good"

        quality_score = max(0.0, min(1.0, (contrast / 255.0) * 0.8 + (brightness / 255.0) * 0.2))

        return ImageAnalysis(
            width=image.shape[1],
            height=image.shape[0],
            channels=image.shape[2],
            brightness=brightness,
            contrast=contrast,
            exposure_status=exposure_status,
            white_balance="auto",
            is_portrait=False,
            has_skin_tone=False,
            quality_score=quality_score,
        )

    def correct_exposure(self, image: np.ndarray, factor: float = 1.1) -> np.ndarray:
        adjusted = np.clip(image * factor, 0, 255).astype(np.uint8)
        return adjusted

    def auto_white_balance(self, image: np.ndarray) -> np.ndarray:
        b, g, r = cv2.split(image.astype(np.float32))
        avg_b = float(np.mean(b))
        avg_g = float(np.mean(g))
        avg_r = float(np.mean(r))
        avg = (avg_b + avg_g + avg_r) / 3.0

        scale_b = avg / avg_b if avg_b else 1.0
        scale_g = avg / avg_g if avg_g else 1.0
        scale_r = avg / avg_r if avg_r else 1.0

        balanced = cv2.merge(
            [
                np.clip(b * scale_b, 0, 255),
                np.clip(g * scale_g, 0, 255),
                np.clip(r * scale_r, 0, 255),
            ]
        ).astype(np.uint8)
        return balanced

    def sharpen(self, image: np.ndarray, strength: float = 1.0) -> np.ndarray:
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
        sharpened = cv2.filter2D(image, -1, kernel * strength)
        return np.clip(sharpened, 0, 255).astype(np.uint8)

    def enhance(self, image: np.ndarray) -> np.ndarray:
        corrected = self.correct_exposure(image, factor=1.05)
        balanced = self.auto_white_balance(corrected)
        return self.sharpen(balanced, strength=0.7)


if __name__ == "__main__":
    sample = np.zeros((100, 100, 3), dtype=np.uint8)
    processor = PhotoProcessor()
    analysis = processor.analyze_image(sample)
    print(analysis)
