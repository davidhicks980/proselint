"""Tests for misc.bureaucratese check."""

from proselint.checks.misc.bureaucratese import check

from .conftest import assert_fail, assert_pass


def test():
    """Basic smoke test for misc.bureaucratese."""
    assert_pass(check, "Smoke phrase with nothing flagged.")
    assert_fail(check, "I hope the report meets with your approval.")
