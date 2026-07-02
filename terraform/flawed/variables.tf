variable "location" {
  description = "Azure region where the demo resources will be created"
  type        = string
  default     = "Canada Central"
}

variable "vm_size" {
  description = "International cost issue: oversized VM for a test workload. This is a flaw in the demo and should be corrected to a smaller size."
  type        = string
  default     = "Standard_D8s_v3"
}