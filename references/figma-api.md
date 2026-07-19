# Figma MCP API Reference

Official remote Model Context Protocol (MCP) server integration for Figma.

* **Connection URL:** `https://mcp.figma.com/mcp`
* **Transport:** Remote HTTP (OAuth authentication)

## Exposed Tools

* `figma/get_design_context`: Retrieves styling, variables, layout, and property metadata for a selected frame or layer.
* `figma/get_variable_defs`: Retrieves the variables and design token values in a selection.
* `figma/get_code_connect_map`: Retrieves production component mapping information.
* `figma/get_code_connect_suggestions`: Retrieves mapping recommendations.
* `figma/get_screenshot`: Captures a high-resolution screenshot of the selected layer/frame.

## OAuth Authentication Flow

Figma MCP uses standard web-based OAuth. On the first tool call to the figma server:
1. The client will output a prompt to authenticate.
2. A browser tab will open requesting permissions to connect your Figma account.
3. Once approved, the access tokens are securely managed by the client application.
