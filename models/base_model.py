#!/usr/bin/python3
"""Our BaseModel that defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime

class BaseModel:
    """contains common attribute"""
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()
