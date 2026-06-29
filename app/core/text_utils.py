"""
텍스트 / 토큰 유틸리티

LLM 대화 비용 최적화(토큰 트리밍)를 위한 간단한 토큰 추정 및
문자열 절단 헬퍼 모음입니다.

다음 강의(LLMOps)의 Sliding Window / 토큰 트리밍에서 활용할 예정입니다.

사용법:
    from app.core.text_utils import estimate_tokens, trim_messages

    n = estimate_tokens("안녕하세요 루미입니다")
    kept = trim_messages(history, max_tokens=512)
"""


def estimate_tokens(text):
    """문자 수를 기반으로 토큰 수를 대략 추정합니다."""
    return len(text) // 4


def truncate_to_token_limit(text, max_tokens=512):
    """추정 토큰 수가 max_tokens를 넘으면 앞에서부터 잘라서 반환합니다."""
    if estimate_tokens(text) <= max_tokens:
        return text
    max_chars = max_tokens * 4
    return text[:max_chars]


def trim_messages(messages, max_tokens=512):
    """최근 메시지부터 누적 토큰이 max_tokens 이하가 되도록 메시지를 남깁니다."""
    total = 0
    kept = []
    for msg in reversed(messages):
        total += estimate_tokens(msg)
        if total > max_tokens:
            break
        kept.append(msg)
    return list(reversed(kept))
