from __future__ import annotations

from metric_contract_check.models import Rule

PROJECT_NAME = 'metric-contract-check'
DESCRIPTION = 'Validate metric names and event contracts before analytics changes ship.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'event: checkout.failed metric missing owner and unit dollars_total'
MEDIUM_SAMPLE = '\\b(dollar|usd|eur|amount|revenue)\\b(?!.*\\bunit\\b)'
CLEAN_SAMPLE = 'event: checkout_completed owner: analytics unit: count tags: region,plan'

RULES = (
    Rule(
        code='missing-owner',
        severity='high',
        pattern='\\b(missing owner|owner\\s*:\\s*$|owner\\s*:\\s*unknown)\\b',
        message='metric ownership is missing',
        recommendation='Assign an owning team before accepting the metric.',
    ),
    Rule(
        code='currency-unit-risk',
        severity='medium',
        pattern='\\b(dollar|usd|eur|amount|revenue)\\b(?!.*\\bunit\\b)',
        message='money metric may not declare units',
        recommendation='Declare currency and scale explicitly.',
    ),
    Rule(
        code='high-cardinality-tag',
        severity='low',
        pattern='\\b(user_id|email|session_id|request_id)\\b',
        message='high-cardinality tag detected',
        recommendation='Remove per-user tags or route to logs instead of metrics.',
    ),
)
