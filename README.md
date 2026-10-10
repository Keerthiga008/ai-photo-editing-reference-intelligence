# AI-Powered Professional Photo Editing & Reference Intelligence

This repository contains the initial architecture and starter implementation for an AI-powered desktop application for professional photo editing, reference intelligence, and Adobe Photoshop handoff.

## Overview

The project is designed for wedding, portrait, and event photography workflows. It combines:

- image classification and quality analysis
- reference-based editing style matching
- adaptive exposure, white balance, and colour correction
- skin-tone protection and detail enhancement
- Photoshop-ready output handoff
- batch processing and project-level consistency

## MVP Focus

- Windows desktop application foundation
- batch photo import and project organisation
- image quality and lighting analysis
- editable reference metadata and image library
- adaptive photo enhancement pipeline
- Photoshop integration stub for direct handoff

## Repository Layout

- `app/` – application entry points and UI shell
- `core/` – image processing, analysis, and Photoshop integration logic
- `data/` – project assets, references, and export folders
- `requirements.txt` – Python dependencies

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```

## Planned Modules

- photo import and validation
- classification and scene analysis
- reference intelligence engine
- editing plan generation
- non-destructive enhancement workflow
- Photoshop handoff
- export and QA review

## Current Status

This repo includes a starter foundation for the core image processing and Photoshop integration layer, which can be extended into the full desktop application.
