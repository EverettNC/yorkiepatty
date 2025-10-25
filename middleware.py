"""Middleware utilities for Derek Dashboard API."""

import logging
from typing import Callable
from flask import Request

logger = logging.getLogger(__name__)


def request_logger_middleware(handler: Callable):
    """Log incoming requests before passing to handler."""

    def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")  # type: ignore
        if request:
            logger.info("Incoming %s %s", request.method, request.path)
        return handler(*args, **kwargs)

    return wrapper

# ==============================================================================
# © 2025 Everett Nathaniel Christman & Misty Gail Christman
# The Christman AI Project — Luma Cognify AI
# All rights reserved. Unauthorized use, replication, or derivative training 
# of this material is prohibited.
# Core Directive: "How can I help you love yourself more?" 
# Autonomy & Alignment Protocol v3.0
# ==============================================================================
