terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.100"
    }
  }
}

provider "azurerm" {
  features {}
}

locals {
  common_tags = {
    environment = "demo"
    project     = "cloudnova-iac-review"
    owner       = "group-3"
    costCenter  = "academic"
  }
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-cloudnova-iac-demo-cc-001"
  location = "Canada Central"
  tags     = local.common_tags
}

resource "azurerm_storage_account" "storage" {
  name                            = "stcloudnovaiacdemo001"
  resource_group_name             = azurerm_resource_group.rg.name
  location                        = azurerm_resource_group.rg.location
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  public_network_access_enabled   = false
  allow_nested_items_to_be_public = false
  tags                            = local.common_tags
}

variable "vm_size" {
  default = "Standard_B1s"
}