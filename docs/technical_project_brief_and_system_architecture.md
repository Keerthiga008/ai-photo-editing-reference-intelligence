# TECHNICAL PROJECT SPECIFICATION & SYSTEM ARCHITECTURE
## AI-Powered Professional Photo Editing, Reference Intelligence & Adobe Photoshop Integration

Repository standard: GitHub technical specification document
Status: approved for implementation (v1.0.0-proposal)
Target platform: Windows 10/11 x64
Runtime targets: Python 3.11+, OpenCV / NumPy, optional C++20 sidecar, Adobe Photoshop CC and modern desktop workflows

## 1. Executive summary

This repository provides the technical blueprint for an AI-assisted desktop photo post-production system tailored to wedding, portrait, and event photography.

The software should analyse each photograph, classify its scene and lighting, match the image to a curated set of reference styles, generate an editable decision plan, and apply adaptive enhancements while preserving the original file and keeping Photoshop available for final professional refinement.

## 2. Primary system topology

```text
+--------------------------------------------------------+
| Windows 10/11 client workstation                       |
|                                                        |
| +-----------------------+ +--------------------------+ |
| | Frontend UI           | | Review and batch view    | |
| | PySide6 / Qt desktop  | | Before / after viewport  | |
| +----------+------------+ +------------+-----------+ |
|            |                              |                 |
|            v                              v                 |
| +-----------------------+  +---------------------------+ |
| | Backend orchestration |  | Local SQLite metadata     | |
| | pipeline manager      |  | & reference index store   | |
| +----------+------------+  +---------------------------+ |
|            |                                                |
|            v                                                |
| +-----------------------+ +-----------------------------+ |
| | AI inference engine   | | Image processing engine     | |
| | ONNX / DirectML /     | | OpenCV / Pillow / numpy    | |
| | segmentation models   | | color science & filters    | |
| +----------+------------+ +-------------+---------------+ |
|            |                              |                   |
|            v                              v                   |
| +--------------------------------------------------------+ |
| | Photoshop bridge                                      | |
| | open files, script handoff, layer-ready export        | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+
```

## 3. Functional architecture

### 3.1 Desktop front end

Responsible for:

- project creation and import
- batch queue display
- reference library browsing
- before/after comparison
- QC review dashboard
- photoshop handoff controls

Suggested stack:

- Python 3.11+
- PySide6 / Qt
- QOpenGLWidget for review surfaces where needed

### 3.2 Orchestration core

Responsible for:

- job scheduling
- memory budgeting
- pipeline execution
- database persistence
- project state transitions
- retries and error recovery

### 3.3 AI engine

Responsible for:

- scene classification
- face and subject detection
- lighting and exposure estimation
- reference similarity search
- quality-risk detection

### 3.4 Image core

Responsible for:

- exposure correction
- white balance adjustment
- local tonal balancing
- subtle retouching
- colour grading
- frequency separation for texture preservation
- safe non-destructive output generation

### 3.5 Photoshop bridge

Responsible for:

- verifying Photoshop availability
- passing approved outputs to Photoshop
- creating PSD or TIFF working files
- preserving editable file handoff for final post-production

## 4. Repository structure

```text
ai-photo-editing-reference-intelligence/
├── app/
│   ├── __init__.py
│   └── main.py
├── core/
│   ├── __init__.py
│   ├── image_processing.py
│   └── photoshop_integration.py
├── src/
│   ├── client_ui/
│   │   └── app_window.py
│   ├── backend_core/
│   │   ├── __init__.py
│   │   ├── db_manager.py
│   │   └── pipeline/
│   │       ├── __init__.py
│   │       └── orchestrator.py
│   ├── ai_engine/
│   │   ├── __init__.py
│   │   └── faiss_index.py
│   ├── image_core/
│   │   ├── __init__.py
│   │   └── frequency_sep.py
│   └── ps_bridge/
│       ├── __init__.py
│       └── bridge_controller.py
├── server/
│   └── main.py
├── docs/
│   └── technical_project_brief_and_system_architecture.md
├── tests/
│   └── test_core_modules.py
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── README.md
└── technical_project_brief_and_system_architecture.md
```

## 5. Core data model

The application should store project metadata in SQLite while keeping file assets on disk.

```sql
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    base_color_space TEXT DEFAULT 'ACEScc',
    scratch_disk_path TEXT NOT NULL
);

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
);

CREATE TABLE IF NOT EXISTS classifications (
    asset_id TEXT PRIMARY KEY REFERENCES media_assets(id) ON DELETE CASCADE,
    scene_category TEXT,
    lighting_type TEXT,
    indoor_outdoor_prob REAL,
    face_count INTEGER DEFAULT 0,
    primary_subject_bbox JSON,
    histogram_metrics JSON,
    quality_flags JSON
);

CREATE TABLE IF NOT EXISTS reference_profiles (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    source_type TEXT,
    source_uri TEXT,
    embedding_vector BLOB,
    target_palette JSON,
    target_skin_lab JSON,
    textual_instructions TEXT
);

CREATE TABLE IF NOT EXISTS edit_plans (
    asset_id TEXT PRIMARY KEY REFERENCES media_assets(id) ON DELETE CASCADE,
    reference_id TEXT REFERENCES reference_profiles(id),
    status TEXT DEFAULT 'PENDING',
    plan_parameters JSON NOT NULL,
    qc_warning_flags JSON,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 6. Core pipeline stages

1. Import and validate files
2. Image analysis and lighting estimation
3. Subject classification and detection
4. Reference matching
5. Edit plan generation
6. Technical correction
7. Selective enhancement and retouching
8. Adaptive color grading
9. Quality assessment
10. Human review
11. Photoshop handoff
12. Final export

## 7. Engineering guidelines

- Never overwrite original files by default.
- Maintain non-destructive intermediate assets.
- Keep metadata on every processed image.
- Separate project-level styling from image-level correction values.
- Treat each image as a unique decision, while preserving album consistency.
- Use explicit human approval gates before final export.

## 8. MVP scope

The May 2026 MVP should include:

- Windows desktop application shell
- local project management
- photo upload and folder import
- automatic image classification
- reference library management
- exposure and white balance correction
- basic skin-tone protection and detail enhancement
- batch processing queue
- before/after preview
- Photoshop-compatible output handoff
- JPEG/TIFF export

## 9. Risks and safeguards

- RAW compatibility must be validated by camera model.
- External social media or video references may be blocked or restricted.
- Photoshop automation APIs vary by version and OS configuration.
- Performance must be monitored under large photo batches.
- User approval must remain central to final output decisions.

## 10. Implementation status

The repository now contains a starter foundation for the following modules:

- `app/main.py` – desktop application shell
- `core/image_processing.py` – image analysis and enhancement utilities
- `core/photoshop_integration.py` – Photoshop detection and handoff stub
- `src/backend_core/db_manager.py` – project metadata access layer
- `src/backend_core/pipeline/orchestrator.py` – processing orchestration scaffold
- `src/image_core/frequency_sep.py` – frequency separation foundation
- `src/ps_bridge/bridge_controller.py` – bridge interface contract
- `server/main.py` – optional service entry point

This structured starter is intended to support the implementation of the full technical architecture described in this specification.
