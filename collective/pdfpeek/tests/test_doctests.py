# -*- coding: utf-8 -*-
"""Fix other people's missing docstrings."""

from collective.pdfpeek import testing
from plone.testing import layered
import doctest
import unittest as unittest

integration_tests = [
    'integration.txt'
]
functional_tests = [
]


def test_suite():
    """Fix other people's missing docstrings."""
    return unittest.TestSuite(
        [layered(doctest.DocFileSuite('tests/{0:s}'.format(f),
                                      package='collective.pdfpeek',
                                      optionflags=testing.optionflags),
                 layer=testing.PDFPEEK_AT_INTEGRATION_TESTING)
            for f in integration_tests] +
        [layered(doctest.DocFileSuite('tests/{0:s}'.format(f),
                                      package='collective.pdfpeek',
                                      optionflags=testing.optionflags),
                 layer=testing.PDFPEEK_AT_FUNCTIONAL_TESTING)
            for f in functional_tests]
    )
