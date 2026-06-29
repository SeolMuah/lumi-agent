"""
시간 / 날짜 유틸리티

방송 일정 안내 등에서 사용할 한국 시간(KST) 변환·포맷 헬퍼 모음입니다.

사용법:
    from app.core.time_utils import format_kst, seconds_until

    text = format_kst(broadcast_at)
    remain = seconds_until(broadcast_at)
"""

from datetime import datetime, timedelta, timezone


def to_kst(dt):
    """datetime을 한국 시간(KST, UTC+9)으로 변환합니다."""
    kst = timezone(timedelta(hours=9))
    return dt.astimezone(kst)


def format_kst(dt):
    """datetime을 'YYYY-MM-DD HH:MM' 형식의 한국 시간 문자열로 변환합니다."""
    return to_kst(dt).strftime("%Y-%m-%d %H:%M")


def seconds_until(target):
    """현재 시각부터 target까지 남은 시간을 초 단위로 반환합니다."""
    now = datetime.now()
    return int((target - now).total_seconds())
