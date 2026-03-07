#!/usr/bin/env python3
"""Run tests for telegram_api package."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Run a command and print the result."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print('='*60)

    result = subprocess.run(cmd, capture_output=False)

    if result.returncode != 0:
        print(f"\n❌ {description} failed!")
        return False
    else:
        print(f"\n✅ {description} passed!")
        return True


def main():
    """Run all tests."""
    print("Telegram API Package Test Runner")
    print("="*60)

    # Change to the telegram_api directory
    api_dir = Path(__file__).parent
    tests_dir = api_dir / "tests"

    if not tests_dir.exists():
        print(f"❌ Tests directory not found: {tests_dir}")
        sys.exit(1)

    # Check if pytest is available
    try:
        import pytest
        pytest_available = True
    except ImportError:
        pytest_available = False
        print("⚠️  pytest not installed. Install with: pip install pytest")

    if pytest_available:
        # Run pytest
        success = run_command(
            [sys.executable, "-m", "pytest", "tests/", "-v"],
            "Running pytest"
        )

        if not success:
            sys.exit(1)

        print("\n" + "="*60)
        print("Running specific test categories...")
        print("="*60)

        # Run unit tests
        run_command(
            [sys.executable, "-m", "pytest", "tests/", "-v", "-m", "unit"],
            "Unit tests"
        )

        # Run integration tests
        run_command(
            [sys.executable, "-m", "pytest", "tests/", "-v", "-m", "integration"],
            "Integration tests"
        )
    else:
        # Run tests directly
        print("\nRunning tests without pytest...")

        test_files = list(tests_dir.glob("test_*.py"))
        if not test_files:
            print("❌ No test files found!")
            sys.exit(1)

        all_passed = True
        for test_file in sorted(test_files):
            success = run_command(
                [sys.executable, str(test_file)],
                f"Running {test_file.name}"
            )
            if not success:
                all_passed = False

        if not all_passed:
            sys.exit(1)

    print("\n" + "="*60)
    print("✅ All tests completed!")
    print("="*60)


if __name__ == "__main__":
    main()
