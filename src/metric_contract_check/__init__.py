"""Package entry points for metric-contract-check."""

from metric_contract_check.core import audit_records, read_records
from metric_contract_check.models import AuditReport, Finding, Rule

__all__ = ["AuditReport", "Finding", "Rule", "audit_records", "read_records"]
__version__ = "0.1.0"
