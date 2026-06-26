# CloudNova AI-Assisted IaC Review and Deployment

## Project Topic
Group 3: AI-Assisted Infrastructure as Code Review and Deployment

## Scenario
CloudNova is a mid-size SaaS company. Their DevOps team uses Terraform and deploys infrastructure changes frequently. Manual pull request reviews are slow and sometimes miss security, governance, and cost issues. This prototype shows how AI can review Terraform before deployment.

## Demo Flow
1. Developer opens a Pull Request with flawed Terraform code.
2. GitHub Actions runs:
   - Terraform validation
   - Checkov static security scan
   - AI review script
3. AI reviews the Terraform file for:
   - Security risks
   - Cost concerns
   - Naming/governance violations
   - Suggested fixes
4. Findings are posted in the workflow output.
5. Team fixes the Terraform.
6. Pipeline runs successfully and Terraform plan is generated.

## Team Work Split
- Member 1: Coordinator & Story
- Member 2: Cloud Architecture & IaC Grounding
- Member 3: AI Workflow
- Member 4: Demo Driver
- Member 5: Governance & Critical Analysis

## Repository Structure
```text
.github/workflows/      GitHub Actions pipeline
terraform/flawed/       Terraform with intentional issues for the demo
terraform/fixed/        Improved Terraform version
scripts/                AI review script
docs/                   Slides notes and member sections
```

## Important
This demo is for academic purposes. Use `terraform plan` for the presentation unless the group is ready to deploy real Azure resources.
