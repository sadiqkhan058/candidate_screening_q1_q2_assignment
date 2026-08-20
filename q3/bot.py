from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_knowledge(market):
    path = BASE_DIR / market / "knowledge.md"

    if not path.exists():
        raise FileNotFoundError(f"Knowledge base not found: {path}")

    return path.read_text(encoding="utf-8")


def get_market_knowledge(market):
    market = market.lower().strip()

    if market not in {"philippines", "indonesia"}:
        raise ValueError("Market must be 'philippines' or 'indonesia'")

    return load_knowledge(market)


def detect_language(text):
    """
    Simple language detection for the prototype.
    This is intentionally rule-based.
    """
    text_lower = text.lower()

    filipino_words = {
        "magkano", "salamat", "ako", "ko", "mo", "ang",
        "mga", "para", "hindi", "opo", "po", "pwede",
        "gusto", "kailangan"
    }

    indonesian_words = {
        "berapa", "saya", "anda", "yang", "untuk",
        "tidak", "bisa", "mau", "ingin", "terima",
        "kasih", "angsuran", "pinjaman"
    }

    words = set(text_lower.split())

    if words.intersection(filipino_words):
        return "filipino"

    if words.intersection(indonesian_words):
        return "indonesian"

    return "english"


def respond_philippines(text):
    language = detect_language(text)
    text_lower = text.lower()

    if "premium" in text_lower or "magkano" in text_lower:
        if language == "filipino":
            return (
                "Para sa exact premium, kailangan nating i-check "
                "ang policy details. I can connect you with a representative "
                "para sa tamang amount."
            )

        return (
            "I don't want to guess the premium amount. "
            "A representative can check the exact policy details for you."
        )

    if "coverage" in text_lower or "sakop" in text_lower:
        if language == "filipino":
            return (
                "Para malaman kung ano ang covered ng policy, "
                "kailangan nating tingnan ang specific policy details. "
                "I can connect you with a representative."
            )

        return (
            "Coverage depends on the specific policy. "
            "I can connect you with a representative to confirm the details."
        )

    if "beneficiary" in text_lower:
        return (
            "A beneficiary is the person or party designated "
            "to receive the applicable policy benefit."
        )

    return (
        "I can help with life insurance and bancassurance questions. "
        "If the information is not available here, I can connect you "
        "with a representative."
    )


def respond_indonesia(text):
    language = detect_language(text)
    text_lower = text.lower()

    if "angsuran" in text_lower or "installment" in text_lower:
        if language == "indonesian":
            return (
                "Untuk detail angsuran yang tepat, saya perlu memeriksa "
                "informasi pembiayaan Anda. Saya bisa membantu menghubungkan "
                "Anda dengan petugas."
            )

        return (
            "For the exact installment amount, "
            "a representative needs to check the financing details."
        )

    if "pinjaman" in text_lower or "loan" in text_lower:
        if language == "indonesian":
            return (
                "Untuk kualifikasi pinjaman, saya tidak ingin memberikan "
                "informasi yang belum terverifikasi. Saya bisa menghubungkan "
                "Anda dengan petugas."
            )

        return (
            "For loan qualification, I don't want to provide "
            "unverified information. I can connect you with a representative."
        )

    return (
        "Saya dapat membantu mengenai consumer finance dan multifinance. "
        "Jika informasinya tidak tersedia, saya dapat menghubungkan "
        "Anda dengan petugas."
    )


def respond(market, text):
    market = market.lower().strip()

    if market == "philippines":
        return respond_philippines(text)

    if market == "indonesia":
        return respond_indonesia(text)

    raise ValueError("Market must be 'philippines' or 'indonesia'")


if __name__ == "__main__":
    print("Q3 Native-Language Voice Bot")
    print("Type 'exit' to stop.\n")

    market = input("Market (philippines/indonesia): ").strip().lower()

    if market not in {"philippines", "indonesia"}:
        print("Invalid market.")
        raise SystemExit(1)

    # Load KB to verify it exists.
    get_market_knowledge(market)

    print(f"\nLoaded {market} knowledge base.")
    print("Start chatting.\n")

    while True:
        user_input = input("Customer: ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        answer = respond(market, user_input)
        print(f"Bot: {answer}\n")
