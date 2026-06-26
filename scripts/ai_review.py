import os
from pathlib import Path

# Optional: install openai and set OPENAI_API_KEY in GitHub Secrets.
# This script is intentionally simple for a student demo.
# It can print a mock AI review if no API key is available.

TERRAFORM_PATH = Path("terraform/flawed/main.tf")

def mock_review(terraform_code: str) -> str:
    return """# AI IaC Review Findings

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

def real_openai_review(terraform_code: str) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = f"""
Review this Terraform code for:
1. Security risks
2. Cost concerns
3. Naming and governance violations
4. Suggested fixes

Return the response using severity levels: Critical, High, Medium, Low.

Terraform code:
```hcl
{terraform_code}
```
"""

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": "You are a cloud security and DevOps reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content

def main():
    terraform_code = TERRAFORM_PATH.read_text()

    if os.getenv("OPENAI_API_KEY"):
        review = real_openai_review(terraform_code)
    else:
        review = mock_review(terraform_code)

    print(review)

    Path("ai-review-output.md").write_text(review)

if __name__ == "__main__":
    main()
