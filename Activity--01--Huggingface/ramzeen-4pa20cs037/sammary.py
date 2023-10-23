from transformers import pipeline

def summarize_text(text, max_length=50):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=10, do_sample=False)[0]['summary_text']
    return summary

# Example usage
long_text =input()

short_summary = summarize_text(long_text, max_length=100)
print(short_summary)
