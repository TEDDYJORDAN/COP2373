import re
import time
# List of spam keywords
spam_keywords = ["buy now", "free", "limited time", "click here", "subscribe",
                 "win", "winner", "prize", "order now", "urgent", "act now",
                 "apply now", "cheap", "best price", "congratulations",
                 "exclusive", "risk-free", "guaranteed", "save big",
                 "special promotion", "money", "offer expires", "lowest price",
                 "miracle", "100% free", "no cost", "trial", "rich",
                 "instant", "cash bonus"]
def make_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time elapsed was', t2 - t1)
        return ret_val

    return wrapper
@make_timer
def scan_email_for_spam(email_message):
    spam_score = 0
    detected_keywords = []
    for keyword in spam_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', email_message, re.IGNORECASE):
            occurrences = len(re.findall(r'\b' + re.escape(keyword) + r'\b', email_message, re.IGNORECASE))
            spam_score += occurrences
            detected_keywords.append((keyword, occurrences))

    # Simulate some processing time
    time.sleep(2)
    return spam_score, detected_keywords

def eval_spam_score(spam_score):
    if spam_score == 0:
        likelihood = "Not Spam"
    elif 1 <= spam_score <= 5:
        likelihood = "Unlikely to be Spam"
    elif 6 <= spam_score <= 10:
        likelihood = "Possibly Spam"
    elif 11 <= spam_score <= 15:
        likelihood = "Likely Spam"
    else:
        likelihood = "Highly Likely Spam"
    return likelihood

def main():
    print("Enter your email content:")
    email_message = input()

    spam_score, detected_keywords = scan_email_for_spam(email_message)
    likelihood = eval_spam_score(spam_score)

    print("\nSpam result")
    print(f"Spam score: {spam_score}")
    print(f"Likelihood of spam: {likelihood}")
    print("Detected keywords and phrases:")
    for keyword, count in detected_keywords:
        print(f"- {keyword}: {count} occurrence(s)")

if __name__ == "__main__":
    main()