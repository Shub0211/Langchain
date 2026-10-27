from langchain_community.tools import DuckDuckGoSearchRun, ShellTool


#DuckDuckGo built-in tool
search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('ipl news')

# print(results)

#Shell tool
shell_tool = ShellTool()
results = shell_tool.invoke('ls')
# print(results)

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)






























