from http import client
import os
from pathlib import Path
from urllib import response
from click import prompt
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Optional: install openai and set OPENAI_API_KEY in GitHub Secrets.
# This script is intentionally simple for a student demo.
# It can print a mock AI review if no API key is available.

TERRAFORM_PATH = Path("terraform/flawed/main.tf")
OUTPUT_PATH = Path("ai-review-output.md")

def mock_review() -> str:
    return """# AI IaC Review Findings - The Mock Reeview

## Critical
- Storage account allows public network access. This may expose data to the internet.
- NSG rule allows SSH from 0.0.0.0/0. This creates a public attack surface.

## High
- Resource tags are missing. Add tags such as environment, owner, project, and costCenter.
- Naming does not follow a clear standard. Use a consistent naming convention.

## Medium
- VM size appears oversized for a test workload. Consider a smaller SKU for cost optimization.

## Suggested Fixes
- Disable public network access for storage.
- Restrict SSH access to a trusted IP range or use Azure Bastion.
- Add required tags.
- Use a smaller VM size for demo/test environments.
"""

def azure_openai_review(terraform_code: str) -> str:

    client = OpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
    )

    prompt = f"""
Review this Terraform code for an Azure deployment.

Check for:
1. Security risks
2. Cost concerns
3. Naming standard violations
4. Missing tags
5. Governance issues
6. Suggested fixes

Return the answer in Markdown.

Terraform:

```hcl
{terraform_code}
```
"""

    response = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input=prompt,
    )

    return response.output_text

def main():
    terraform_code = TERRAFORM_PATH.read_text(encoding="utf-8")

    required_vars = [
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_DEPLOYMENT",
    ]

    if all(os.getenv(var) for var in required_vars):
        print("Using Azure OpenAI review...")
        try:
            review = azure_openai_review(terraform_code)
        except Exception as e:
            print(f"Azure OpenAI failed: {e}")
            print("Falling back to mock review...")
            review = mock_review()
    else:
        print("Azure OpenAI configuration not found. Using mock review...")
        review = mock_review()

    print(review)
    OUTPUT_PATH.write_text(review, encoding="utf-8")

if __name__ == "__main__":
    main()
