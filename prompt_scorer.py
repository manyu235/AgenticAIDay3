from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import json

llm = ChatOllama(model="gemma3:latest")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are a prompt quality evaluator. Analyze prompts based on 5 criteria and provide scores.

Criteria:
1. Clarity (0-10): Is the prompt easy to understand with a clear goal?
2. Specificity (0-10): Are sufficient details and requirements provided?
3. Context (0-10): Is background information, audience, or use case mentioned?
4. Output Format (0-10): Is expected output format, tone, or length specified?
5. Persona (0-10): Is a specific role assigned in the prompt?

You must return your response in valid JSON format with this exact structure:
{
  "clarity": number,
  "specificity": number,
  "context": number,
  "output_format": number,
  "persona": number,
  "final_score": number,
  "explanation": "string",
  "suggestions": ["string1", "string2", "string3"]
}

Do not include any text outside the JSON object."""),
    ("human", "Evaluate this prompt:\n\n{prompt_text}")
])

def score_prompt(prompt_text):
    try:
        formatted_prompt = prompt_template.format(prompt_text=prompt_text)
        response = llm.invoke(formatted_prompt)
        
        try:
            result = json.loads(response.content)
            if "final_score" not in result:
                scores = [
                    result.get("clarity", 0),
                    result.get("specificity", 0),
                    result.get("context", 0),
                    result.get("output_format", 0),
                    result.get("persona", 0)
                ]
                result["final_score"] = round(sum(scores) / len(scores), 1)
            return result
        except json.JSONDecodeError:
            return {
                "clarity": 0,
                "specificity": 0,
                "context": 0,
                "output_format": 0,
                "persona": 0,
                "final_score": 0,
                "explanation": "Failed to parse response",
                "suggestions": [response.content]
            }
    except Exception as e:
        return {
            "clarity": 0,
            "specificity": 0,
            "context": 0,
            "output_format": 0,
            "persona": 0,
            "final_score": 0,
            "explanation": f"Error: {str(e)}",
            "suggestions": []
        }

def display_results(result):
    print("\nScores:")
    print(f"Clarity: {result.get('clarity', 0)}/10")
    print(f"Specificity: {result.get('specificity', 0)}/10")
    print(f"Context: {result.get('context', 0)}/10")
    print(f"Output Format: {result.get('output_format', 0)}/10")
    print(f"Persona: {result.get('persona', 0)}/10")
    print(f"\nFinal Score: {result.get('final_score', 0)}/10")
    print(f"\nExplanation:\n{result.get('explanation', 'N/A')}")
    print("\nSuggestions:")
    for i, suggestion in enumerate(result.get('suggestions', []), 1):
        print(f"{i}. {suggestion}")

def main():
    print("Prompt Quality Scoring Agent")
    print("Evaluate prompt quality based on 5 criteria")
    
    while True:
        user_input = input("\nEnter 'score' to evaluate a prompt, or 'quit' to exit: ").strip().lower()
        
        if user_input == 'quit':
            print("Exiting.")
            break
        
        if user_input == 'score':
            print("Enter your prompt below.")
            print("When finished, enter '###END###' on a new line:")
            
            lines = []
            while True:
                line = input()
                if line.strip() == '###END###':
                    break
                lines.append(line)
            
            prompt_text = '\n'.join(lines)
            
            if not prompt_text.strip():
                print("Error: No prompt provided.")
                continue
            
            print("\nEvaluating prompt...")
            
            result = score_prompt(prompt_text)
            display_results(result)
        else:
            print("Invalid input. Please enter 'score' or 'quit'.")

if __name__ == "__main__":
    main()
