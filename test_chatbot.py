
from chatbot import FAQChatbot


def test_chatbot():
    bot = FAQChatbot(threshold=0.40)

    test_cases = [
        {
            "question": "How can I apply for admission?",
            "expected_category": "Admissions",
            "should_match": True,
        },
        {
            "question": "I forgot my password",
            "expected_category": "Technical Support",
            "should_match": True,
        },
        {
            "question": "Where can I check my exam timetable?",
            "expected_category": "Examinations",
            "should_match": True,
        },
        {
            "question": "What is the weather on Mars?",
            "expected_category": None,
            "should_match": False,
        },
    ]

    passed = 0

    for case in test_cases:
        result = bot.get_response(case["question"])

        correct_match = result["matched"] == case["should_match"]

        correct_category = (
            case["expected_category"] is None
            or result["category"] == case["expected_category"]
        )

        success = correct_match and correct_category

        print(f"\nQuestion: {case['question']}")
        print(f"Matched: {result['matched']}")
        print(f"Category: {result['category']}")
        print(f"Similarity: {result['score']}")
        print("Result:", "PASS" if success else "FAIL")

        if success:
            passed += 1

    print(f"\nFinal result: {passed}/{len(test_cases)} tests passed.")


if __name__ == "__main__":
    test_chatbot()
