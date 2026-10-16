
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import FAQ_DATA


class FAQChatbot:

    def __init__(self, threshold=0.45):
        self.threshold = threshold

        # Store every main question and its alternative phrasings.
        self.questions = []
        self.faq_indices = []

        for index, faq in enumerate(FAQ_DATA):
            all_phrasings = [
                faq["question"],
                *faq["alternatives"]
            ]

            for phrasing in all_phrasings:
                self.questions.append(phrasing)
                self.faq_indices.append(index)

        # Convert FAQ text into numerical TF-IDF vectors.
        
        self.vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        strip_accents="unicode",
        stop_words="english"
)


        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    @staticmethod
    def clean_text(text):
        """Normalize user input before matching."""
        text = text.lower().strip()
        text = re.sub(r"[^\w\s]", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text

    def get_response(self, user_question):
        """Find the closest FAQ and return its answer."""

        cleaned_question = self.clean_text(user_question)

        if not cleaned_question:
            return {
                "answer": "Please enter a question.",
                "category": "General",
                "score": 0.0,
                "matched_question": None,
                "matched": False
            }

        # Convert the user's question using the same vectorizer.
        user_vector = self.vectorizer.transform(
            [cleaned_question]
        )

        # Compare the user's question against all FAQ phrasings.
        similarities = cosine_similarity(
            user_vector,
            self.question_vectors
        )[0]

        best_index = similarities.argmax()
        best_score = float(similarities[best_index])

        faq_index = self.faq_indices[best_index]
        matched_faq = FAQ_DATA[faq_index]

        # Reject weak matches instead of giving an unreliable answer.
        if best_score < self.threshold:
            return {
                "answer": (
                    "Sorry, I couldn't find a reliable answer to "
                    "that question. Please try rephrasing it or "
                    "contact the relevant college department."
                ),
                "category": "General",
                "score": round(best_score, 3),
                "matched_question": None,
                "matched": False
            }

        return {
            "answer": matched_faq["answer"],
            "category": matched_faq["category"],
            "score": round(best_score, 3),
            "matched_question": matched_faq["question"],
            "matched": True
        }
