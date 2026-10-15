import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)

# Cache Keys
PERFORMANCE_REPORT_CACHE_KEY = "analytics:performance_report"
TASK_METRICS_CACHE_KEY = "analytics:task_metrics"

# Time To Live (TTL) constants in seconds
CACHE_TTL_5_MINUTES = 300
CACHE_TTL_1_HOUR = 3600


def get_cached_performance_report():
    """Fetches the cached performance report from Redis."""
    try:
        return cache.get(PERFORMANCE_REPORT_CACHE_KEY)
    except Exception as e:
        logger.warning(f"Cache get failed: {e}")
        return None


def set_cached_performance_report(data, timeout=CACHE_TTL_5_MINUTES):
    """Saves the performance report to Redis with a TTL."""
    try:
        cache.set(PERFORMANCE_REPORT_CACHE_KEY, data, timeout=timeout)
    except Exception as e:
        logger.warning(f"Cache set failed: {e}")


def invalidate_performance_cache():
    """Invalidates/deletes cached reports when new tasks or projects are modified."""
    try:
        cache.delete(PERFORMANCE_REPORT_CACHE_KEY)
        cache.delete(TASK_METRICS_CACHE_KEY)
        logger.info("[CACHE] Invalidation successful for analytics reports.")
    except Exception as e:
        logger.warning(f"Cache invalidation failed: {e}")
