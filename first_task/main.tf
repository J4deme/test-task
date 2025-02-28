terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>2.31.1"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "my_rsg"
  location = "westeurope"

  tags = {
    enviroment = "dev"
    source     = "Terraform"
  }
}
