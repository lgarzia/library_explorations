# DSPy: Programming—not prompting—Foundation Models

- [DSPy YouTube](https://www.youtube.com/watch?v=CDung1LnLbY)
- [DSpy Conference Talk](https://www.youtube.com/watch?v=Dt3H2ninoeY)

per Bard:
Applications of DSPy:

- Question answering with chain-of-thought reasoning: Build systems that analyze retrieved texts, perform multi-step reasoning, and provide comprehensive answers.
- Data summarization with abstraction and summarization modules: Generate concise summaries of complex data by identifying key points and abstractive rephrasing.
- Customizable creative text generation: Control the style, tone, and content of generated text by composing appropriate modules and adjusting parameters.

- [ColBERTv2](https://github.com/stanford-futuredata/ColBERT):Function: Its primary purpose is to efficiently and effectively retrieve relevant documents from a large corpus of text based on a given query.
- [ragatouille](https://github.com/bclavie/ragatouille): RAGatouille's purpose is to bridge this gap: make it easy to use state-of-the-art methods in your RAG pipeline, without having to worry about the details or the years of literature!

---

[Medium - Jesus R.](https://medium.com/towards-artificial-intelligence/inside-dspy-the-new-language-model-programming-framework-you-need-to-know-about-88c65566903f):

- Alternative to LlamaIndex, LangChain, Semantic Kernel
  LMP (Language Model Programming)
- Declarative Layers Incorporate Desired Logic [ChainOfThought, Retrieve, Self Reflection]
- Key innovation is automatic compiler
- Signature: Crafting LLM Behaviors (Elucidate the nature of sub-task):
  - delineation of the sub-task:
  - elaboration of input fields
  - explanation of one or more output fields
- Enabling Program Optimization via dspy.teleprompt

---
