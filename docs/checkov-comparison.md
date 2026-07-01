# Checkov Scan Comparison

## Flawed Terraform
Checkov failures: 15

## Fixed Terraform
Checkov failures: 11

## Result
The fixed version reduced the number of Checkov failures by 4.

## Main Improvements
- Removed public IP exposure from the VM.
- Restricted SSH access.
- Disabled public storage access.
- Added governance tags.
- Improved naming standards.
- Reduced VM size for cost optimization.

## Note
The fixed version still has some Checkov findings because Checkov applies enterprise-level security rules. For this academic demo, the focus is on demonstrating improvement and showing how AI can summarize and explain the most important IaC risks.