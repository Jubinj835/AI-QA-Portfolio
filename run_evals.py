import subprocess
import sys


def run_evaluation_suite():
    # Complete list of all evaluation test files in your portfolio suite
    test_files = [
        "tests/lesson1_test.py",
        "tests/lesson2_deepEval_test.py",
        "tests/lesson3_faithfulness_test.py"
    ]

    print("🚀 Starting Local AI QA Evaluation Suite...")

    for test_file in test_files:
        print(f"\n--------------------------------------------------")
        print(f"Running evaluation: {test_file}")
        print(f"--------------------------------------------------")

        # Executes pytest safely using your active Python 3.12 environment interpreter
        result = subprocess.run([sys.executable, "-m", "pytest", test_file, "-v"])

        if result.returncode != 0:
            print(f"❌ Evaluation failed in: {test_file}")
        else:
            print(f"✅ Evaluation passed successfully in: {test_file}")

    print("\n🎉 Evaluation suite complete!")


if __name__ == "__main__":
    run_evaluation_suite()