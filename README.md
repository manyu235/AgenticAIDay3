# Prompt Quality Scoring Agent

A LangChain-based agent that evaluates prompt quality based on 5 criteria and provides actionable feedback.

## Features

- Evaluates prompts on 5 quality criteria
- Assigns scores out of 10 for each criterion
- Calculates final average score
- Provides improvement suggestions
- JSON-compatible output format

## Evaluation Criteria

1. **Clarity (0-10)**: Is the prompt easy to understand with a clear goal?
2. **Specificity (0-10)**: Are sufficient details and requirements provided?
3. **Context (0-10)**: Is background information, audience, or use case mentioned?
4. **Output Format (0-10)**: Is expected output format, tone, or length specified?
5. **Persona (0-10)**: Is a specific role assigned in the prompt?

**Final Score**: Average of all 5 criteria scores

## Requirements

Install required packages:

```bash
pip install langchain-ollama langchain-core
```

Install Ollama and pull the model:

```bash
ollama pull gemma3:latest
```

## Usage

### Interactive Mode

Run the main script:

```bash
python prompt_scorer.py
```

1. Enter `score` to evaluate a prompt
2. Paste your prompt text
3. Type `###END###` on a new line when finished
4. View the evaluation results

### Test Suite

Run all 10 test prompts:

```bash
python test_prompts.py
```

This will evaluate 10 sample prompts ranging from very poor to excellent quality.

## Output Format

The agent provides:

- Individual scores for each criterion (0-10)
- Final average score (0-10)
- Brief explanation of the evaluation
- 2-3 suggestions for improvement

Example output:

```
Scores:
Clarity: 8/10
Specificity: 7/10
Context: 6/10
Output Format: 9/10
Persona: 9/10

Final Score: 7.8/10

Explanation:
The prompt has a clear role and output format specification, but could benefit from more context about the target audience.

Suggestions:
1. Add more details about the target audience demographics
2. Specify the expected length or word count
3. Include examples of desired tone or style
```

## Test Prompts

The `test_prompts.py` file includes 10 test cases:

1. Very Poor Prompt - Minimal information
2. Poor Prompt - No specifics
3. Below Average - Some details
4. Average - Has role and topic
5. Good - Has role, topic, and audience
6. Very Good - Multiple elements
7. Excellent - All elements present
8. Excellent - Comprehensive prompt
9. Good - Clear but missing some details
10. Average - Has goal but lacks structure

## Project Structure

```
day3/
├── prompt_scorer.py      # Main scoring agent
├── test_prompts.py       # Test suite with 10 prompts
└── README.md            # Documentation
```

## How It Works

1. Takes a text prompt as input
2. Sends it to LLM with evaluation criteria
3. LLM analyzes the prompt against 5 criteria
4. Returns structured JSON with scores and suggestions
5. Calculates final average score
6. Displays results to user

## License

MIT License
