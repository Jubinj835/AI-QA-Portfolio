import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.models.llms.ollama_model import OllamaModel

def test_edgecase_answer_relevancy():
    # 1. Define Local Model
    local_ai_model = OllamaModel(model="deepseek-r1:1.5b")
    # 2. Define a trickier test case with extra fluff or indirect wording
    test_case = LLMTestCase(
        input = "Can I get my money back if I changed my mind after two weeks? ",
        actual_output = "Our policy states that refunds are accepted within 30 days of purchase, provided you have the receipt."
    )

    metric = AnswerRelevancyMetric(
        threshold=0.8,
        model=local_ai_model,
        include_reason=True
    )
    # Manually measure the metric instead of just asserting
    metric.measure(test_case)

    print(f"\n--- DEEPEVAL DEBUG INFO ---")
    print(f"Score: {metric.score}")
    print(f"Reason: {metric.reason}")

    # Then assert
    assert metric.score >= metric.threshold
