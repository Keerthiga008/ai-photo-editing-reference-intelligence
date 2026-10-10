from __future__ import annotations

import cv2
import numpy as np


class FrequencySeparationEngine:
    """Frequency separation for tone and texture control in portrait enhancement."""

    @staticmethod
    def split_frequencies(image_rgb32: np.ndarray, blur_sigma: float = 3.0):
        low_frequency = cv2.GaussianBlur(
            image_rgb32,
            (0, 0),
            sigmaX=blur_sigma,
            sigmaY=blur_sigma,
            borderType=cv2.BORDER_REFLECT,
        )
        high_frequency = (image_rgb32 - low_frequency) + 0.5
        high_frequency = np.clip(high_frequency, 0.0, 1.0)
        return low_frequency, high_frequency

    @staticmethod
    def recombine_frequencies(low_freq: np.ndarray, high_freq: np.ndarray) -> np.ndarray:
        reconstructed = (high_freq - 0.5) + low_freq
        return np.clip(reconstructed, 0.0, 1.0)
