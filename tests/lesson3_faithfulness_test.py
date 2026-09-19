import os
os.environ['DEEPEVAL_PER_ATTEMPT_TIMEOUT_SECONDS_OVERRIDE'] = '300';

from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.models import OllamaModel
from deepeval.metrics import FaithfulnessMetric

def test_faithfulness_metric():
    local_model = OllamaModel(model = "deepseek-r1:1.5b")

    test_case = LLMTestCase(
        input = "What is our return policy?",
        actual_output="You can return any item within 30 days of purchase with a receipt.",
        retrieval_context=["Our store policy allows returns up to 30 days after purchase provided you have the original receipt."]
    )

    metric = FaithfulnessMetric(threshold=0.7,model=local_model)

    assert_test(test_case, [metric])