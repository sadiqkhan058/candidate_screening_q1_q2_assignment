from bot import respond


def check(market, user_input, expected_words):
    answer = respond(market, user_input)

    print(f"\n[{market}]")
    print(f"Customer: {user_input}")
    print(f"Bot: {answer}")

    answer_lower = answer.lower()

    for word in expected_words:
        assert word.lower() in answer_lower, (
            f"Expected '{word}' in response"
        )

    print("PASS")


def main():
    # Philippines
    check(
        "philippines",
        "magkano ang premium?",
        ["premium", "representative"]
    )

    check(
        "philippines",
        "What is a beneficiary?",
        ["beneficiary"]
    )

    check(
        "philippines",
        "What is covered by my policy?",
        ["insurance", "representative"]
    )

    # Indonesia
    check(
        "indonesia",
        "berapa angsuran saya?",
        ["angsuran", "petugas"]
    )

    check(
        "indonesia",
        "What is my loan qualification?",
        ["loan", "representative"]
    )

    check(
        "indonesia",
        "Saya ingin informasi tentang pinjaman.",
        ["pinjaman", "petugas"]
    )

    print("\nAll Q3 automated tests passed.")


if __name__ == "__main__":
    main()
