from __future__ import annotations

import cv2
import numpy as np


def smoke_test() -> None:
    image = np.zeros((64, 64, 3), dtype=np.uint8)
    assert image.shape == (64, 64, 3)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    assert gray.shape == (64, 64)


if __name__ == "__main__":
    smoke_test()
    print("Smoke test passed.")
