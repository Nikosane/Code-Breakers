def analyze_tool(tool, snippet):
    if tool == "key_analysis":
        return {"success": "AB" in snippet or "XX" in snippet}
    elif tool == "pattern_recognition":
        return {"success": snippet.endswith("CD")}
    return {"success": False}
