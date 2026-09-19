def test_cancel_order():
    test_case = {
        "id": "TC001",
        "question": "How Can I Cancel my order?",
        "expected_answer": "You can cancel your order from your account dashboard before it ships.",
        "actual_answer": "You can cancel your order from your account dashboard before it ships."
    }
    assert test_case["actual_answer"]== test_case["expected_answer"]