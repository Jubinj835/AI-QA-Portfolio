import os
os.environ["DEEPEVAL_PER_ATTEMPT_TIMEOUT_SECONDS_OVERRIDE"] = "300"

from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.models import OllamaModel

def test_customer_relevancy():
    #1. Define Local Model
    local_model = OllamaModel(model = "deepseek-r1:1.5b")
    #2. Define the Testcase
    test_case = LLMTestCase(
        input = "How can I Cancel my order?",
        actual_output = "You can cancel your order from your account dashboard before it ships."
    )
    #3. Define the Metric
    metric = AnswerRelevancyMetric(threshold=0.67,model=local_model)
    #4. Run Evaluation
    assert_test(test_case, [metric])
