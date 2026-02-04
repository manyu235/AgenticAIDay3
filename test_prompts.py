from prompt_scorer import score_prompt, display_results

test_prompts = [
    {
        "name": "Test 1: Very Poor Prompt",
        "prompt": "Write something."
    },
    {
        "name": "Test 2: Poor Prompt - No Specifics",
        "prompt": "Tell me about AI."
    },
    {
        "name": "Test 3: Below Average - Some Details",
        "prompt": "Write an article about climate change with some facts."
    },
    {
        "name": "Test 4: Average - Has Role and Topic",
        "prompt": "You are a teacher. Explain photosynthesis to students."
    },
    {
        "name": "Test 5: Good - Has Role, Topic, and Audience",
        "prompt": "You are a marketing expert. Write a social media post about our new product launch targeting millennials."
    },
    {
        "name": "Test 6: Very Good - Multiple Elements",
        "prompt": "You are a technical writer. Create a user guide for our mobile app. Include step-by-step instructions with screenshots. Target audience is non-technical users."
    },
    {
        "name": "Test 7: Excellent - All Elements Present",
        "prompt": "You are a financial analyst. Write a 500-word investment report on Tesla stock for retail investors. Include current valuation, growth prospects, and risks. Use professional tone with bullet points for key metrics."
    },
    {
        "name": "Test 8: Excellent - Comprehensive Prompt",
        "prompt": "You are an HR compliance auditor. Review the following remote work policy and identify missing compliance clauses, ambiguous language, and suggest improvements. Return output in JSON format with keys: issues, severity, recommendations. Cite references where applicable."
    },
    {
        "name": "Test 9: Good - Clear but Missing Some Details",
        "prompt": "As a project manager, draft a status update email to the client about the website redesign project. Mention completed milestones and next steps."
    },
    {
        "name": "Test 10: Average - Has Goal but Lacks Structure",
        "prompt": "Summarize this meeting transcript and list action items."
    }
]

def run_all_tests():
    print("Running all test prompts...\n")
    print("=" * 80)
    
    for i, test in enumerate(test_prompts, 1):
        print(f"\n{test['name']}")
        print("-" * 80)
        print(f"Prompt: {test['prompt']}")
        
        result = score_prompt(test['prompt'])
        display_results(result)
        
        print("\n" + "=" * 80)
        
        if i < len(test_prompts):
            input("\nPress Enter to continue to next test...")

if __name__ == "__main__":
    run_all_tests()
