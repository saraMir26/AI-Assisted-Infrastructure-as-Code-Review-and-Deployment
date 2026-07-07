variable "location" {
  description = "Azure region where the demo resources will be created."
  type        = string
  default     = "Canada Central"
}

variable "vm_size" {
  description = "Cost-optimized VM size for a demo or test workload."
  type        = string
  default     = "Standard_B1s"
}