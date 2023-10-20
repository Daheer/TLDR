from TLDR.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class Prediction:
  def __init__(self):
    self.config = ConfigurationManager().get_model_evaluation_config()

  def predict(self, text):
    tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
    gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
    pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
    print("Dialogue:\n", text)

    summary = pipe(text, **gen_kwargs)[0]['summary_text']
    print("\nSummary:\n", summary)
    return summary    