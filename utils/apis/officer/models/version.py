from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class Version(BaseModel):
    manifestId: Optional[str] | None
    branch: Optional[str] | None
    version: Optional[str] | None
    buildVersion: Optional[str] | None
    engineVersion: Optional[str] | None
    riotClientVersion: Optional[str] | None
    riotClientBuild: Optional[str] | None
    buildDate: Optional[datetime] | None
