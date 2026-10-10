# AI-Powered Professional Photo Editing & Reference Intelligence

This repository is the technical foundation for an AI-assisted desktop workflow built for wedding, portrait, and event photography production. It combines image analysis, reference-driven style matching, adaptive enhancement, and Photoshop integration.

## Project intent

The application is designed to help professional photographers:

- import large event and portrait photo sets
- analyze individual images for lighting, exposure, and scene quality
- match each image to a relevant reference profile
- create a non-destructive editing plan before applying changes
- preserve natural skin tones and realistic detail
- batch-process high-volume jobs efficiently
- hand off selected photos to Adobe Photoshop for final refinement and export

## Repository architecture

```text
ai-photo-editing-reference-intelligence/
├── app/
├── core/
├── src/
│   ├── client_ui/
│   ├── backend_core/
│   ├── ai_engine/
│   ├── image_core/
│   └── ps_bridge/
├── server/
├── docs/
├── tests/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── technical_project_brief_and_system_architecture.md
```

## Current implementation status

This repository currently includes:

- a Windows desktop app shell
- starter image-processing functions
- a Photoshop integration stub
- a basic orchestration structure aligned with the proposed system architecture

## Planned milestones

1. Proof of concept over a representative wedding and portrait dataset
2. Image analysis and classification engine
3. Reference intelligence and stylistic matching
4. Non-destructive enhancement pipeline
5. Photoshop bridge and handoff workflow
6. Quality assurance, performance optimization, and pilot deployment

## Development direction

The architecture follows a modular design:

- `src/client_ui` for interactive review and editing workflows
- `src/backend_core` for queueing, processing orchestration, and persistence
- `src/ai_engine` for scene classification and vector matching
- `src/image_core` for color science, frequency separation, and enhancement engines
- `src/ps_bridge` for Photoshop-driven handoff and automation
- `server` for optional cloud metadata and reference harvesting services

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main
```

## Notes

This is an initial implementation foundation. It is intentionally modular and extensible so it can evolve into the full technical specification described in the project brief.
