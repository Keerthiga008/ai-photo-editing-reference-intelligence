from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class JobStatus:
    job_id: str
    status: str = "queued"
    progress: float = 0.0


class PipelineOrchestrator:
    """Simple processing orchestration scaffold."""

    def __init__(self):
        self.jobs: dict[str, JobStatus] = {}

    def enqueue(self, job_id: str) -> JobStatus:
        status = JobStatus(job_id=job_id, status="queued", progress=0.0)
        self.jobs[job_id] = status
        return status

    def update(self, job_id: str, status: str, progress: float) -> JobStatus:
        item = self.jobs.get(job_id)
        if item is None:
            item = JobStatus(job_id=job_id)
            self.jobs[job_id] = item
        item.status = status
        item.progress = max(0.0, min(progress, 100.0))
        return item

    def get_job(self, job_id: str) -> JobStatus | None:
        return self.jobs.get(job_id)

    def list_jobs(self) -> List[JobStatus]:
        return list(self.jobs.values())
